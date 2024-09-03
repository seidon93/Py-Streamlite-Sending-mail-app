import requests
from Send_mail import send_email
API_KEY = "662c2076bb06462c9d9018f5e8ef6e4e"

topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}"
       "sortBy=publishedAt&"
       f"apiKey={API_KEY}&"
       "language=en")

response = requests.get(url)
content = response.json()

email_body = ""

for i in content['articles'][0:20]:
    title = i['title'] if i['title'] is not None else ""
    description = i['description'] if i['description'] is not None else ""

    if title or description:
        email_body = ("Subject: Today's news" + "\n"
                      + title + "\n"
                      + description + "\n"
                      + i["url"] + 2 * "\n")

email_body = email_body.encode("utf-8")
send_email(message=email_body)

