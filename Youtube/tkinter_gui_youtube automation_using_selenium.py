from tkinter import *
import datetime
from youtube import youtube 
from tkinter import messagebox
import time


root = Tk()
root.title("youtube automation ")
root.geometry("1080x720")
user = None


def not_sinin():
	global openurl,closeafter,labe
	func= Frame(box2,bd=5)
	func.place(relx = 0, rely = 0 , relheight = 0.6 ,relwidth = 1)
	
	Label(func,text= 'FUNTIONS......',font=('arial',20,'bold'),anchor = 'nw').place(relx=0,rely=0,relheight=0.1,relwidth=1)
	Label(func,text= 'DESCRIPTION  : TICK THE FUNTION TO EXECUTE THEM ',font=('arial',9,'bold'),anchor = 'nw').place(relx=0,rely=0.1,relheight=0.08,relwidth=1)

	openurl = IntVar()
	checkurl =Checkbutton(func,text = '1. open url',font=('arial',15,'bold'),variable = openurl ,onvalue=1 ,offvalue = 0,anchor = 'nw')
	checkurl.place(relx = 0, rely = 0.18 , relheight = 0.1 ,relwidth = 1)
	checkurl.select()
	
	closeafter=IntVar()
	checkcose =Checkbutton(func,text = '2. close browser after 30 sec of opening ',font=('arial',15,'bold'), anchor = 'nw',onvalue=1 ,offvalue = 0,variable = closeafter)
	checkcose.place(relx = 0, rely = 0.28 , relheight = 0.1 ,relwidth = 1)
	

	butt = Button(func,text ="EXECUTE ALL CHECKED FUNTIONS" ,font=('arial',15,'bold'),fg ='white',bg ='#34495E',command =lambda : status_12())
	butt.place(relx = 0, rely = 0.88 , relheight = 0.1 ,relwidth = 1)

	fund = Frame(box2,bd=3,bg='black')
	fund.place(relx = 0, rely = 0.62 , relheight = 0.38 ,relwidth = 1)
	labe = Label(fund,font=('arial',20,'bold'),anchor='nw')
	labe.pack(fill=BOTH,expand=True)



def yes_sinin():
	global openurl,count,like,comment,commente,subscribe,closeafter,labe
	func= Frame(box2,bd=5)
	func.place(relx = 0, rely = 0 , relheight = 0.6 ,relwidth = 1)
	
	Label(func,text= 'FUNTIONS......',font=('arial',20,'bold'),anchor = 'nw').place(relx=0,rely=0,relheight=0.1,relwidth=1)
	Label(func,text= 'DESCRIPTION  : TICK THE FUNTION TO EXECUTE THEM ',font=('arial',9,'bold'),anchor = 'nw').place(relx=0,rely=0.1,relheight=0.08,relwidth=1)

	openurl = IntVar()
	checkurl =Checkbutton(func,text = '1. open url',font=('arial',15,'bold') ,variable = openurl,onvalue= 1 ,offvalue = 0 ,anchor = 'nw')
	checkurl.place(relx = 0, rely = 0.18 , relheight = 0.1 ,relwidth = 1)
	openurl.set(1)
	
	count=IntVar()
	checkcount =Checkbutton(func,text = '2. count vieos of given url',font=('arial',15,'bold'), anchor = 'nw',onvalue=1 ,offvalue = 0,variable = count)
	checkcount.place(relx = 0, rely = 0.28 , relheight = 0.1 ,relwidth = 1)

	like=IntVar()
	checklike =Checkbutton(func,text = '3. like one by one ',font=('arial',15,'bold'), anchor = 'nw',onvalue=1 ,offvalue = 0,variable = like)
	checklike.place(relx = 0, rely = 0.38 , relheight = 0.1 ,relwidth = 1)


	subscribe = IntVar()
	checkcose =Checkbutton(func,text = '4. subscribe from video ',font=('arial',15,'bold'), anchor = 'nw',onvalue=1 ,offvalue = 0,variable = subscribe)
	checkcose.place(relx = 0, rely = 0.48 , relheight = 0.1 ,relwidth = 1)
	
	comment=IntVar()
	checkcomment =Checkbutton(func,text = '5. comment on each ',font=('arial',15,'bold'), anchor = 'nw',onvalue=1 ,offvalue = 0,variable = comment)
	checkcomment.place(relx = 0, rely = 0.58 , relheight = 0.1 ,relwidth = 1)

	commente = Entry(func,font=('arial',10))
	commente.place(relx = 0.06, rely = 0.68 , relheight = 0.1 ,relwidth = 0.9)
	
	closeafter=IntVar()
	checkcose =Checkbutton(func,text = '6. close browser after 30 sec of opening ',font=('arial',15,'bold'), anchor = 'nw',onvalue=1 ,offvalue = 0,variable = closeafter)
	checkcose.place(relx = 0, rely = 0.78 , relheight = 0.1 ,relwidth = 1)
	

	butt = Button(func,text ="EXECUTE ALL CHECKED FUNTIONS" ,font=('arial',15,'bold'),fg ='white',bg ='#34495E',command =lambda : status_12())
	butt.place(relx = 0, rely = 0.9 , relheight = 0.1 ,relwidth = 1)


	fund =Frame(box2,bd=3,bg='black')
	fund.place(relx = 0, rely = 0.62 , relheight = 0.38 ,relwidth = 1)
	labe =Label(fund,font=('arial',20),anchor='nw')
	labe.pack(fill=BOTH,expand=True)



