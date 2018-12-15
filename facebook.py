from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os

class Facebook:

	def __init__(self,username,password):
		self.username = username
		self.password = password
		driver = webdriver.Firefox()
		self.driver = driver
		self.login_to_facebook()

		

	def login_to_facebook(self):
		
		self.driver.get('http://www.facebook.com')
		#sends email and password and clicks login
		self.driver.find_element_by_id('email').send_keys(self.username)
		self.driver.find_element_by_id('pass').send_keys(self.password)
		#logs in to facebook
		try:
			self.driver.find_element_by_id('u_0_2').click()
		except:
			try:
				self.driver.find_element_by_id('u_0_3').click()
			except:
				self.driver.find_element_by_id('u_0_w').click()
		self.driver.execute_script("window.alert = function() {};")

	

	
	
	def get_friend_list(self,name,ids):
		#name argument can be anything for file name
		SCROLL_PAUSE_TIME = 5

		#opens the url of the given id
		self.driver.get('https://www.facebook.com/'+ids+'/friends')
		self.driver.execute_script("window.alert = function() {};")

		#height for scrolling through
		last_height = self.driver.execute_script("return document.body.scrollHeight")
		
		while True:
			try:
				old_data = open(name,'r')
				old_datas = old_data.readlines()
				old_data.close()
			except Exception as t:
				print(t)
			fo = []
			p = self.driver.find_elements_by_css_selector('div.fsl.fwb.fcb')
			try:
				for aas in p:	
					links = aas.find_element_by_tag_name('a')
					datas = links.get_attribute('href').split('?')[0]
					ids = datas.strip().split('/')[-1]
					names = links.text
					#profile.php are profiles without username
					#friends whose ids are deactivated or ...
					if ids!='profile.php' and ids!='friends#':
						d = names+':'+ids
						if d not in fo:
							#print(d)
							fo.append(d)
				
				f = open(name, 'w')							
				f.write('\n'.join(fo))
				f.close()	
				f = open(name,'r')
				try:
					if set(old_datas) == set(f.readlines()):
						break
				except Exception as e:
					print(e)
				f.close()
				# Scroll down to bottom
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			    	# Wait to load page
				time.sleep(SCROLL_PAUSE_TIME)

			    	# Calculate new scroll height and compare with last scroll height
				new_height = self.driver.execute_script("return document.body.scrollHeight")
				if new_height == last_height:
					break
				last_height = new_height

			except Exception as e:
				print(e)
				break



	
	def my_friends(self):
		# function to get own friend list
		self.get_friend_list(self.username,self.username)

		
	def send_friend_request(self,ids):
		#function for sending friend list here id is the username of the person to send friend request
		self.driver.get('https://www.facebook.com/'+ids)
		time.sleep(5)
		self.driver.execute_script("window.alert = function() {};")
		try:
			data = self.driver.find_element_by_css_selector('button.FriendRequestAdd.addButton')
			data.click()
			print('sent to' + ids)
		except Exception as e:
			print(e)



	def send_message(self,username,message,spam=False):
		#function send message 
		p = 'https://www.facebook.com/messages/t/'+username
		self.driver.execute_script("window.alert = function() {};")
		self.driver.get(p)

		#loop for spamming
		if spam == True:
			while 1:
				self.driver.find_element_by_class_name('_5rpu').send_keys(str(message)+Keys.RETURN)
		else:
			self.driver.find_element_by_class_name('_5rpu').send_keys(str(message)+Keys.RETURN)



	def message_all(self,message):
		#function to send message to all friends 
		#message is the text to send 
		self.my_friends()
		friend_list = open(self.username,'r')
		friends = friend_list.readlines()
		for friend in friends:
			self.send_message(friend.split(':')[-1],message)

	def like(self,username=None):
		#this is kind of incomplete
		#function to like all the posts
		#for liking all the posts of a friend pass username paramenter
		if username is not None:
			self.driver.get("https://www.facebook.com/"+username)
			time.sleep(3)
			self.driver.execute_script("window.alert = function() {};")
			class_name = "UFILikeLink"
		else:
			class_name = "_6a-y"
			

		SCROLL_PAUSE_TIME = 5
		
		while True:
			posts = self.driver.find_elements_by_class_name(class_name)
			print(len(posts))
			x = 0
			for post in posts:
				if post.get_attribute('aria-pressed') is not False:
					try:	
						x = x+1
						post.click()
						print("clicked")
						print(x)
					except Exception as e:
						print(e)
					
			
			
			#height for scrolling through
			last_height = self.driver.execute_script("return document.body.scrollHeight")
			# Scroll down to bottom
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load page
			time.sleep(SCROLL_PAUSE_TIME)

			# Calculate new scroll height and compare with last scroll height
			new_height = self.driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
				
		
	

		

