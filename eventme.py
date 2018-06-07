import requests
from bs4 import BeautifulSoup
import re
from sgw.core import SendGrid


class EventMe:
    def __init__(self, base_url, search_url, sg_api, sg_from, sg_from_name):
        self.base_url = base_url
        self.search_url = search_url
        self.email = SendGrid(sg_api, sg_from, sg_from_name)

    def scrap(self, date1, date2):
        date1, date2 = date1.strftime("%d/%m/%Y"), date2.strftime("%d/%m/%Y")
        if date1 == date2:
            self.title = f"Eventos en Tenerife ({date1})"
        else:
            self.title = f"Eventos en Tenerife ({date1} - {date2})"
        params = {
            "field_fecha_value[min][date]": date1,
            "field_fecha_value[max][date]": date2
        }
        result = requests.get(url=self.search_url, params=params)
        # remove invalid tag </br> since it leads wrong beautiful soup
        content = result.text.replace("</br>", "")

        self.events = []
        soup = BeautifulSoup(content, "html.parser")
        ul = soup.find("ul", "list-small-post")
        for container in ul.find_all("div", "small-post"):
            img = container.find("div", "thumb").a.img["src"]
            post = container.find("div", "post-c-wrap")
            url = self.base_url + post.h4.a["href"]
            title = re.sub(r"[‘'’]", "", post.h4.a.string).strip()
            meta = post.find("div", "meta")
            category, venue = meta.find_all("div", "post-category")
            if category.a:
                category = category.a.string.upper()
            else:
                category = "SIN CATEGORÍA"
            venue = venue.a.string
            date = meta.find("div", "post-date").span.string
            self.events.append({
                "img": img,
                "url": url,
                "title": title,
                "category": category,
                "venue": venue,
                "date": date
            })

    def __build_msg(self):
        msg = ["<table>"]
        for e in self.events:
            msg.append(f"""
                <tr>
                    <td>
                        <a href="{e['url']}"><img src="{e['img']}"></a>
                    </td>
                    <td>
                        <b>{e['title']}</b><br>
                        {e['category']}<br>
                        {e['url']}<br>
                        {e['date']}<br>
                        {e['venue']}
                    </td>
                </tr>
            """)
        msg.append("</table>")
        self.msg = "".join(msg)

    def send(self, *args):
        self.__build_msg()
        for addr in args:
            self.email.send(
                to=addr,
                subject=self.title,
                msg=self.msg,
                html=True
            )
