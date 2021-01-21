import json
from csv import DictWriter, DictReader
from time import sleep
from typing import Generator
from requests import exceptions, post
import configparser


class OrgCollector:
    MAX_FETCH_RETRY = 3
    fields = [
        "name",
        "login",
        "email"
    ]

    def __init__(self, token: str):
        self.cursor = None
        self._headers = {"Authorization": f"token {token}"}

    def save_all(self, output_path: str):
        with open(output_path, 'w', encoding='utf-8', buffering=1) as f:
            json.dump(self.all(), f, indent=1)
            # writer = DictWriter(f, self.fields)
            # writer.writeheader()
            # for row in self.all():
            #     writer.writerow(row)
            print("\nFinish to collect the repo list. Output is " + output_path)

    def all(self):
        self.cursor = None

        orgs = {}
        with open('orgs_short.csv', 'r') as org_list:
            reader = DictReader(org_list)
            for org in reader:
                org_name = org['login']
                print(org_name)
                output =self._generator(org_name)
                try:
                    orgs[org_name] = [x['node']['name'] for x in output['data']['organization']['repositories']['edges']]
                except TypeError:
                    orgs[org_name] = []
        return orgs

    def _generator(self, org):
        nth_retry = 0
        try:
          res = post(
                'https://api.github.com/graphql',
                headers=self._headers,
                data=self._graphql_request(org),
            ).json()
          if "errors" in res:
            if nth_retry < self.MAX_FETCH_RETRY:
              nth_retry += 1
              # Magic number to avoid timeout
              sleep(10)
            else:
              nth_retry = 0
              print(res["errors"])
          return res
        except exceptions.HTTPError as http_err:
            raise http_err
        except Exception as err:
            raise err

    def _graphql_request(self, org) -> str:
        """GitHub GraphQL Query

        See https://developer.github.com/v4/object/pullrequest/
        """
        query = '''
query { 
  
    rateLimit {
        remaining
        resetAt
    }
  	organization(login: "%(repo_org)s"){
    repositories(first: 10) {
      edges{
        node{
          name
        }
      }
    }
  }
}
        ''' % {'repo_org': org}
        # return query
        return json.dumps({'query': query}).encode('utf-8')



if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.conf')
    token = config["GitHub"]["token"]
    collector = OrgCollector(token)
    collector.save_all('repos.json')