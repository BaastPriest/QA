import pytest

import data
import functions

def test_create_booking_success_firstname():
    body = functions.change_booking_body()
    req = functions.create_booking(body).status_code
    exp = 200      # 300
    assert req == exp, f'Expected: {exp}, Actual {req}'

#параметризация
@pytest.mark.parametrize("totalprice", # дока про pytest
                         [
                             pytest.param(99999999999, id="1_BigNumbers"),
                             pytest.param(1, id="2_SmallNumbers"), #можно не указывать ID
                             pytest.param(0, id="3_ZeroNumbers"),
                             pytest.param(34.565, id="4_ZeroNumbers")
                         ])
def test_create_booking_success_totalprice(totalprice):
    body = functions.change_booking_body("totalprice", 2)
    req = functions.create_booking(body).status_code
    exp = 200
    assert req == exp, f'Expected: {exp}, Actual {req}' # можно добавить описание в выводе

# удалить бронирование
def test_delete_booking_success():
    id = functions.create_booking(data.booking_body).json()["bookingid"]
    req = functions.delite_booking(id).status_code
    exp = 201 # статус код из API DeleteBooking
    assert req == exp