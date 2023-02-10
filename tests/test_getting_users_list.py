import requests

from configuration import SERVICE_URL

from src.baseclasses.response import Response

from src.schemas.user import User

def test_getting_users_list():
  r = requests.get(url=SERVICE_URL)
  test_object= Response(r)
  test_object.assert_status_code(200).validate(User)

