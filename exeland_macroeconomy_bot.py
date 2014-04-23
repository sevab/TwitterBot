user_list = ['@baskind', '@sandy_doo', '@pragyan_damani', '@angzhiquan']
usersDB = {
			'@baskind':['ub208','example_password1', 0],
			'@sandy_doo':['am636', 'example_password2', 0],
			'@pragyan_damani':['pd285', 'example_password3', 0],
			'@angzhiquan' :['eza202', 'example_password4', 0]
			}


import mechanize
import cookielib

def login(username, password):
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.open('http://macro.exeter.ac.uk/macro/site/login')
	br.select_form(nr=0)
	br.form['LoginForm[username]'] = username
	br.form['LoginForm[password]'] = password
	br.submit()
	html = br.response().readlines()
	return html

def extract_digit(string):
	temp = ''
	for s in string:
		if s.isdigit():
			temp+=s
	string = int(temp)
	return string
	

	
import twitter
import datetime
import os
import sys

now = datetime.datetime.now()
api  = twitter.Api()

api = twitter.Api(
	consumer_key = os.environ['consumer_key'],
	consumer_secret = os.environ['consumer_secret'],
	access_token_key = os.environ['access_token_key'],
	access_token_secret = os.environ['access_token_secret']
)

def publish_tweets(tweet_list):
	now = datetime.datetime.now()
	ms = now.second

	for tweet in tweet_list:
		ms+=1
		date = ' %d:%d:%d' % (now.hour, now.minute, ms)
		tweet = tweet + date
		api.PostUpdate(tweet)
		print tweet




# Loop while the Exeland market is open
while now.hour in range(8, 19):
	tweet_list = list()

	#	Gather data on each user
	for user in user_list:
		html = login(usersDB[user][0],usersDB[user][1])
		# initial_quantity = extract_digit(html[81])
		try:
			initial_quantity = usersDB[user][2]
			remaining_quantity = extract_digit(html[82])
			
			if remaining_quantity in range(-1, 11):
				
				if initial_quantity == remaining_quantity:
					continue
					
				elif remaining_quantity == 0:
					tweet = 'You\'ve just sold out all of your stock. Go sell some more! %s' % (user)
					usersDB[user][2] = remaining_quantity
					tweet_list.append(tweet)
					
				elif remaining_quantity > initial_quantity:
					usersDB[user][2] = remaining_quantity
					print user, remaining_quantity
					
				elif remaining_quantity < initial_quantity:
					diff = initial_quantity - remaining_quantity 
					tweet = "Someone just bought %d units from you. You have just %d units remaining %s" % (diff, remaining_quantity, user)
					tweet_list.append(tweet)
					usersDB[user][2] = remaining_quantity
					print user, remaining_quantity, "diff = ", diff
				
				else:
					#print user, "Nothing has changed. Monitoring..."
					continue

		except:
			continue
	
	#	Tweet
	if not tweet_list:
		continue
	else:
		print tweet_list
		publish_tweets(tweet_list)		# what if tweet_list is empty?
		tweet_list = list()
		print tweet_list
		
else:
	print "Macroeconomy is Closed"
	sys.exit(1)