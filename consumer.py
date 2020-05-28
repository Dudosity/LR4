import requests
import random
import time
"""
http://127.0.0.1:5000/Create_queue?Q=new_queue
http://127.0.0.1:5000/get_q_list
http://127.0.0.1:5000/add_mes?Q=new_queue&M=%22get%20some%20work%22
http://127.0.0.1:5000/getmes?Q=new_queue
"""
queue = ''
stat_count = 0
while 1:
	q_list = requests.get('http://127.0.0.1:5000/get_q_list')
	queue = q_list.json()[1][random.randint(0, len(q_list.json()[1])-1)]
	getmes = requests.get('http://127.0.0.1:5000/getmes?Q='+ queue)
	time.sleep(float(getmes.json()[1]))
	if getmes.json()[1] == 'Success':
		stat_count += 1
	print("cons1",getmes.json()[1])
	# print json content 

