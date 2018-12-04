import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#處理需要回答18歲以上的問題
def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})  
    return response


board = input("請輸入看板網址(直接按enter預設NBA版): ")
if not board:
	board = 'https://www.ptt.cc/bbs/NBA/index.html'
num = int(input("輸入想要抓取的頁數: "))
titles = []
authors = []
dates = []
links = []
# url = 'https://www.ptt.cc/bbs/NBA/index.html'
url = board
for i in range(num):
	# res = requests.get(url)
	res = fetch(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	paging = soup.select('div.btn-group-paging a')
	next_page = 'https://www.ptt.cc'+paging[1]['href']
	url = next_page

	#標題
	posts = soup.select('div.title')
	for post in posts:
		try:
			titles.append(post.contents[1].text)
		except:
			titles.append(np.nan)

	#作者
	all_author=soup.select('div.author')
	for author in all_author:
		authors.append(author.text)
	#日期
	all_date = soup.select('div.date')
	for date in all_date:
		dates.append(date.text)
	#內文太過龐大想改成連結，不過只要文章被刪除沒有a tag就會出錯，因此沒有放
	all_link = soup.select('div.title a')
	for link in all_link:
		try:
			links.append('https://www.ptt.cc/bbs/'+link['href'])
		except:
			links.append(np.nan)

	ptt_dic = {"title": titles,
				"author": authors,
				"date": dates}
	ptt_df = pd.DataFrame(ptt_dic)

#看板名稱
board_name = soup.select('a.board')[0].text
print(board_name)
print(ptt_df)






