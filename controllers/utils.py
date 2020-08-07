###########################################
# Author : PANG-SORAM-DEPO
# Github : https://github.com/PangSoramDepo
###########################################

import json

from operator import attrgetter
from odoo.http import request
from odoo import http

models={
    'res.partner'   :   ['id','name','display_name']
}

g_take=5
g_condition=[]

class Utils:
    def __init__(self, model):
        self.model=model
        self._restore()

    def all(self):
        return self._private_all()

    def where(self,field,confition,value):
        global g_condition
        g_condition.append((field,confition,value))
        return self

    def take(self,take=5):
        global g_take
        g_take=take
        return self

    def get(self):
        return self._private_all(g_take)

    def _private_all(self,limit=None):
        raw_data=request.env[self.model].search(g_condition) if limit is None else request.env[self.model].search(g_condition,limit=limit)
        data=[]
        for x in raw_data:
            data.append(self._get_key_value(x,*models[self.model]))
        return data

    def _get_key_value(self,obj,*arg):
        data={}
        for x in arg:
            data[x]=attrgetter(x)(obj)
        return data

    def _restore(self):
        global g_take
        global g_condition
        g_take=5
        g_condition=[]