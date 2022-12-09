import bs4

from .parser import Parser
import requests
import json
from bs4 import BeautifulSoup


class WantedParser(Parser):
    def __init__(self, url: str) -> None:
        self.url = url

    def _parse(self) -> str:
        return self.get_row_data().__str__()

    def get_row_data(self) -> dict:
        list_id = self.get_list_of_id()
        list_of_data = {}
        for id in list_id:
            list_of_data[id] = self.get_info_of(str(id))
        return list_of_data

    def get_list_of_id(self) -> list:
        offset = 0
        limit = 2
        list_of_id = []
        flag = True
        # while (flag):
        html = requests.get(
            self.url + f"/api/v4/jobs?1670145066301&country=kr&tag_type_ids=518&job_sort=company.response_rate_order&locations=all&years=-1&limit={limit}&offset={offset}")
        soup = BeautifulSoup(html.text, "html.parser")
        list_jo = json.loads(soup.text)
        if list_jo["data"] is None:
            flag = False
        else:
            for i in list_jo["data"]:
                list_of_id.append(i["id"])
            offset += limit
        return list_of_id

    def get_info_of(self, id: str) -> dict:
        target_data = ["jd", "company_name", "logo_img", "address", "due_time", "requirements", "main_tasks"]
        url = self.url + f"/wd/{id}"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        instance_of_data = soup.find("script", type="application/json")
        instance_of_json = json.loads(instance_of_data.contents[0])['props']['pageProps']['head'][id]
        to_delete_list = []
        for key in instance_of_json:
            if not key in target_data:
                to_delete_list.append(key)
        for key in to_delete_list:
            del instance_of_json[key]
        instance_of_json["origin_url"] = url
        return instance_of_json
