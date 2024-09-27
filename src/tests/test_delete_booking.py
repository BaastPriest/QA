from src import sender_stand_request


def test_delete_booking(booking_body):
    resp = sender_stand_request.create_booking(booking_body)
    assert resp.status_code == 200, f"Expected 200, but got {resp.status_code}"
    booking_id = resp.json()["bookingid"]
    del_resp = sender_stand_request.delete_booking(booking_id)
    assert del_resp.status_code == 201, f"Expected 201, but got {del_resp.status_code}"
    resp_get = sender_stand_request.get_booking(booking_id)
    assert resp_get.status_code == 404, f"Expected 404, but got {resp_get.status_code}"


def test_delete_booking_twice(booking_body):
    resp = sender_stand_request.create_booking(booking_body)
    booking_id = resp.json()["bookingid"]
    sender_stand_request.delete_booking(booking_id)
    del_resp_second = sender_stand_request.delete_booking(booking_id)
    assert del_resp_second.status_code in [404, 410, 405],\
        f"Expected 404, 410 or 405, but got {del_resp_second.status_code}"


def test_delete_nonexistent_booking():
    nonexistent_booking_id = 9999999
    del_resp = sender_stand_request.delete_booking(nonexistent_booking_id)
    assert del_resp.status_code in [404, 405], f"Expected 404/405, but got {del_resp.status_code}"


def test_delete_booking_without_auth(booking_body):
    resp = sender_stand_request.create_booking(booking_body)
    booking_id = resp.json()["bookingid"]
    del_resp = sender_stand_request.delete_booking(booking_id,use_auth=False)
    assert del_resp.status_code in [401, 403], f"Expected 401 or 403, but got {del_resp.status_code}"


def test_delete_booking_with_invalid_token(booking_body):
    resp = sender_stand_request.create_booking(booking_body)
    booking_id = resp.json()["bookingid"]
    del_resp = sender_stand_request.delete_booking(booking_id, custom_token="invalid_token_value")
    assert del_resp.status_code == 403, f"Expected 403, but got {del_resp.status_code}"