def funtion_action(l,s,c):
	
	if l and s and c :
		# 111
		print('like \n subscribe \n comment ')
		for i in videos:
			you.like(i)
			status.set('status : like video ')
			labe['text'] =f'video liked'
			you.commenting(commente.get())
			status.set('status : commenting ')
			labe['text'] =f'commenting \n {commente.get()}'
			
			if videos.index(i) == 0 :
				labe['text'] = you.subscribe()
				status.set('status : subscribing ')
			else :
				pass

	elif l and s and not(c) :
		# 110
		print('like \n subscribe \n not comment')

		for i in videos:
			you.like(i)
			status.set('status : video like ')
			labe['text'] =f' video liked '

			if videos.index(i) == 0 :
				labe['text'] = you.subscribe()
				status.set('status : subscribing ')
			else :
				pass


	elif l and not(s) and c :
		# 101
		print('like \n not subscribe \n comment')

		for i in videos:
			you.like(i)
			status.set('status : video like ')
			labe['text'] =f' video liked '
			you.commenting(commente.get())
			status.set('status : commenting ')
			labe['text'] =f'commenting \n {commente.get()}'
			

	elif l and not(s) and not(c) :
		# 100
		print('like \n not subscribe \n not comment')

		for i in videos:
			you.like(i)
			status.set('status : video like ')
			labe['text'] =f' video liked '

	elif not(l) and s and c :
		# 011
		print('not like \n subscribe \n comment')

		for i in videos:
			you.geturl(i)

			you.commenting(commente.get())
			status.set('status : commenting ')
			labe['text'] =f'commenting \n {commente.get()}'
			
			if videos.index(i) == 0 :
				labe['text'] = you.subscribe()
				status.set('status : subscribing ')
			else :
				pass


	elif not(l) and s and not(c) :
		# 010
		print('not like \n subscribe \n not comment')

		you.geturl(videos[0])

		labe['text'] = you.subscribe()
		status.set('status : subscribing ')
		

	elif not(l) and not(s) and c :
		# 001
		print('not like \n not subscribe \n comment')
	
		for i in videos:
			you.geturl(i)
			print(videos.index(i)+1,end=" ")
			you.commenting(commente.get())
			status.set('status : commenting ')
			labe['text'] =f'commenting \n {commente.get()}'

	elif not(l) and not(s) and not(c) :
		print('no like \n no subscribe \n no comment')
		pass


