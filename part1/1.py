#Counting
# Given a list of urls, print out the top 3 frequent filenames.
from collections import Counter
def counting(urls):
	l = []
	for i in urls:
		url = i.split('/')[-1:][0]
		l.append(url)
	dic = {}
	for i in l:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1
	#本來想用list做排序後取值，但用模塊比較簡單點
	# topthree = sorted(dic.values())[-3:]
	#利用Counter module處理dic中的數字
	c = Counter(dic)
	for k, v in c.most_common(3):
		print(k,v)




urls = urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

counting(urls)

