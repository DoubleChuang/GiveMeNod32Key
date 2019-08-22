import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
print("START")
req = Request('https://nodkey.xyz/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
os.system("cls")
soup = BeautifulSoup(webpage, 'html5lib')
divs = soup.find_all('div', 'main')
print("=======NOD32 Key=======")
for d in divs:
	key = d.find_all('p')
	for i in key[1:]:
		print(i.text.strip())
print("=======================")
os.system("pause")
