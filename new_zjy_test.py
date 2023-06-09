from new_zjy_main import NewZjyApi

headers = {"sec-ch-ua": "\"Microsoft Edge\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
           "Accept": "text/html, */*; q=0.01", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "X-Requested-With": "XMLHttpRequest", "sec-ch-ua-mobile": "?0",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57",
           "sec-ch-ua-platform": "\"Windows\"", "Origin": "https://course.icve.com.cn", "Sec-Fetch-Site": "same-origin",
           "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
           "Referer": "https://course.icve.com.cn/learnspace/learn/learn/templateeight/content_video.action?params.courseId=149285800359ff8b7b1e19542c0f5a59___¶ms.itemId=96a03dbef3f2c98bf5706cadfed8ee5c¶ms.templateStyleType=0¶ms.parentId=caa8b78a5330aaf06eb6542b9ee395fc¶ms.rolePermissions=¶ms.videoTime=146¶ms.connItem=96a03dbef3f2c98bf5706cadfed8ee5c&_t=1685429259660",
           "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9",
           "Cookie": "p_h5_u=DDB10D57-0CE9-4EB6-92E0-47DF0C457B9B; selectedStreamLevel=SD; JSESSIONID=FC1C6CE51916502880EF602F5A69803A; _abfpc=14f9638c75a8848d313c54d3305003f80957580b_2.0; cna=f97a6f8190941c186e53e1fcf4cfa213; _uid=0fb67b7a-d764-46b4-b139-2bc02b37c14c; ssxmod_itna=QuDQefODkFY5GHD8D2DEdDtbWzapDmh4x3dM4GNbYDZDiqAPGhDC43F3LD3jYerhQDUoa0xHWjYp5oLWI8Y4vPb2u4GLDmKDyKeReeDxaq0rD74irDDxD3Db+dDSDWKD9D0RSBc6yKGWDmR8DWPDYxDrLaKDRxi7DDyd8x07DQy8YfPwnrECqGYPWjKD9OoDsh0EPjKmAf8xShYA+K73px0kB40O9ryzCroDUBKsyP7NtP+ei0TYAG03qirKtY2xsD2DY76edYWYYo+iFkZWHnqSPDDWeclP4D==; ssxmod_itna2=QuDQefODkFY5GHD8D2DEdDtbWzapDmh4x3dqA=WebD/FA4xFoQwbIPEPBKgxSx6UaDviOyAmEP2kt4OlIbIRW+WIqAWHzWd2O7v4ILRsbU8C9U6umbMjajuQM+BN1yI5jUFLa1wZK9iLLVQ+EP93fjlwE9Ur=BQn51Ib6E0iRiilbe63e1DAphtSuFeaK+WSnW=1K+04WHc3FWvp+kD1U4Q=KOD=ww46vCNqnhr79PlP7arFnH=cO5IcQivK9fvFaGPcjIZpm+LKwmxHMAxX5avtHm29H=v1BitvB7=qF9EHd9MZu1E0BWIbK2NYKP92qGPu39nUp6WKgWPg45j4xTUFLi9Pph8/a5dISmvQKYXUhRGpYoBQeP0UYDo+AeeP+ODNu0AgOCFtawRj9OBFXW+NP3ND53rxDKkHD7=DYFxeD===; token=32c881a8-4b88-4202-b9f0-35a59d50524a; aliyungf_tc=c67d4212cc56c025b36d0a849cd0101d8ce69285bb093ed9fd3e87c9e1731fd0; UNTYXLCOOKIE=\"dXNlci5pY3ZlLmNvbS5jbnx8YWIwZjNhZjlkODVjMjJjYjUzZGUxNTBmYmI5ZTA2ZjN8fDE5MDEzMDAwODl8fHpoemo=\"; rest_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbklkIjoiMTkwMTMwMDA4OSIsInNpdGVDb2RlIjoiemh6aiIsInVzZXJfbmFtZSI6IjE5MDEzMDAwODkiLCJwaG90byI6bnVsbCwic3VJZCI6Inl3dDhhc21yb3F2b2J3ajBydnUxdmciLCJhdXRob3JpdGllcyI6WyJST0xFX1NUVURFTlQiXSwiY2xpZW50X2lkIjoiMjEwODE4NzcxOCIsInRydWVOYW1lIjoi5p2o6ZSLIiwic3VkSWQiOiJ5d3Q4YXNtcm9xdm9id2owcnZ1MXZnIiwicm9sZUNvZGUiOiIwIiwic2NvcGUiOlsiYWxsIl0sInJvbGVOYW1lIjoi5a2m55SfIiwiZXhwIjoxNjg2NjI2ODU3LCJqdGkiOiJiOGU1N2RmYS1jYTA1LTQ3ZDYtYTEzYi1mYjFiMDAwYWZiYzEifQ.CSMYjE7Wftud9dy5TDvySPsqEnTW3LwSNjolc9oL8XVS5u_bgPGPvllh3epRiT8IrHQhDH_rw11DIJaxAmFhIHit0C550iC9s-sUjLsqik66DV2FmUtap9DvbPLRB731ynXO1Hi4f91RVc4qYb8mlJ_Gx3mqYPTkYwgx_jbpsMbYTehqIv0rKlCiIVDRiEy8GopaJgIWeDJjCtFZlj3bgG0PpnQKynCAZkmXbkCfx5l28pduSkIij0_LRcE9WR1i8ZiDN8-__TAgpUesFqE89DZBzcdPfygdlVb3EBug6bLpDbEIAuYpOTgOZBcgGJsfOGUl1HMHIeLMt56A5fVN2g; learning-course=ywt8asmroqvobwj0rvu1vg_149285800359ff8b7b1e19542c0f5a59___; jwplayer.volume=50; acw_tc=2f6fc11416854288375983897e925dd1848660bacf2c071751a9bf5fee5b42; SERVERID=4df0a646369c4a07c6f8144ee85f6da2|1685429259|1685417257"}

if __name__ == '__main__':
    new_zjy_api = NewZjyApi()
    new_zjy_api.set_headers(headers)

    data = {
        "data": "info",
        "page.searchItem.queryId": "getStuCourseInfoById",
        "page.searchItem.keyname": "",
        "page.curPage": 1,
        "page.pageSize": 5

    }

    # new_zjy_api.get_by_sql_code(data)
    new_zjy_api.get_course_list()
    new_zjy_api.start()
    print("结束")
