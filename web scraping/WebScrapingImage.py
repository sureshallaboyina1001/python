import requests
import bs4

result=requests.get("https://en.wikipedia.org/wiki/Supercomputer")
soup=bs4.BeautifulSoup(result.text,'lxml')
img_info=soup.select(".thumbimage")

supercomp=img_info[0]
supercomp['src']
image_link="http:"+supercomp['src']

supercompimg=requests.get(image_link,'lxml')
f=open("new_image.jpg",'wb')
f.write(supercompimg.content)
f.close()




