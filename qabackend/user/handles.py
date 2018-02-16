# coding:utf-8

import datetime
import json

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QUANTAXIS.QAUtil.QASql import QA_util_sql_mongo_setting
from QUANTAXIS.QASU.user import QA_user_sign_in,QA_user_sign_up

class SignupHandler(RequestHandler):
    def get(self):
        username=self.get_argument('user',default='admin')
        password=self.get_argument('password',default='admin')
        if QA_user_sign_up(username,password,client=QA_util_sql_mongo_setting()):
            self.write('SUCCESS')
        else:
            self.write('WRONG')



class SigninHandler(RequestHandler):
    def get(self):
        username=self.get_argument('user',default='admin')
        password=self.get_argument('password',default='admin')
        res=QA_user_sign_in(username,password,client=QA_util_sql_mongo_setting())
        if res is not None:
            self.write('SUCCESS')
        else:
            self.write('WRONG')