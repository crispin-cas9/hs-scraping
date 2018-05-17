# yeet

import re
import urllib.request

def strippage(pg):
	page = urllib.request.urlopen('https://www.homestuck.com/story/' + str(pg)).read().decode('utf-8')
	striplist = re.findall('<p.+?>(.+?)</p>', page) # capture group of anything within paragraph tags

	stripped = [re.sub('(\\r)', ' ', section) for section in striplist]
	stripped = [re.sub('<br>', '\n', section) for section in stripped]
	stripped = [re.sub('(<.+?>)', ' ', section) for section in stripped]
	stripped = [re.sub('&quot;', '"', section) for section in stripped]
	stripped = [re.sub('&lt;', '<', section) for section in stripped]
	stripped = [re.sub('&gt;', '>', section) for section in stripped]
	
	if len(stripped) == 1:
		return stripped[0]
	else:
		return "\n"

skip = [2399, 3038, 3088, 6370, 7902, 7903, 7904]

text = " "
count = 8000
while count < 8086:
	if count not in skip:
		text = text + strippage(count) + '\n'
	if count % 500 == 0:
		print('.')
	count = count + 1

file = open("homestuck2.txt", "w")
file.write(text)
