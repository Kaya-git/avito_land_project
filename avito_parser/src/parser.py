import undetected_chromedriver as uc
from typing import Protocol


class Parser(Protocol):

    def __init__(
        self,
        url: str,
    ):
        self.url = url
        self.driver = uc.Chrome(browser_executable_path="/usr/lib/brave-browser/brave-browser")

    def make_query(self):
        self.driver.get(self.url)

    # def scrap_adv_links(self, html):
    #     with open(f"{html}", mode="r") as f:
    #         lxml_file = f.read()

    #     soup = BeautifulSoup(lxml_file, "lxml")

    #     links = []

    #     for link in soup.find_all("a"):

    #         links.append(link.get("href"))

    #     return links


class AvitoParser(Parser):
    ...
