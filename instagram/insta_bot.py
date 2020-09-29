from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time
import os
import json

class module:
	def __init__(self,user,password):
		self.user = user
		self.password= password
		if len(self.password) < 6 :
			raise Exception('password must be of greater length')

		print("setup drivers",end='')
		self.driver = webdriver.Chrome('chromedriver.exe')
		print(" ..successful")

	def open_insta(self,url ="https://www.instagram.com/accounts/login/"):
		print(f"opening {url}")
		self.driver.get(url)
		# time.sleep(1.5)

	def login(self):
		driver = self.driver
		print("finding elements")

		username_input_xpath = "//input[@name = 'username']"
		password_input_xpath = "//input[@name = 'password']"
		button_xpath = "//button[@class='sqdOP  L3NKy   y3zKF     ']"
		self.execute_when_element_on_screen(driver,username_input_xpath)

		user = driver.find_element_by_xpath(username_input_xpath)	
		password = driver.find_element_by_xpath(password_input_xpath)	
		login = driver.find_element_by_xpath(button_xpath)

		user.send_keys(self.user)
		password.send_keys(self.password)
		login.click()

		# check if login confirm
		try:
			unsucessful_login = '//*[@id="slfErrorAlert"]'
			self.execute_when_element_on_screen(driver,unsucessful_login,time=2)
			print()
			print('wrong username or password')
			print()
			driver.close()
			return False
			# raise Exception('wrong username or password') /cant use it here because raise excetion will cancel out the try statement

		except :
			print('login successful....')
		
		# elemenate save info popup
		try:
			save_login_popup = '//*[@id="react-root"]/section/main/div/div/div/div/button'
			self.execute_when_element_on_screen(driver,save_login_popup)	
			driver.find_element_by_xpath(save_login_popup).click()
			print("save-info box eleminated")
	
		except :
			pass

		# elemenate turn notification on popup
		try :
			notification_popup_xpath = '/html/body/div[4]/div/div/div/div[3]/button[2]'
			self.execute_when_element_on_screen(driver,notification_popup_xpath) 
			driver.find_element_by_xpath(notification_popup_xpath).click()
			print("notification box eleminated")
		except :
			pass 

		return True
	
	def profile(self):
		driver = self.driver
		print("opening user profile")
		driver.get(f'https://www.instagram.com/{self.user}/')

	def find_person(self,persons_id):
		#name should be full and correct
		driver = self.driver
		print("finding person",end=' ')
		driver.get("https://www.instagram.com/"+persons_id+"/")
		sorry_path = "//*[contains(text(),'Sorry, this page ')]"
		try :
			# self.execute_when_element_on_screen(driver,setting_xpath,time=1)
			driver.find_element_by_xpath(sorry_path)			
			print('\nunable to found the persond wrong username \n')
			return False

		except :
			print(persons_id , 'founded')
			return True

	def countphotos(self):
		# must call after the find person
		driver = self.driver
		post_count_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span'
		self.execute_when_element_on_screen(driver,post_count_xpath)
		print("There are ",driver.find_element_by_xpath(post_count_xpath).text)
		# for i in range(1,10):
		# 	for j in range(1,4):
		# 		path = "//*[@id='react-root']/section/main/div/div[4]/article/div/div/div[{}]/div[{}]".format(i,j)
		# 		path = driver.find_element_by_css_selector("//*[@id='react-root']/section/main/div/div[4]/article/div/div/div[1]/div[1]")
		# 		path.click()        

	def like_some(self):
		'''this function will like only some of the image '''
		driver = self.driver
		try :
			post = driver.find_element_by_xpath("//span[text()=' posts']").text.replace(' posts', '')
		except :
			post = driver.find_element_by_xpath("//span[text()=' post']").text.replace(' post', '')

		try:
			post = post.replace(',','')
		except:
			pass

		if int(post) == 0 :
			print('there are no post to like or dislike')
			return

		try:
			private = driver.find_element_by_xpath('//*[@class="rkEop"]').text
		
			if private == 'This Account is Private' :
				print("\nThis account is private can't do anything\n")
		except:	
			print("account is not private woking hard to complete task")
			# taking only 10 persent of posts
			post = 10 if int(post) > 10 else int(post)
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
			photos = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//div[@class=' _2z6nI']//a")]
			count = 0
			for i in range(post) :
				i = photos[i]
				# make in same tab or new tab 
				unlike_xpath = "//*[name()='svg'][@class='_8-yf5 '][@aria-label ='Unlike']"
				like_xpath = "//*[name()='svg'][@class='_8-yf5 '][@aria-label ='Like']"
				window_xpath = '//*[@id="react-root"]/section/main/div/div/article'
				driver.get(i)
				count += 1
				self.execute_when_element_on_screen(driver,window_xpath)
				try:
					like = driver.find_element_by_xpath(like_xpath)						
					like.click()
					print(str(count).zfill(3),'photo liked url is -> ',i)
						
				except:
					driver.find_element_by_xpath(unlike_xpath)
					print(str(count).zfill(3),"photo already liked !! url -> ",i)           								
	
	def likeall(self,LIKE =True):
		driver = self.driver
		try :
			post = driver.find_element_by_xpath("//span[text()=' posts']").text.replace(' posts', '')
		except :
			post = driver.find_element_by_xpath("//span[text()=' post']").text.replace(' post', '')

		try:
			post = post.replace(',','')
		except:
			pass

		if int(post) == 0 :
			print('there are no post to like or dislike')
			return		
					
		def fun1():
			''' for post more then 40'''
			# concept here is create a list of links of all posts of persons profile then go one by one on each post   
			# create a list of all post urls 
			photos = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//div[@class=' _2z6nI']//a")]
			# scrolling into window and collecting all the post urls 
			for i in range(int(int(post)/10)+2) :
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
				time.sleep(1)
				b = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//div[@class=' _2z6nI']//a")]
				for i in b:
					if i not in photos:
						photos.append(i)

			print()
			print("Total posts found are :",(len(photos)))

			count = 0
			for i in photos :
				unlike_xpath = "//*[name()='svg'][@class='_8-yf5 '][@aria-label ='Unlike']"
				like_xpath = "//*[name()='svg'][@class='_8-yf5 '][@aria-label ='Like']"
				window_xpath = '//*[@id="react-root"]/section/main/div/div/article'
				driver.get(i)
				count += 1
				self.execute_when_element_on_screen(driver,window_xpath)
				if LIKE :
					try:
						like = driver.find_element_by_xpath(like_xpath)						
						like.click()
						print(str(count).zfill(3),'photo liked url is -> ',i)
							
					except:
						driver.find_element_by_xpath(unlike_xpath)
						print(str(count).zfill(3),"photo already liked !! url -> ",i)           								

				else :
					try :
						unlike = driver.find_element_by_xpath(unlike_xpath)
						unlike.click()
						print(str(count).zfill(3),"photo disliked !! url -> ",i) 

					except :
						driver.find_element_by_xpath(like_xpath)						
						print(str(count).zfill(3),'photo not liked url is -> ',i)
						          						 
		def fun2():
			'''run when photos are less then 40 ,this will open post in window and check if it is liked or not'''
			# concept here is to click on the post on page then do stuff after every 3 posts scrole a litte and go on again 

			# there is a little variation in code for different accounts - big or small account fix by table_num,element_variation
			table_num = 3
			try :
				self.execute_when_element_on_screen(driver,f'//*[@id="react-root"]/section/main/div/div[{table_num}]/article/div[1]/div',time = 5)
			except :
				table_num = 2
				self.execute_when_element_on_screen(driver,f'//*[@id="react-root"]/section/main/div/div[{table_num}]/article/div[1]/div')

			print('table_num',table_num)

			current_po = 0
			# pixles for first time  ---  300
			driver.execute_script(f"window.scrollTo({current_po},{current_po + 300});")
			current_po = 300
			# time.sleep(5)

			element_varation = 2
			for i in range(1,math.ceil(int(post)/3)+1):
				
				for j in range(1,4):
					print(((i-1)*3)+j,end=' ')
					# click on image
					# image_xpath = f'//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[{i}]/div[{j}]'
					try :							
						image_xpath = f'//*[@id="react-root"]/section/main/div/div[{element_varation}]/article/div[1]/div/div[{i}]/div[{j}]'
						self.execute_when_element_on_screen(driver,image_xpath,time=1.5)
					except :
						element_varation = 3
						image_xpath = f'//*[@id="react-root"]/section/main/div/div[{element_varation}]/article/div[1]/div/div[{i}]/div[{j}]'
						self.execute_when_element_on_screen(driver,image_xpath,time=2)

					image_element = driver.find_element_by_xpath(image_xpath)
					image_element.click()

					# like button click
					# here it can be change to normal !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
					# Like_bt_xpath = f'/html/body/div[4]/div[2]/div/article/div[{element_varation}]/section[1]/span[1]/button/div'
					Like_bt_xpath = f'/html/body/div[4]/div[2]/div/article/div[{3}]/section[1]/span[1]/button/div'
					self.execute_when_element_on_screen(driver,Like_bt_xpath)
					if LIKE :
						try :
							like_xpath = f"//*[name()='svg'][@aria-label ='Like']"
							driver.find_element_by_xpath(like_xpath).click()
							print('pic liked')
						except :
							unlike_xpath = f"//*[name()='svg'][@aria-label ='Unlike']"
							driver.find_element_by_xpath(unlike_xpath)
							print('already liked')

					else :
						try :
							unlike_xpath = f"//*[name()='svg'][@aria-label ='Unlike']"
							driver.find_element_by_xpath(unlike_xpath).click()
							print('removed like')
						except :
							like_xpath = f"//*[name()='svg'][@aria-label ='Like']"
							driver.find_element_by_xpath(like_xpath)						
							# like.click()
							print('already not liked')
						


					# click on exit button 
					exit_xpath = '//div/button[@class="wpO6b "]'
					exit_bt = driver.find_elements_by_xpath(exit_xpath)[-1]
					exit_bt.click()

					# EXIT ON LAST POST
					if ((i-1)*3)+j == int(post) :
						return

				driver.execute_script(f"window.scrollTo({current_po},{current_po + 250});")
				# for each post ---  250
				current_po += 250
				
		try:
			private = driver.find_element_by_xpath('//*[@class="rkEop"]').text
		
			if private == 'This Account is Private' :
				print("\nThis account is private can't do anything\n")
		except:	
			print("account is not private woking hard to complete task")
			# because there is only 42 elements are possible on screen at once
			if int(post) <= 40 :
				fun2()                
			else:
				fun1()

	def logout(self):	
		driver = self.driver
		print("opening profile")
		
		driver.get(f'https://www.instagram.com/{self.user}/')

		# open settings 
		setting_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button'
		self.execute_when_element_on_screen(driver,setting_xpath)
		driver.find_element_by_xpath(setting_xpath).click()
		print("opening settings")
		
		# loging out
		# time.sleep(0.2)
		loging_out = '//button[text()="Log Out"]'
		self.execute_when_element_on_screen(driver,loging_out)
		driver.find_element_by_xpath(loging_out).click()
		print('loging out !!')
		driver.close()

	def execute_when_element_on_screen(self,driver,xpath,time=10) :
		# print(xpath)
		WebDriverWait(driver, float(time)).until(EC.element_to_be_clickable((By.XPATH, xpath)))
