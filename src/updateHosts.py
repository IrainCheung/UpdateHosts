import sys
url='https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts'
try:
	import requests
	resp=requests.get(url)
	content= resp.content
except:
	import urllib2
	resp=urllib2.urlopen(url)
	content=resp.read()

with open(sys.path[0]+'\\addition.txt','r') as f:
    content=f.read()+content

with open(r'C:\WINDOWS\System32\drivers\etc\HOSTS','w') as f:
    f.write(content)

print 'update completed'
