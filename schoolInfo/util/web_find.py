import aiohttp
from bs4 import BeautifulSoup

import datetime
import random

import json
import asyncio
import re


class HTMLGetter:
    def __init__(
        self,
        headers: dict = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        },
    ):
        self.headers = headers

    async def get_html(self, url: str):
        async with aiohttp.ClientSession() as cs:
            html = await cs.get(url, headers=self.headers)
            return await html.text()

    async def get_json(self, url: str):
        html = await self.get_html(url)
        data = BeautifulSoup(html, "html.parser")
        jsonData = json.loads(data.get_text())
        return jsonData


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        HTMLGetter().get_json(
            "https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=T10&SD_SCHUL_CODE=9296071"
        )
    )
