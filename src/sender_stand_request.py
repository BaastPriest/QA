import requests
from src import configuration, data


def create_booking(booking_body):
    response = requests.post(configuration.BASE_URL + configuration.BOOKING_PATH, json=booking_body,
                             headers=configuration.HEADERS)
    return response


def get_booking(booking_id):
    response = requests.get(configuration.BASE_URL + configuration.BOOKING_PATH + f"/{booking_id}",
                            headers=configuration.HEADERS)
    return response


def partial_update_booking(booking_id, update_body):
    token = create_token()
    headers_with_auth = configuration.HEADERS.copy()
    headers_with_auth["Cookie"] = f"token={token}"
    response = requests.patch(configuration.BASE_URL + configuration.BOOKING_PATH + f"/{booking_id}",
                              json=update_body, headers=headers_with_auth)
    return response


def update_booking(booking_id, booking_body):
    headers_with_auth = configuration.HEADERS.copy()
    headers_with_auth['Authorization'] = 'Basic ' + 'YWRtaW46cGFzc3dvcmQxMjM='  # Это базовая авторизация с логином admin и паролем password123
    response = requests.put(configuration.BASE_URL + configuration.BOOKING_PATH + f"/{booking_id}", json=booking_body, headers=headers_with_auth)
    return response


def delete_booking(booking_id, use_auth=True, custom_token=None):
    headers = configuration.HEADERS.copy()
    if custom_token:
        headers["Cookie"] = f"token={custom_token}"
    elif use_auth:
        headers["Cookie"] = f"token={create_token()}"
    response = requests.delete(configuration.BASE_URL + configuration.BOOKING_PATH + f"/{booking_id}",
                               headers=headers)
    return response


def change_booking_body(field, name):
    new_booking_body = data.booking_body.copy()
    new_booking_body[field] = name
    # new_booking_body["firstname"] = name
    return new_booking_body


def create_token():
    response = requests.post(configuration.BASE_URL + configuration.AUTH_PATH,
                          json=data.auth_body, headers=configuration.HEADERS)
    token = response.json().get("token")
    return token


