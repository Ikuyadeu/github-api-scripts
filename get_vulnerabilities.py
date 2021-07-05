"""
途中まで作ったけど最終的に動かなかったので供養
"""


import json
import sys
from csv import DictWriter
from datetime import datetime, timezone
from time import sleep
from typing import Generator, Optional
from requests import exceptions, request, post
from urllib.error import HTTPError
from urllib.request import urlopen, Request


class PullsCollector:
    MAX_FETCH_RETRY = 3
    fields = [
        "number",
        "createdAt",
        "name",
        "severity",
        "vulnerableVersionRange"
    ]

    def __init__(self, token: str, repo_owner: str, repo_name: str, repo_branch = "master"):
        self._token = token
        self._repo_owner = repo_owner
        self._repo_name = repo_name
        self._repo_branch = repo_branch
        self._headers = {"Authorization": f"token {token}"}
        self.cursor = None

    def save_all(self, output_path: str):
        with open(output_path, 'w', encoding='utf-8', buffering=1) as f:
            writer = DictWriter(f, self.fields)
            writer.writeheader()
            for row in self.all():
                writer.writerow(row)
            print("\nFinish to collect the vulnerablity list. Output is " + output_path)

    def all(self) -> Generator:
        self.cursor = None
        gene = self._generator()
        hasNextPage = True
        while hasNextPage:
            obj = next(gene)
            if "errors" in obj:
              continue

            for pull in (edge['node'] for edge in obj['data']['repository']['vulnerabilityAlerts']['edges']):
                yield self._format(pull)
            hasNextPage = obj['data']['repository']['vulnerabilityAlerts']['pageInfo']['hasNextPage']
            self.cursor = obj['data']['repository']['vulnerabilityAlerts']['pageInfo']['endCursor']
            if obj['data']['rateLimit']['remaining'] < 1:
                reset_at = self._parse_datetime(obj['data']['rateLimit']['resetAt'])
                delta = reset_at - datetime.now(timezone.utc)
                sleep(delta.seconds)

    def _generator(self):
        nth_retry = 0
        while(True):
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
                  continue
                else:
                  nth_retry = 0
                  print(res["errors"])
              yield res
            except exceptions.HTTPError as http_err:
                raise http_err
            except Exception as err:
                raise err

    def _graphql_request(self) -> str:
        """GitHub GraphQL Query

        See https://developer.github.com/v4/object/pullrequest/
        """
        query = '''
            query($cursor: String) {
              rateLimit {
                remaining
                resetAt
              }
              repository(owner: "%(repo_owner)s", name: "%(repo_name)s") {
                vulnerabilityAlerts(after: $cursor, first: 50) {
                  pageInfo {
                    hasNextPage
                    endCursor
                  }
                  edges {
                    node {
                      createdAt
                      securityVulnerability {
                        package {
                          name
                        }
                        severity
                        vulnerableVersionRange
                      }
                    }
                  }
                }
              }
            }
        ''' % {'repo_owner': self._repo_owner, 'repo_name': self._repo_name, 'repo_branch': self._repo_branch}
        # return query
        return json.dumps({'query': query, 'variables': {'cursor': self.cursor}}).encode('utf-8')

    def _format(self, vuln: dict) -> dict:
        return {
            "commit_len": vuln['commits']['totalCount'],
            "base_commit_sha": vuln['baseRefOid'],
            "merge_commit_sha": vuln['headRefOid'],
            "created_at": self._parse_datetime(vuln['createdAt']),
            "merged_at": self._parse_datetime(vuln['mergedAt']),
            "merged_by": self._merged_by(vuln)
        }

    def _parse_datetime(self, d: str) -> datetime:
        return datetime.strptime(d, '%Y-%m-%dT%H:%M:%SZ')

    def _merged_by(self, vuln: dict) -> Optional[str]:
        merged_by = vuln.get('mergedBy')
        if merged_by is None:
            return None
        return merged_by.get('login')

if __name__ == "__main__":
    collector = PullsCollector("995a00abc096ec3203f1fe85b134bf8d2d0c9574", "kubernetes", "kubernetes")
    for x in collector.all():
      # if x["created_at"] > datetime.strptime("2019-1-1", '%Y-%m-%d'):
      print(x)