def status_12():
	global you,videos
	try:
		print(f'options\n2.{count.get()}\n3.{like.get()}\n4.{subscribe.get()}\n5.{comment.get()}\n6.{closeafter.get()} ')
	except:
		print(f"options \n2.{closeafter.get()}")


	labe['text'] = ''
	status.set('status : '+'executing codes')
	
	if signin.get() == 0:
		status.set('status : without signin')
		labe['text'] = 'setting drivers'
		you = youtube(None,None,browser = 'Edge' if v.get() == 1 else 'Chrome')
		labe['text'] = 'opening gien url' 
		
		if url2e.get() == None  or  url2e.get().strip() == '' :
			labe['text'] = 'url not given\ntry again later '
		
		else:
			you.geturl(url2e.get())
			labe['text'] = f'opened url : {url2e.get()}'

			if closeafter.get() ==  1 :
				labe['text'] ="closing browser window in 15s"

				time.sleep(10)

				you.close_end()
				labe['text'] ='window cosed '

			else:
				labe['text'] = 'work done \nyou can run again '

	else:
		# signin.get() == 1
	
		if (usere.get() == None or usere.get().strip()=='' )  or  ( passe.get() == None or passe.get().strip() == ''  ):
			labe['text' ] = "user nanme & password \ncan not remain empty "
		elif (urle.get() == None or urle.get().strip()=='' ) :
			labe['text' ] = "please provide url to EXECUTE "


		else:					
			labe['text']= f'user name = {usere.get()}'
			you =youtube(usere.get(),passe.get(),browser = 'Edge' if v.get() == 1 else 'Chrome')
			status.set(' sign in')
			labe['text'] = ' setting driver'
			
			you.geturl()
			labe['text'] = ' opening url'
			
			time.sleep(2)
			labe['text'] = ' signing in by given username '
			labe['text'] = you.signing()

			time.sleep(2)

			############################################################################################################
			# if url1 == 1 only open 1 else url2 for massive work 		
			
			labe['text'] = f'opening video page : {urle.get()}'
			
			you.geturl(urle.get())

			videos = you.scrole_page_and_video_links()  #give all videos url

			if count.get() == 1:
				print("1")
				labe['text'] = 'total videos founded :'+ str(len(videos))
				print('total videos founded :', str(len(videos)))
				status.set('status : counting videos ')
			else :
				pass

			funtion_action(like.get(),subscribe.get(),comment.get())


			# if (subscribe.get() == 1) or (like.get() == 1):
				
			# 	for i in videos:
			# 		status.set('status : like and subscribe ')
			# 		you.like(i)

			# 		if comment.get() == 1:
			# 			print("1")
			# 			if (commente.get() == None) and (commente.get().strip() == '') : 
			# 				print("none comment get")
			# 				labe['text'] = "none comment get"
			# 			else:
			# 				# you.geturl(i)
			# 				you.commenting(commente.get())
			# 				status.set('status : commenting ')
			# 				labe['text'] =f'commenting \n {commente.grt()}'
							
			# 			pass

			# 		if videos.index(i) == 0:
			# 			you.subscribe()
			# 			status.set('status : subscribing')
			# 		else:
			# 			pass

			# elif (like.get() == 0) or (subscribe.get() == 1) :
			# 	print("2.1" , subscribe.get() )
			# 	you.geturl(videos[0])
			# 	labe['text'] = you.subscribe()
			# 	status.set('status : subscribing ')
				
			
			# elif ( like.get() == 1 ) or ( subscribe.get() == 0) :
				
			# 	for i in videos:
			# 		you.like(i)
			# 		status.set('status : like')
			# 		if comment.get() == 1:
			# 			if (commente.get() == None) and (commente.get().strip() == '') : 
			# 				print("none comment get")
			# 				labe['text'] = "none comment get"
			# 			else:
			# 				# you.geturl(i)
			# 				you.commenting(commente.get())
			# 				status.set('status : commenting ')
			# 				labe['text'] =f'commenting \n {commente.grt()}'
							
			# 		else :
			# 			pass
										
			# if  (comment.get() == 1) or ( like.get() == 0 ) or ( subscribe.get() == 0) :
			# 	print("this one initialises ")
			# 	for i in videos:
			# 		if (commente.get() == None) and (commente.get().strip() == '') : 
			# 			print("none comment get")
			# 			labe['text'] = "none comment get"
			# 		else:
			# 			you.geturl(i)
			# 			you.commenting(commente.get())
			# 			status.set('status : commenting ')
			# 			labe['text'] =f'commenting \n {commente.get()}'
						


			if closeafter.get() == 1:
				labe['text'] ="closing browser window in 15s"

				time.sleep(10)

				you.close_end()
				labe['text'] ='window cosed '
			
			else :

				labe['text'] ='window will not cose automatically \ndo it manualy'

	
