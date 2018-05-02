import requests
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
r = requests.get('http://www.taiwanlottery.com.tw/lotto/BINGOBINGO/drawing.aspx')

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  stories = soup.find_all("td",class_="tdA_4")
  print(stories)
  #for s in stories:
    # 新聞標題
    #print("staff: " + s.text)
