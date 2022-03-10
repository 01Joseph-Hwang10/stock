import requests
from http import HTTPStatus
from scripts.helpers.env_to_dict import use_env
from shared.utils.constants import SERVER_URL

env = use_env()

headers = {
    'Authorization': env.secret_key
}

def main(expected = HTTPStatus.OK) -> bool:
    response = requests.get(SERVER_URL, headers=headers, timeout=5)
    print('Status Code : %d' % response.status_code)
    print('Response : ')
    try:
        response = response.json()
        print(response)
        return response['is_healthy']
    except:
        print(response.content)
    return response.status_code == expected
