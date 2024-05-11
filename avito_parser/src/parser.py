import asyncio
import aiohttp
from typing import Protocol
from config import conf
from bs4 import BeautifulSoup
import aiofiles


class Parser(Protocol):

    async def make_query(url: str = conf.crimea_land.url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                return html

    async def scrap_adv_links(html):
        async with aiofiles.open(f"{html}", mode="r") as f:
            lxml_file = await f.read()
        
    async def collect_links():
        pass

    async def next_page():
        pass

    





class AvitoParser()
