import asyncio

import schoolInfo

async def main():
    school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
    print(school_data)
    
    meal_data : dict = await schoolInfo.meal(ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"], SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"])
    print(meal_data)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
