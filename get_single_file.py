# -*- coding: utf-8 -*-
"""
Summary: Get single file history and real file
Usage: mkdir out
       pip3 install requests
       python3 GetSyngleFile.py
Warning: This script can't get identify Readme.md README.md
"""
import configparser
import requests

def collect_readme_file(user, token, owner, repo):
    project_path = f'{owner}/{repo}'

    session = requests.Session()
    session.auth = (user, token)

    raw_url = f"https://raw.githubusercontent.com/{project_path}/master/README.md"
    content = session.get(raw_url).content.decode("utf-8")

    out_name = f'{owner}-{repo}.md'
    with open(out_name, "w") as f:
        f.write(content)
    print("Success to output %s " % (out_name))


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.conf')
    user = config['GitHub']['id']
    token = config["GitHub"]["token"]
    owner = config["Target"]["owner"]
    repo = config["Target"]["repo"]
    collect_readme_file(user, token, owner, repo)