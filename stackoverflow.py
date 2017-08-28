import requests
from lxml import etree

cookies = {' __gads': 'ID',
 ' _ga': 'GA1.2.605684715.1500135985',
 ' _gat': '1',
 ' _gid': 'GA1.2.253468492.1502748115',
 ' cc': '41b6abba703744b18c5f4335dcce104c',
 'UID': '10B23a76a15612734987f881500130683',
 'UIDR': '1500130683',
 '__gads': 'ID=1697b9fd8ae2e0bb:T=1502289496:S=ALNI_MaICrds7tdxYEBTDYmq14JOLcdV1g',
 '__qca': 'P0-2096890299-1500135986501',
 '_ga': 'GA1.2.605684715.1500135985',
 '_gat_pageData': '1',
 '_gid': 'GA1.2.253468492.1502748115',
 'csouser': 't=er8miBgzkEGZ&s=PqzRpu4GK0et',
 'mc': '596a4233-b2247-bf201-5653d',
 'id':'2296f96fd84900bd||t=1500126269|et=730|cs=002213fd486e5975cd1abd1bd0',
 'prov': 'ec21a04c-8684-140b-84b2-cf82d03afe72'}


def notlogged():
 	r = requests.get('https://stackoverflow.com/users/2563469/rhea')
 	h = etree.HTML(r.content)
 	l = h.xpath("//div[@id='user-card']//ul[contains(@class,'list-unstyled')]/li[5]/span/text()")
 	if len(l):
 		print "logged in since", l[0]
 	

def logged():
	with open('acct.txt') as f:
		acct = f.readline()
	cookies['acct'] = acct
	print acct
 	r = requests.get('https://stackoverflow.com/users/2563469/rhea', cookies= cookies)
 	h = etree.HTML(r.content)
 	l = h.xpath("//aside[contains(@class, 'js-highlight-box-badges')]//span[contains(@class,'-count')]/text()")
	acct = r.cookies.get('acct')
	if acct:
		with open('acct.txt',mode='w') as f:
 			f.write(r.cookies.get('acct'))
 	if not len(l):
 		print "not logged in"
 	else:
 		print l[0]
 		notlogged()
logged()
