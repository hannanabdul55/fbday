
import facebook
import requests
import datetime

'''
Add your wishes templates below in the wishes list where, in each entry the string "<name>"
will be replaced with the name of the wisher 
'''
wishes = ["Hey <name>, Thank you! :) ", "Thank You, <name> :D"]
count =0


def some_action(post):
	global count
	#print(post['created_time'])
	#print(graph.get_object(post['id'].split('_')[1]))
	resp = graph.request("/" + post['id'] +"?fields=from,likes,message")
	#print(resp)
	name = resp["from"]["name"].split(" ")[0]
	temp_len = len(wishes)
	if name is None:
		name = ""
	time = post['created_time']
	message = resp["message"]
	#print(resp.get("likes","likes : None"))
	if bday.replace('/','-') in time and  resp.get("likes","None")=="None":
		graph.put_like(post['id'])
		if "happy" in message or "bday" in message or "birthday" in message or ("many" in message and "returns" in message) :
			graph.put_comment(post['id'],wishes[count%temp_len].replace("<name>",name))
			print("posted comment: " +wishes[count%temp_len].replace("<name>",name))
			count+=1
	#print(time)
	#print(name)
	#comments = graph.get_connections(id=post['id'], connection_name='likes')
	#print(comments)
	


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
# Also, Make sure you give the "publish_posts" "access_birthday" and the "access_posts"
# Permission for the access token
# TODO: ENTER ACCESS TOKEN HERE
access_token = ''

user = 'me'
#ENTER YOUR BDAY
bday = ""
while len(bday)!=5:
	bday = raw_input("Enter Your Birthday in MM/DD Format! Ex: 22nd feb will be 02/22:")
	#bday = '01/01'
	if len(bday)!=5:
		print("Incorrect Input, try Again!")
graph = facebook.GraphAPI(access_token)
args = {'fields':'birthday'}
profile = graph.get_object(user,args = args)
a = {'limit':400}
posts = graph.get_connections(profile['id'], 'feed', args=a)
d = datetime.date.today()
if str(d.month) + '/' + str(d.day) == bday:
	print("happy Birthday!")
else:
	print("Not your bday!")
	exit()
# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
	try:
		# Perform some action on each post in the collection we receive from
		# Facebook.
		#print(posts)
		[some_action(post=post) for post in posts['data']]
		# Attempt to make a request to the next page of data, if it exists.
		posts = requests.get(posts['paging']['next']).json()
	except KeyError:
		# When there are no more pages (['paging']['next']), break from the
		# loop and end the script.
		break