def submitinfo():
	userman.set(usere.get()+'@gmail.com ')
	status.set('status : '+'feeding data ')
	messagebox.showinfo("USER GIVEN INFO", f"username  = {usere.get()}\npassword  = {passe.get()}\nurl       = {urle.get()}\nsecond url= {url2e.get()}" )
	try:
		labe['text'] = usere.get()+'\n'+urle.get()+'\n'+url2e.get()
	except:
		pass



def clear():
	status.set('status : '+'clearing data TABS')
	usere.delete(0,'end')
	passe.delete(0,'end')
	urle.delete(0,'end')
	url2e.delete(0,'end')
	labe['text'] =''
	
	try:
		commente.delete(0,'end')
		count.set(0)
		like.set(0)
		subscribe.set(0)
		comment.set(0)
		closeafter.set(0)
		signin.set(0)
	
	except: 
		pass


def stoppro():
	try:
		you.close_end()

		status.set('status : '+'closing browser window')
	except:
		labe['text'] = "unable to stop \ntring first initiate the process"



def funtion():
	status.set('status : '+'confirming data')
	if signin.get() == 0:
		not_sinin()
	else:
		yes_sinin()
	


	# print(sin.instate(['selected']) 
########################### main tk code #######################################################################################


#####################  #      top frame works ##############
date = datetime.datetime.now()     
day = date.strftime("%A")          

userman=StringVar()
userman.set(user)

Tops=Frame(root, bd=1,height=45)
Tops.pack(side=TOP,fill='x')
a=Label(Tops, font=('arial',10, 'bold'),  text=f"current user ", justify= 'left',bg = '#9db4ff',anchor = 'w').place(relx = 0,rely= 0,relheight=0.5,relwidth=0.5) 
Label(Tops, font=('arial',10, 'bold'),  textvariable= userman , justify= 'left',bg = '#9db4ff',anchor = 'w').place(relx = 0,rely= 0.5,relheight=0.5,relwidth=0.5) 
b=Label(Tops, font=('arial',10, 'bold'),  text=f"Date :{date.day}/{str(date.now().month).zfill(2)}/{date.now().year} \n Day :{day}", bg = '#9db4ff',anchor = 'e').place(relx = 0.5,rely= 0,relheight=1,relwidth=0.5) 
##########################top end ############



###########        middle and main componets are here 
midle = Frame(root,background='#5FEBFF',bd=10)
midle.pack(fill =BOTH,expand = True)
###########################################
box = Frame(midle,bd=2)
box.place(relx = 0,rely= 0,relheight=0.09,relwidth=1) 

expla =Label(box,text = "AUTOMATE YOUTUBE",bg='#FF1801',font =('Arial Black',30,'bold'),fg='white')
expla.pack(side ='top',fill =BOTH,expand=False)

############################################
box1= Frame(midle,bd =10,bg ='#5D6D7E')
box1.place(relx =0,rely=0.09,relheight=0.9,relwidth=0.5)

box2 = Frame(midle,bd=10,bg='Steel Blue' )
box2.place(relx =0.5,rely=0.09,relheight=0.9,relwidth=0.5) 


browser_option = Frame(box1)
browser_option.place(relx =0,rely=0,relheight=0.12,relwidth=1)

lab =Label(browser_option,text ="Chosse your BROWSER [EDGE] RECOMMENDED",font =('arial',15,'bold') )
lab.pack(side ='top',fill= BOTH,expand= True)

v=IntVar()
Radiobutton(browser_option,text ='CHROME',font =('arial',15),variable =v,value=2).pack(side= 'left',fill= BOTH,expand= True)
Radiobutton(browser_option,text='EDGE',font =('arial',15),variable =v,value = 1).pack(side = 'right',fill= BOTH,expand= True)


user = Frame(box1)
user.place(relx =0,rely=0.13,relheight=0.06,relwidth=1)

userl = Label(user, text = 'USER NAME [email] =>',font=('arial',10,'bold') )
userl.place(relx=0,rely=0,relheight=1,relwidth=0.5)
usere = Entry(user,bd=5)
usere.place(relx=0.5,rely=0,relheight=1,relwidth=0.5)
userl2 = Label(user, text = '@gmail.com',font=('arial',10,'bold'),anchor='w' )
userl2.place(relx=0.83,rely=0,relheight=1,relwidth=0.5)

