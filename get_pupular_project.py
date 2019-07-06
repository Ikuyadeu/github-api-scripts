"""
Get popular project
Before run
$ pip3 install PyGithub
"""

import requests
import json
import csv
from github import Github
import configparser
from time import sleep
import sys

config = configparser.ConfigParser()
config.read('config.conf')
user = config["GitHub"]["id"]
password = config["GitHub"]["password"]
language = config["Projects"]["lang"]
count = int(config["Projects"]["count"])
g = Github(user, password)

repos = g.search_repositories("stars:>0", sort="stars", language=language)

results = []
for i, x in enumerate(repos[:count]):
    sys.stdout.write("\rProcessing... : %d/%d projects" % (i + 1, count))
    ratelimit = g.get_rate_limit().core.remaining
    if ratelimit < 100:
        print("Sleeping for replenish rate limit")
        sleep(3600)
        ratelimit = g.get_rate_limit().core.remaining
    results.append({"repo": x.name, "owner": x.owner.login,
                    "url": x.url, "forks": x.forks, "stars": x.stargazers_count})

with open("popular_" + language + ".csv", "w") as org_file:
    writer = csv.DictWriter(
        org_file, ["repo", "owner", "url", "forks", "stars"])
    writer.writeheader()
    writer.writerows(results)