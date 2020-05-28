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
while 1:
	q_list = requests.get('http://127.0.0.1:5000/get_q_list')
	queue = q_list.json()[1][random.randint(0, len(q_list.json()[1])-1)]
	response = requests.get('http://127.0.0.1:5000/add_mes?Q='+ queue +'&M=' + str(round(random.uniform(0, 2), 2)) )
	print(response.json()) 
	time.sleep(round(random.uniform(0, 0.5), 2))
	if random.uniform(0, 1) > 0.98:
		response = requests.get('http://127.0.0.1:5000/Create_queue?Q=queue'+str(round(random.uniform(0, 10), 2)) )
