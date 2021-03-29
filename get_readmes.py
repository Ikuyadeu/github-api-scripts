from get_single_file import collect_readme_file
# from csv import DictWriter, DictReader
import json
import configparser

config = configparser.ConfigParser()
config.read('config.conf')
user = config['GitHub']['id']
token = config["GitHub"]["token"]
with open("repos.json", 'r', encoding='utf-8', buffering=1) as f:
    reader = json.load(f)
    for org, repos in reader.items():
        for repo in repos:
            collect_readme_file(user, token, org, repo, './readmes')