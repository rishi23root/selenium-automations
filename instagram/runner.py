import time 
from insta_bot import module
from getpass import getpass

def timer(funtion):
	import time
	def wrapper(*args,**kwargs):
		t1= time.time()
		funtion(*args,**kwargs)
		t2 = time.time() - t1
		if t2 < 300 :
			print("Total time taken in working",str(round(t2,3))+'s')
			pass
		else :
			print("Total time taken in working",str(round(t2/60,3))+'m')

	return wrapper


@timer
def instalikes(username,password,target_id):
	rishi = module(username,password)
	rishi.open_insta()
	if rishi.login() :
		# find person on instagram 
		if rishi.find_person(target_id) :				
			# count numbers of post 
			rishi.countphotos()
			# like all of the posts
			# rishi.likeall(LIKE=True)
			# like some of the posts min = 10
			rishi.like_some()
			# logot from your account
		rishi.logout()
	


username = input('Enter your username :')
password = getpass('Enter your password <safe input>:')
target_id = input('Enter your target_id :')

instalikes(username,password,target_id)

input('press Enter to EXIT -|')
