from requests import Session
from .error import UnauthorisedError


class ClimateGuardApi:
    BASE_URL = 'https://api.climateguard.info'
    API_PREFIX = '/api/telegramBot'
    API_URL = BASE_URL + API_PREFIX
    _request = Session()
    token = ''

    def __init__(self, login: str, password: str):
        token: bool = self._token_obtain(login, password)
        if not token:
            raise UnauthorisedError('Unauthorised')
        else:
            self.token = token
            self._request.headers.update({'Authorization': f'Bearer {token}'})

    def _token_obtain(self, login: str, password: str):
        json = {'email': login, 'password': password}
        response = self._request.post(f'{self.BASE_URL}/api/loginViaApi', json=json)
        data = response.json()
        if 'error' in data:
            return False;
        if 'success' in data:
            success: dict = data['success']
            return success.get('access_token')
