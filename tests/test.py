import asyncio

import schoolInfo


async def main():
    print_end: str = "\n\n\n\n\n"
    school_data: dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
    print(school_data, end=print_end)

    meal_data: dict = await schoolInfo.meal(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )
    print(meal_data, end=print_end)

    schedule_data: dict = await schoolInfo.schedule(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )

    print(schedule_data, end=print_end)

    major_data: dict = await schoolInfo.major(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )

    print(major_data, end=print_end)

    class_data: dict = await schoolInfo.classes(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )

    print(class_data, end=print_end)

    timetable_data: dict = await schoolInfo.timetable(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
        SCHUL_KND_SC_NM=school_data["SCHUL_KND_SC_NM"],
    )

    print(timetable_data, end=print_end)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
