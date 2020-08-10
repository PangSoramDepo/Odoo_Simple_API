###########################################
# Author : PANG-SORAM-DEPO
# Github : https://github.com/PangSoramDepo
###########################################

import logging

from odoo import http
from odoo.http import request
from operator import attrgetter
from .utils import Utils

_logger = logging.getLogger(__name__)
_AULR='/api/'
_Log="--------------------------API---------------------------"

class MyViewModule(http.Controller):
    @http.route(_AULR+'check-health', auth='public')
    def index(self, **kw):
        return "Health Is Still Alive"

    @http.route(_AULR+'<string:model>/all',type='json',methods=["GET"], auth='public')
    def model_all(self,model):
        partner=Utils(model)
        data=partner.all()
        del partner
        return data

    @http.route(_AULR+'<string:model>/limit/<int:limit>',type='json',methods=["GET"], auth='user')
    def model_limit(self,model,limit):
        partner=Utils(model)
        return partner.take(limit).get()

    @http.route(_AULR+'<string:model>/where',type='json',methods=["GET"], auth='public')
    def model_where(self,model):
        partner=Utils(model)
        return partner.where('name','ilike','man').where('id','=',40).take(limit).get()

    @http.route(_AULR+'<string:model>/add',type='json',methods=["POST"], auth='public')
    def model_insert(self,model,**kw):
        partner=Utils(model)
        return partner.insert(kw)

    @http.route(_AULR+'<string:model>/delete/<int:id>',type='json',methods=["POST"], auth='user')
    def model_delete(self,model,id):
        partner=Utils(model)
        return partner.where('id','=',id).delete()

    @http.route(_AULR+'<string:model>/update/<int:id>',type='json',methods=["POST"], auth='public')
    def model_update(self,model,id,**kw):
        partner=Utils(model)
        return partner.where('id','=',id).update(kw)
