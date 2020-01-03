from .http import HttpClient
import aiohttp
import asyncio

class FluxpointClient:
    def __init__(self, user_agent: str, token: str, loop: asyncio.AbstractEventLoop=asyncio.get_event_loop()):
        self.global_headers = {}
        self.token = token
        self.session = aiohttp.ClientSession(loop=loop)
        self.http = HttpClient(self.session, self.token)