password =Frame(box1)
password.place(relx =0,rely=0.20,relheight=0.06,relwidth=1)

passl=Label(password,text='PASSWORD',font=('arial',10,'bold'))
passl.place(relx=0,rely=0,relheight=1,relwidth=0.5)
passe = Entry(password,bd=5,show='*')
passe.place(relx=0.5,rely=0,relheight=1,relwidth=0.5)


url =Frame(box1)
url.place(relx =0,rely=0.27,relheight=0.07,relwidth=1)

urll=Label(url,text='ENTER URL OF VIDEO PAGE \n(for massive work)',font=('arial',10,'bold'))
urll.place(relx=0,rely=0,relheight=1,relwidth=0.5)
urle = Entry(url,bd=5)
urle.place(relx=0.5,rely=0,relheight=1,relwidth=0.5)


url2 =Frame(box1)
url2.place(relx =0,rely=0.35,relheight=0.07,relwidth=1)

url2l=Label(url2,text='ENTER URL FOR SPECIFIC VIDEO',font=('arial',10,'bold'))
url2l.place(relx=0,rely=0,relheight=1,relwidth=0.5)
url2e = Entry(url2,bd=5)
url2e.place(relx=0.5,rely=0,relheight=1,relwidth=0.5)


butframe = Frame(box1)
butframe.place(relx =0,rely=0.43,relheight=0.08,relwidth=1)

button = Button(butframe,bg='#D6DBDF',bd=5,text='CHECK DETAILS',font=('arial',20,'bold'),command = lambda : submitinfo())
button.pack(fill=BOTH,expand=True)


fun = Frame(box1)
fun.place(relx =0,rely=0.53,relheight=0.15,relwidth=1)

head =Label(fun,text ='click on FUNTION to get options',font=('arial',15,'bold'))
head.pack(side='top',fill=BOTH,expand=True)

sinl =Label(fun,text ='Tick on signin to get more options',font=('arial',15),anchor='w')
sinl.pack(side='left',fill=BOTH,expand=True)

signin =IntVar()
sin = Checkbutton(fun,text = 'sign in',font=('arial',15,'bold'),variable= signin,onvalue=True , offvalue =False )
sin.pack(side ='right', fill =BOTH , expand = True)

funbutton = Button(box1,text= ' FUNTIONS ',bd=10,font=('Arial',20,'bold'),command=lambda:funtion())
funbutton.place(relx =0,rely=0.69,relheight=0.09,relwidth=1)
# message box

# funbutton = Button(box1,text= ' FUNTIONS ')
# funbutton.place()

clearbutton=Button(box1,text = 'clear all TABS ',bg='#F7DC6F',bd=5,font=('Arial',20,'bold'),command=lambda :clear())
clearbutton.place(relx =0,rely=0.8,relheight=0.1,relwidth=0.5)

stopbutton = Button(box1,text= 'STOP PROCESS ',bd=5,font=('Arial',20,'bold'),command= lambda : stoppro())
stopbutton.place(relx =0.5,rely=0.8,relheight=0.1,relwidth=0.5)

endbutton = Button(box1 , text= ' END OR CLOSE ',bg='#FADBD8',bd=10,font=('Arial',20,'bold'),command= lambda :root.destroy())
endbutton.place(relx =0,rely=0.9,relheight=0.1,relwidth=1)



################################################


###  #      bottom frame works

version = 1
status = ''    #'working' or not
status=StringVar()
status.set('status : '+'')
bottom = Frame(root,bd=0.5,background='black')
bottom.pack(side='bottom',fill='x')
c =Label(bottom,text = f'Develeoped by Rishabh Jain on {datetime.datetime(2020, 5, 17).date()}', justify = 'left',anchor ='w' ,background='#FEF9E7' ).pack(expand=True,side ='left',fill= BOTH)
d =Label(bottom,textvariable=status,background='#FEF9E7',anchor ='center').pack(expand=True,side='left',fill=BOTH)
e =Label(bottom , text = f'Version [{version}]' , justify='right' ,anchor ='e',background='#FEF9E7').pack(side ='right',expand=True,fill= BOTH)

#end of bottom line code 


root.mainloop()
