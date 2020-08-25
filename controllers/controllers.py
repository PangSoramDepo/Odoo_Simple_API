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
_AURL='/api/'
_Log="--------------------------API---------------------------"

class API_Route_Controller(http.Controller):
    @http.route(_AURL+'check-health', auth='public')
    def index(self):
        return "Health Is Still Alive"

    @http.route(_AURL+'<string:model>/all',type='json',methods=["GET"], auth='user')
    def model_all(self,model):
        return Utils(model).all()

    @http.route(_AURL+'<string:model>/limit/<int:limit>',type='json',methods=["GET"], auth='user')
    def model_limit(self,model,limit):
        return Utils(model).take(limit).get()

    @http.route(_AURL+'<string:model>/where',type='json',methods=["GET"], auth='user')
    def model_where(self,model):
        return Utils(model).where('id','=',40).take(limit).get()

    @http.route(_AURL+'<string:model>/add',type='json',methods=["POST"], auth='user')
    def model_insert(self,model,**kw):
        return Utils(model).insert(kw)

    @http.route(_AURL+'<string:model>/delete/<int:id>',type='json',methods=["POST"], auth='user')
    def model_delete(self,model,id):
        return Utils(model).where('id','=',id).delete()

    @http.route(_AURL+'<string:model>/update/<int:id>',type='json',methods=["POST"], auth='user')
    def model_update(self,model,id,**kw):
        return Utils(model).where('id','=',id).update(kw)