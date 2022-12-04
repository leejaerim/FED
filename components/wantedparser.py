import bs4

from .parser import Parser
import requests
import json
from bs4 import BeautifulSoup


class WantedParser(Parser):
    def __init__(self, url: str) -> None:
        self.url = url

    def _parse(self) -> str:
        list_id = self.get_list_of_id()
        return str(list_id)
    def get_list_of_id(self)->list:
        offset = 0
        limit = 100
        res = []
        flag = True
        while (flag):
            html = requests.get(self.url + f"&limit=100&offset={offset}")
            print(self.url + f"&limit=100&offset={offset}")
            soup = BeautifulSoup(html.text, "html.parser")
            jo = json.loads(soup.text)
            if jo["data"] is None:
                flag = False
            else:
                for i in jo["data"]:
                    res.append(i["id"])
                offset += limit
        return res



