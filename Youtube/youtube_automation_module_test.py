from youtube import *


def likeandsub():
	'''can only call after function(scrole_page_and_video_links) 
	like and subcribe all videos present '''
	os.system("cls")
	for i in range(len(url)):
		print()
		print('video no :',i+1)
		print('trying ', url[i]  )
		time.sleep(2)

		you.like(url[i])
		you.subscribe()	
		print()
		time.sleep(2)

		os.system('cls')


you = youtube('rishabhjainfinal','1Rishabh@jain')
you.geturl()
you.signing()


print("start process")
print()
you.geturl('https://www.youtube.com/channel/UCqwUrj10mAEsqezcItqvwEw/videos')
url=you.scrole_page_and_video_links()
likeandsub()

you.close_end()
# for i in url:
# 	you.like(i)
# 	you.subscribe()
# you.close_end()

