'''
/* We'll scrap a web, get some image, download these images, 
/* and store them in localhost
'''

import requests as req
from bs4 import BeautifulSoup
import urllib


def main():
	protocol = 'https:'
	URL = protocol + '//xkcd.com'
	for i in range(1,6):
		resp = req.get(URL+'/' + str(i))
		soup = BeautifulSoup(resp.content, 'html.parser')
		img_container = soup.find(id='comic')
		img_url = img_container.find('img')['src']
		img_name= img_url.split('/')[-1]
		print('Downloading image {} ...'.format(img_name))
		urllib.request.urlretrieve(protocol+img_url, img_name)


if __name__ == '__main__':
	main()