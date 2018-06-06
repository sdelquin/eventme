import config
import requests
from bs4 import BeautifulSoup
import re
from sgw.core import SendGrid

date1 = "07/06/2018"
date2 = "09/06/2018"


params = {
    "field_fecha_value[min][date]": date1,
    "field_fecha_value[max][date]": date2
}
result = requests.get(url=config.SEARCH_URL, params=params)
# remove invalid tag </br> since it leads wrong beautiful soup
content = result.text.replace("</br>", "")

msg = ["<table>"]
soup = BeautifulSoup(content, "html.parser")
for container in soup.find_all("div", "small-post"):
    img = container.find("div", "thumb").a.img["src"]
    post = container.find("div", "post-c-wrap")
    url = config.BASE_URL + post.h4.a["href"]
    title = re.sub(r"[‘'’]", "", post.h4.a.string).strip()
    meta = post.find("div", "meta")
    category, venue = meta.find_all("div", "post-category")
    if category.a:
        category = category.a.string.upper()
    else:
        category = "SIN CATEGORÍA"
    venue = venue.a.string
    date = meta.find("div", "post-date").span.string

    msg.append(f"""
<tr>
    <td>
        <a href="{url}"><img src="{img}"></a>
    </td>
    <td>
        <b>{title}</b><br>
        {category}<br>
        {url}<br>
        {date}<br>
        {venue}
    </td>
</tr>
    """)
msg.append("</table>")

msg = "".join(msg)

email = SendGrid(
    config.SENDGRID["API_KEY"],
    config.SENDGRID["FROM_EMAIL"],
    config.SENDGRID["FROM_NAME"]
)
