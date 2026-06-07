from api.login.login_api import LoginAPI
from utils.read_data import read_json
from utils.schema_validate import validate_schema

login_api = LoginAPI()

def test_valid_login():
    data = read_json("test_data/login_data.json")

    payload = data["valid_user"]

    response = login_api.login(payload)

    assert response.status_code == 200

    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)

def test_invalid_login():
    data = read_json("test_data/login_data.json")

    payload = data["invalid_user"]

    response = login_api.login(payload)

    assert response.status_code in [400, 401]

def test_login_schema_valid():
    data = read_json("test_data/login_data.json")

    payload = data["valid_user"]

    login_schema = {
        "type": "object",
        "properties": {
            "statusCode": {"type": "integer"},
            "message": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "userId": {"type": "integer"},
                    "email": {"type": "string", "format": "email"},
                    "role": {"type": "string"},
                    "status": {"type": "string"},
                    "createdDateTime": {"type": ["string", "null"]},
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"},
                    "city": {"type": "string"},
                    "state": {"type": "string"},
                    "country": {"type": "string"},
                    "zoneId": {"type": "string"},
                    "imageId": {"type": ["string", "null"]},
                    "jwtToken": {"type": "string"}
                },
                "required": [
                    "userId",
                    "email",
                    "role",
                    "status",
                    "firstName",
                    "lastName",
                    "jwtToken"
                ]
            }
        },
        "required": ["statusCode", "message", "data"]
    }
    response = login_api.login(payload)

    assert response.status_code == 200

    response_json = response.json()

    validate_schema(response_json, login_schema)