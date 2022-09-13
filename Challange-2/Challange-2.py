import requests
import json

metadata_url = 'http://169.254.169.254/latest/'
#from get_metadata import get_metadata

def convert_funct(url, arr):
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = convert_funct(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output


def get_metadata():
    initial = ["meta-data/"]
    result = convert_funct(metadata_url, initial)
    return result


def get_metadata_json():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    metadata = get_metadata()
    return list(gen_dict_extract(key, metadata))
#from get_metadata import get_metadata

if __name__ == '__main__':
    print(get_metadata_json())
    key = input("What key details you like to view ?\n")
    print(find_key(key))
