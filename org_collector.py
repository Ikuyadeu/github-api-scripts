import json
from csv import DictWriter
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
            writer = DictWriter(f, self.fields)
            writer.writeheader()
            for row in self.all():
                writer.writerow(row)
            print("\nFinish to collect the pull list. Output is " + output_path)

    def all(self) -> Generator:
        self.cursor = None
        # gene = self._generator()
        # hasNextPage = True
        output =self._generator()
        # while hasNextPage:
        #     obj = next(gene)
        #     if "errors" in obj:
        #       continue
        orgs = [x['node'] for x in output['data']['search']['edges']]
        #     output.extend(orgs)
        #     break
        #     if obj['data']['rateLimit']['remaining'] < 1:
        #         break
        return orgs

    def _generator(self):
        nth_retry = 0
        try:
          res = post(
                'https://api.github.com/graphql',
                headers=self._headers,
                data=self._graphql_request(),
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

    def _graphql_request(self) -> str:
        """GitHub GraphQL Query

        See https://developer.github.com/v4/object/pullrequest/
        """
        query = '''
{
    rateLimit {
        remaining
        resetAt
    }
    search(query: "type:org repos:>50", type: USER, first: 100) {
        repositoryCount
        edges {
            node {
            ... on Organization {
                name
                login
                email
                }
            }
        }
    }
}
        '''
        # return query
        return json.dumps({'query': query}).encode('utf-8')



if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.conf')
    token = config["GitHub"]["token"]
    collector = OrgCollector(token)
    collector.save_all('orgs.csv')