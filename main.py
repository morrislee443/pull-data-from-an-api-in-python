import requests
import json

from requests import Response


# This is for demonstration purpose only, example
def pull_data_from_an_API(url: str, key1: str, key2: str, key3: str, key4: str):
    response_API = requests.get(url)
    data = response_API.text
    parsed_json = json.loads(data)
    return parsed_json[key1][key2][key3][key4]


def connect_to_an_api(url: str):
    return requests.get(url)


def get_the_data_from_API(response_API: Response):
    return response_API.text


def parse_the_data_into_JSON_format(data: str):
    return json.loads(data)


def extract_the_data_and_print_it(parsed_json: any, key1: str, key2: str, key3: str, key4: str):
    return parsed_json[key1][key2][key3][key4]


if __name__ == '__main__':
    active_case = pull_data_from_an_API('https://api.covid19india.org/state_district_wise.json', 'Andaman and Nicobar Islands', 'districtData', 'South Andaman', 'active')
    print("Active cases in South Andaman:", active_case)

