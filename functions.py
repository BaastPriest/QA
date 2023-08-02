import requests
import data
import url


def create_booking(body):
    return requests.post(url.URL + url.CREATE_BOOKING, json=body)

# def change_booking_body():
#     new_booking_body = data.booking_body.copy()
#     new_booking_body["firstname"] = "AAA"
#     return new_booking_body

#параметризация
def change_booking_body(field, name):
    new_booking_body = data.booking_body.copy()
    new_booking_body[field] = name
    return new_booking_body

def create_token(): # из API CreateToken
    token = requests.post(url.URL + url.AUTH, json=data.auth_body).json()["token"]
    return token
# print(create_token()) # для проверки что функция работает

def delite_booking(id_booking):
    headers = data.header.copy()
    headers["Cookie"] = "token=" + create_token()   # формат Header в API DeleteBooking
    req = requests.delete(url.URL + url.DELETE_BOOKING + str(id_booking),  # метод delete
                          headers = headers)
    return req


