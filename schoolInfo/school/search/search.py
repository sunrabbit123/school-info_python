import asyncio

from schoolInfo.util import url_manager, HTMLGetter

async def search(keyword : str) -> dict:
    url : str = url_manager(type="schoolInfo")
    return await HTMLGetter().get_json(url)
