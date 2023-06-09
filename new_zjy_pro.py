import json
from new_zjy_main import NewZjyApi

HEADERS = {}


def add_cookie_auth():
    header_str = input("请输入浏览器中登录的header信息: ")
    global HEADERS
    HEADERS = json.loads(header_str)


if __name__ == '__main__':
    new_zjy_api = NewZjyApi()
    add_cookie_auth()
    new_zjy_api.set_headers(HEADERS)
    new_zjy_api.get_course_list()
    new_zjy_api.start()
    print("结束")
