import ssl
import requests
from time import time
from os import environ
from hashlib import md5

PUBLIC_API_KEY = environ.get("PUBLIC_API_KEY")
PRIVATE_API_KEY = environ.get("PRIVATE_API_KEY")
BASE_URL = "https://gateway.marvel.com"
endpoint = "/v1/public/characters"
api_url = f"{BASE_URL}{endpoint}"


def get_auth_hash(ts):
    timestamp = ts
    auth_params = (timestamp + PRIVATE_API_KEY + PUBLIC_API_KEY).encode("utf-8")
    return md5(auth_params).hexdigest()


def get_url(search_term):
    ts = str(time())
    auth_hash = get_auth_hash(ts)
    params = f"nameStartsWith={search_term}"
    auth = f"ts={ts}&apikey={PUBLIC_API_KEY}&hash={auth_hash}"
    return f"{api_url}?{params}&{auth}"


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
        kwargs["ssl_context"] = ctx
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)
