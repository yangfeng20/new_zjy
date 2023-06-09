import requests
from logger import Logger
import init_mooc


class NewZjyApi:
    """新职教云的请求api封装"""

    __get_by_sql_code_url = "https://user.icve.com.cn/learning/u/userDefinedSql/getBySqlCode.json"

    def __init__(self):
        self.headers = {}
        self.session = requests.session()
        self.logger = Logger.log()
        self.logger.log_self_open = self.logger.log_self_open.DEBUG
        self.course_list = []

    def set_headers(self, headers: dict):
        self.headers = headers

    def get_by_sql_code(self, form_data: dict):
        resp = self.session.post(self.__get_by_sql_code_url, data=form_data, headers=self.headers)
        self.logger.debug("sql_code响应数据：" + resp.text)
        resp_json = resp.json()
        return resp_json

    def get_course_list(self):
        course_list_param = {
            "data": "info",
            "page.searchItem.queryId": "getStuCourseInfoById",
            "page.searchItem.keyname": "",
            "page.curPage": 1,
            "page.pageSize": 10

        }
        course_list_resp = self.get_by_sql_code(course_list_param)
        course_list = course_list_resp.get("page", {}).get("items", {})[0].get("info", [])
        if not course_list:
            self.logger.debug(course_list_resp)
            raise Exception("未查询到课程列表")
        for course_info in course_list:
            course_name = course_info['ext1']
            course_teacher = course_info['ext4']
            course_id = course_info['ext9']

            course = {
                "course_id": course_id,
                "course_name": course_name,
                "course_teacher": course_teacher,
            }
            self.course_list.append(course)

    def start(self):
        init_mooc.HEADERS = self.headers
        course = self.course_list[self.select_course()]
        self.logger.info("正在执行: ", course.get('course_name'), course.get('course_teacher'))
        init_mooc.start(self.session, course.get('course_id'))

    def select_course(self):
        if not self.course_list:
            raise Exception("课程列表为空")
        print("请通过课程序号来选择需要刷课的课程")
        for index, course in enumerate(self.course_list):
            print(index, course.get("course_name", " "), course.get("course_teacher", " "))
        index = -1
        try:
            index = int(input("请输入课程对于序号：\n"))
        except ValueError as e:
            print("无效课程序号", e)
            exit(-1)
        return index
