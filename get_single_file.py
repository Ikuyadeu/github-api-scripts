# -*- coding: utf-8 -*-
"""
Summary: Get single file history and real file
Usage: mkdir out
       pip3 install requests
       python3 GetSyngleFile.py filePath
       (e.g.) python3 GetSyngleFile.py package.json
Warning: This script can't get identify Readme.md README.md
"""
import json
import sys
import configparser
import requests

ARGS = sys.argv
config = configparser.ConfigParser()
config.read('config.conf')
user = config["Git Hub"]["id"]
password = config["GitHub"]["password"]
owner = config["Target"]["owner"]
repo = config["Target"]["repo"]
PATH = ARGS[1]
OUT_DIR = "out/"

PROJECT_PATH = owner + "/" + repo

URL = "/".join(["https://api.github.com/repos",
                PROJECT_PATH,
                "commits"])

RAW_URL = "https://raw.githubusercontent.com/" + PROJECT_PATH


AUTH = requests.auth.HTTPBasicAuth(user, password)
PARAMS = {"path": PATH,
          "per_page": 100,
          "page": 1,}
COMMITS = []

# Get All commit log
while True:
    RESP = requests.get(URL,
                        params=PARAMS,
                        auth=AUTH)
    CONTENT = json.loads(RESP.content.decode("utf-8"))
    if len(CONTENT) <= 1 or PARAMS["page"] > 10:
        break
    PARAMS["page"] += 1
    COMMITS.extend(CONTENT)
    print("Get commits from %s" % RESP.url)

# Output Commit log
OUT_FILE_PATH = owner +"-" + repo + ".json"
with open(OUT_FILE_PATH, "w") as f:
    json.dump(COMMITS, f, indent=4)
    print("Output commit log to %s" % OUT_FILE_PATH)

# Curl real files
COMMITS_LEN = len(COMMITS)
for i, commit in enumerate(reversed(COMMITS)):
    FILE_URL = "/".join([RAW_URL, commit["sha"], PATH])
    CONTENT = requests.get(FILE_URL, auth=AUTH).content.decode("utf-8")
    with open(str(i) + "-" + PATH, "w") as f:
        f.write(CONTENT)
    sys.stdout.write("\r%d / %d Output File " % (i + 1, COMMITS_LEN))
