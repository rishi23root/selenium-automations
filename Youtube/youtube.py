from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class youtube:

	"""This module is use for automation of youtube threw sekenium webdriver 
		this module is only for youtube
		for this module you need latest webdriver in same directory as progarm
		just check you browser version
		if you don't get the driver then link are;'
		[crome = https://chromedriver.chromium.org/downloads] 
		[Edge = https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ ]  """                                 
	
	def __init__(self,email,password,browser = 'Edge' ):

		'''take userid, password,browser(Crome or Edge) and url of youtube although this is strictly for only youtube '''
		print("running ")

		self.user = email
		
		self.password = password 
		if browser == 'Chrome' :
			self.driver = webdriver.Chrome('D:\selenium automation\youtube automation\chromedriver.exe')
			print("using [ crome ] browser")
		else :
			try:
				self.driver = webdriver.Edge('D:\selenium automation\youtube automation\edge_old.exe')#msedgedriver.exe') 
			except:
				self.driver = webdriver.Edge('D:\selenium automation\youtube automation\msedgedriver.exe') 
		
			print("using [ Edge ]  browser")
		self.driver.maximize_window()
		print("initialising the process ")


	def geturl(self,url='https://www.youtube.com/'):
		'''open provided url and eleminate any notifications box on window '''
		driver = self.driver
		print("opening url",url)
		driver.get(url)
		# print("url open")

		time.sleep(2)
		
		try:
			driver.find_element_by_xpath("//*[@aria-label='Dismiss']").click()
			print("trying eleminating notification box # ") 
			print("done")
			time.sleep(5)

		except :
			pass


	def signing(self):

		'''signing into youtube by pre given values of email and password 
		but can only be used after geturl to get login option '''
		driver = self.driver
		
		print("signing")
		time.sleep(5)

		signi = '''//a[@href ='https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620']'''
		driver.find_element_by_xpath(signi).click()
		print("clicked on signi")
		time.sleep(3)
		
		try:
			email = driver.find_element_by_xpath("//input[@id = 'identifierId']").send_keys(self.user)
			nextB = driver.find_element_by_xpath("//*[text()= 'Next']")
			nextB.click()	

		except:
			email = driver.find_element_by_xpath("//input[@id = 'identifierId']").send_keys(self.user)
			nextB = driver.find_element_by_xpath("//*[text()= 'Next']")
			nextB.click()	
			

		time.sleep(5)

		print("trying given password ")
		passw = driver.find_element_by_xpath("//input[@type= 'password']").send_keys(self.password)
		try:				
			driver.find_element_by_xpath("//*[text()= 'Next']").click()	
			
			time.sleep(5)
		
		except :
			print()
			print("error founded trying again")

			time.sleep(5)

			#print("trying given password ")
			#assw = driver.find_element_by_xpath("//input[@type= 'password']").send_keys(self.password)
			driver.find_element_by_xpath("//*[text()= 'Next']").click()	
			
			time.sleep(5)

		global result		
		try:
			try:
				result ='@@@@@@@@@@\n'+driver.find_element_by_xpath("//div[@jsname='B34EJ']/span").text+'\n@@@@@@@@@@@@@@@@@@@\n error found \n'
				print(result)
				driver.close()
			
			except :
				if driver.current_url=='''https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward''':
					result ='error founded \nyour browser may be secure'
					print(result)					
					driver.close()	
			finally:
				return result
		except :
			result="login sucessfully :-:"
			print(result)
			return result
		
		time.sleep(3)

		try:
			driver.find_element_by_xpath("//*[@aria-label='Dismiss']").click()
			print("trying eleminating notification box # ") 
			print("done")

		except :
			pass
	


	def find_video(self):

		'''only TO find any video or chanal by name or url by input method later '''
		driver = self.driver
		que = input("have any\n  1.[name] or\n 2.[url] to find write 1/2 :")

		if que == 1:
			find = input("write name of [video] or [chanal] :_: :")
			driver.get(f"https://www.youtube.com/results?search_query={find}")

		else:
			find = input("enter url that you have")
			driver.get(find)


	def like(self,url):

		'''like video by video url   '''
		driver = self.driver
		time.sleep(2)

		print('now opening ',url)
		driver.get(url)
		time.sleep(3)
		p="//div[@id='top-level-buttons']//a//yt-formatted-string[@id='text'][@aria-label]"
		a=driver.find_element_by_xpath(p).get_attribute('aria-label')
		a= a.split(' ')[0]
		print(f"there are total {a} likes already")

		try:
			like = driver.find_element_by_xpath(f'''//div[@id="top-level-buttons"]//a//button[@aria-label="like this video along with {a} other people"]''')
			b = like.get_attribute('aria-pressed')
			  #true= liked.false unliked
			if b == 'true' :
				print("video already liked")
			else :
				print("try to like")
				like.click()
				print("video liked @@@")

		except :
			print("not working\n retry loging again ")


	def subscribe(self):

		'''subscribe the video on calling 
		limitatiion : video should be already open #
		good to use in loop'''

		driver = self.driver
		time.sleep(1)

		try : 
			subs = driver.find_element_by_xpath("//div[@id='subscribe-button' and @class='style-scope ytd-video-secondary-info-renderer']//paper-button/yt-formatted-string")
			print(subs.text)

			if subs.text != 'SUBSCRIBED' :
				print("NOT Subscribe yet trying :: ")
				subs.click()
				sub = "Subscribed  @@@"

			else :
				sub = "already subscribed"

			return sub

		except TypeError:
			print("element not founded ")

	def commenting(self,comment):
		''' comment on video 
		limitation url shoud alredy open '''

		driver = self.driver
		time.sleep(2)
		
		# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)"
		# print(" scrolling ")

		try:
				
			for i in range(1):
				driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath('//div[@id="continuations"and @class="style-scope ytd-item-section-renderer"]'))
				print('scrolling ',1)
			time.sleep(2)

			try:
				com = driver.find_element_by_xpath('//div[@id="placeholder-area"]')		
				com.click()
				com.send_keys(comment)

			except:
				com = driver.find_element_by_xpath("//div[@id='contenteditable-root']")
				com.click()		
				com.send_keys(comment)
			

			time.sleep(1)

			send =driver.find_element_by_xpath("//paper-button[@aria-label = 'Comment']")
			send.click()

		# print('done')
		except:
			print("unable to comment")

		


	def scrole_page_and_video_links(self):

		'''get all video info and store in a list variable and make it global
		page shoud be already open '''

		global url

		driver=self.driver
		time.sleep(5)

		for i in range(5):
			driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath('//div[@id="continuations"and @class="style-scope ytd-item-section-renderer"]'))
			# print("scrolling into window wait <> ")
			time.sleep(2)
			# print()

		url = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//a[@id='thumbnail'][@href]")]
		print(f"total {len(url)} videos founded @@")		

		return url


	def close_end(self):

		''' just to close driver at the end '''
		driver = self.driver

		time.sleep(5)

		driver.close()




