###########################################
# Author : PANG-SORAM-DEPO
# Github : https://github.com/PangSoramDepo
###########################################

import json
import logging

from operator import attrgetter
from odoo.http import request
from odoo import http

# TODO : Add your Model and Field you want to search here :
models={
    'res.partner'   :   ['id','name','display_name'],
    'library.book'  :   ['id','name','custom_name','age_days','date_release']
}

_logger=logging.getLogger(__name__)

g_take=5
g_condition=[]
g_model=None

class Utils:
    def __init__(self, model):
        self.model=model
        self._restore()
        self._set_g_modle()

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

    def insert(self,kw):
        return g_model.create(kw)
    
    def delete(self):
        result=g_model.search(g_condition).unlink()
        return result

    def update(self,kw):
        model=g_model.search(g_condition)
        for x in model:
            result=model.update(kw)
        return result

    def _private_all(self,limit=None):
        raw_data=g_model.search(g_condition) if limit is None else g_model.search(g_condition,limit=limit)
        data=[]
        for x in raw_data:
            data.append(self._get_key_value(x,*models[self.model]))
        return data

    def _get_key_value(self,obj,*arg):
        data={}
        for x in arg:
            data[x]=attrgetter(x)(obj)
        return data

    def _set_g_modle(self):
        global g_model
        g_model=request.env[self.model]

    def _restore(self):
        global g_take
        global g_condition
        g_take=5
        g_condition=[]