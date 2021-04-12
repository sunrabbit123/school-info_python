import asyncio
import datetime
from pytz import timezone as tz
import re

import schoolInfo.util as util

async def meal(ATPT_OFCDC_SC_CODE : str, SD_SCHUL_CODE : str, MLSV_YMD : datetime.datetime, timezone : str = "Asia/Seoul") -> dict :
    MLSV_YMD = datetime.datetime.now(tz(timezone))
    MLSV__YMD = re.sub("[^0-9]", "", str(MLSV_YMD.__str__()))[2:8]



    option = [f"MLSV_YMD={MLSV__YMD}", f"ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}", f"SD_SCHUL_CODE={SD_SCHUL_CODE}"]
    url : str = util.url_manager(type="mealServiceDietInfo").url
    return await util.HTMLGetter().get_json(url)