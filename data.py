CREATE_COURIER_DUPLICATION_ERROR = "Этот логин уже используется. Попробуйте другой."
CREATE_COURIER_EMPTY_FIELD_ERROR = "Недостаточно данных для создания учетной записи"
LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR = "Учетная запись не найдена"
LOGIN_WITH_EMPTY_FIELD_ERROR = "Недостаточно данных для входа"


def order_data(color=''):
    data = {
        "firstName": "Юлия",
        "lastName": "Гармай",
        "address": "г.Москва",
        "metroStation": "Павелецкая",
        "phone": "+79105244144",
        "rentTime": 5,
        "deliveryDate": "2025-10-15",
        "comment": "Поехали",
    }
    if color:
        data["color"] = color

    return data
