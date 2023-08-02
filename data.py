booking_body = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}


header = {
"Cookie": "token=abc123"    # из API DeleteBooking
}

# body API CreateToken
auth_body = {
    "username": "admin",
    "password": "password123"
}