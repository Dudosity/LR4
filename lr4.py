#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import requests
from lxml import html
import json
import http.client, urllib.parse
import datetime, time
from flask import send_file
from flask_cors import CORS
from multiprocessing import Queue
from flask import request
from flask_swagger import swagger

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
i = 0 
Q = {}
respone = []
q_settings = {}
statistic = {}
# <multiprocessing.queues.Queue object at 0x1081c12b0>
Q["queue1"] = Queue()
Q["queue2"] = Queue()
Q["queue3"] = Queue()
Q["queue4"] = Queue()
statistic["queue1"] = {}
statistic["queue2"] = {}
statistic["queue3"] = {}
statistic["queue4"] = {}
statistic["queue1"]["count_mes"] = 0
statistic["queue2"]["count_mes"] = 0
statistic["queue3"]["count_mes"] = 0
statistic["queue4"]["count_mes"] = 0
# Блокировка / вечное ожидание...
"""
http://127.0.0.1:5000/Create_queue?Q=new_queue
http://127.0.0.1:5000/get_q_list
http://127.0.0.1:5000/add_mes?Q=new_queue&M=%22get%20some%20work%22
http://127.0.0.1:5000/getmes?Q=new_queue
"""


@app.route('/getmes', methods=['GET'])
def getmes():
    Queue_name = request.args.get('Q')
    try:
        statistic[Queue_name]["count_mes"] -= 1
             
        return jsonify("Success", str(Q[Queue_name].get()))
    except:
        return jsonify("failed or empty")
@app.route('/Create_queue', methods=['GET'])
def Create_queue():
    Queue_name = request.args.get('Q')
    try:
        Q[Queue_name] = Queue()
        return jsonify("Succes")
    except:
        return jsonify("failed")

@app.route('/add_mes', methods=['GET'])
def add_mes():
    Queue_name = request.args.get('Q')
    mes = request.args.get('M')
    try:
        Q[Queue_name].put(mes)
        statistic[Queue_name]["count_mes"] += 1
        return jsonify("Success")
    except:
        return jsonify("failed")

@app.route('/get_q_list', methods=['GET'])
def get_q():
    respone.clear()
    try:
        for key in Q:
            respone.append(key)
        return jsonify("Queues List",respone)
    except:
        return jsonify("failed")

@app.route('/get_settings', methods=['GET'])
def get_settings():
    try:
        return jsonify(q_settings)
    except:
        return jsonify("failed")

@app.route('/get_statistic', methods=['GET'])
def get_stat():
    try:
        return jsonify(statistic)
    except:
        return jsonify("failed")

if __name__ == '__main__':
    app.run(debug=True)