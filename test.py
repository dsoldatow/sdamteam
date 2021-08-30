import requests


if __name__ == '__main__':
    response = requests.post(
        'http://localhost:8080/vk_callback',
        json={'type': 'message_new', 'group_id': '1', 'object': {'text': 'blabla', 'from_id': '123'}},
    )
    print(response.text)
