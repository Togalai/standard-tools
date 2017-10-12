import requests, json


def print_pretty_json(j):
    print(json.dumps(j, sort_keys=True, indent=4))


def input_api_url(url):
    raw_json = requests.get(url)
    json_decoded = json.loads(raw_json)
    return json_decoded