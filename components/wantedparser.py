from .parser import Parser
import requests
import json
from bs4 import BeautifulSoup


class WantedParser(Parser):
    def __init__(self, url: str) -> None:
        self.url = url

    def _parse(self) -> str:
        html = requests.get(self.url)
        soup = BeautifulSoup(html.text, "html.parser")
        # jo = json.loads(soup.find("script"))
        return soup.find("script").text
