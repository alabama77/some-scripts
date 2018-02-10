import re
import httplib2
import urllib.request
from itertools import groupby


print("________________________________________________________________|")
print("                                                             |\n")
print("Скачать все изображения, webm, mp4, gif из треда с сайта 2ch.com")
print("                                                             |\n")
print("________________________________________________________________|")

print("Скопируйте сюда ссылку на тред:")

url = input("Ссылка: ")
url.strip()
if "https://2ch.hk" not in url:
	print("Неправильная ссылка на тред приведёт к ошибке")
print("Опции:")
print("\n")
print("Выбирите, что хотите скачать:")
print("1 - все изображения, 2 - все webm, 3 - все mp4, 4 - все gif, 5 - скачать всё")
hui = int(input("Вводи ключ:"))

#url = 'https://2ch.hk/pr/res/1134500.html'

with urllib.request.urlopen(url) as response:
	content = response.read().decode("utf-8")
images = re.findall('a .*?href="(.*?/src/.*?)"', content)
images = [elem for elem, _ in groupby(images)]
def all_images():
	counter = 0
	for image in images:
		if (image.endswith(".jpg")) or (image.endswith(".jpeg")) or (image.endswith(".png")):
			counter += 1
			urllib.request.urlretrieve("https://2ch.hk" + image, "Картинка с двача" + str(counter))
			print("Скачивание... " + image)
def all_webms():
	counter = 0
	for webm in images:
		if webm.endswith(".webm"):
			counter += 1
			urllib.request.urlretrieve("https://2ch.hk" + webm, "Webm с двача" + str(counter))
			print("Скачивание... " + webm)
def all_mp4():
	counter = 0
	for mp4 in images:
		if mp4.endswith(".mp4"):
			counter += 1
			urllib.request.urlretrieve("https://2ch.hk" + mp4, "Mp4 с двача" + str(counter))
			print("Скачивание... " + mp4)
def all_gif():
	counter = 0
	for gif in images:
		if gif.endswith(".gif"):
			counter += 1
			urllib.request.urlretrieve("https://2ch.hk" + gif, "Gif с двача" + str(counter))
			print("Скачивание... " + gif)

if hui == 1:
	all_images()
elif hui == 2:
	all_webms()
elif hui == 3:
	all_mp4()
elif hui == 4:
	all_gif()
elif hui == 5:
	all_images()
	all_webms()
	all_gif()
	all_mp4()
else:
	print("Вы ввели не то")