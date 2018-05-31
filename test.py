import requests
import re
import json
import datetime
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
r = requests.get('http://www.taiwanlottery.com.tw/lotto/BINGOBINGO/drawing.aspx')

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')
  """
  datas = soup.find_all("td",class_=re.compile("tdA_[34]"))# 把奇數行的資料抓出來
  #even_datas = soup.find_all("td",class_="tdA_3")# 把偶數行的資料抓出來
  i=1
  for d in datas:
    if i == 1:    
      print("期別 :" + d.text)
    elif i == 2:
      print("獎號 :" + d.text) 
    elif i == 3:
      print("超級獎號 :" + d.text)
    elif i == 4:
      print("猜大小 :" + d.text)
    elif i == 5:
      print("猜單雙 :" + d.text)
      i=0
    i+=1
  """
  datas = soup.select('table.tableFull > tr > td > table > tr td[class^=tdA]')
  #print(datas)
  result_list = [] 
  i=1
  tmp_list = []
  for d in datas:
    tmp_list.append(d.text)
    if i == 5:
      result_list.append(tmp_list)
      tmp_list = []
      i=0
    i+=1
  json_test = json.dumps(result_list)  
  """
  with open('lottery_data/'+datetime.datetime.now().strftime("%Y-%m-%d")+'_data.json', 'w') as file:
    file.write(json_test)
    file.close()
  """  
  print(json_test)