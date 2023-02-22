import requests
from requests.structures import CaseInsensitiveDict

def add_order(token, bookId, customerName):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    body = {
        'bookId': bookId,
        'customerName': customerName
    }
    response = requests.post('https://simple-books-api.glitch.me/orders', headers=headers, json=body)
    return response

def delete_order(token, orderId):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers)
    return response

def get_one_order(token, orderId):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers)
    return response

def get_all_order(token):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.get(f'https://simple-books-api.glitch.me/orders', headers=headers)
    return response

def edit_order(token, orderId, customerName):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    body = {
        'customerName': customerName
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers, json=body)
    return response