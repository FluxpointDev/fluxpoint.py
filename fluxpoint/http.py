from .exceptions import MalformedJsonException
import aiohttp
import sys

class HttpClient:
    def __init__(self, token: str, session: aiohttp.ClientSession, other_headers=None):
        self.session = session
        self.token = token

        self.headers = {
            "User-Agent": "fluxpoint.py/1.0.0",
            "X-Powered-By": f"Python/{sys.version} aiohttp/{aiohttp.__version__}"
        }

    async def parse(res):
        try:
            r = await res.json()
            return r
        except e as MalformedJsonException:
            raise e

    async def get(url: str, params=None, headers=None):
        headers = headers or {}
        headers.update(self.headers)

        async with self.session.get(url=url, params=params, headers=headers) as res:
            json = await parse(res)
            await res.release()
            return json