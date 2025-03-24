from atproto import Client
from dotenv import load_dotenv
load_dotenv()
import os
import datetime
import schedule,time,datetime
import requests
import urllib.parse
times = datetime.datetime.now()
times_jpn = times.strftime('%Y年%m月%d日')
url = "https://ja.wikipedia.org/w/api.php"
params = {
    "format": "json",
    "action": "query",
    "list": "random",
    "rnnamespace": 0,
    "rnlimit": 1
}
# 投稿関数
def post():
    response = requests.get(url, params=params)
    data = response.json()
    title = data.get("query").get("random")[0].get("title")
    encoded_title = urllib.parse.quote(title)
    post_text = f"今日のwiki\nhttps://ja.wikipedia.org/wiki/{encoded_title}"
    client.send_post(post_text)
    print("投稿完了:" + times_jpn)  
# アカウントID
account = "wiki-bot.bsky.social"
# さきほど生成したパスワード
pwd = os.getenv("BSKY_API")
client = Client(base_url='https://bsky.social')
client.login(account, pwd)
print("ログイン完了", times_jpn,"\n","Display_name:",client.me.display_name)
schedule.every().day.at("16:00").do(post)
while True:
    schedule.run_pending()
    time.sleep(1)

