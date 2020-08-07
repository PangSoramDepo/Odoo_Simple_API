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

    @http.route(_AULR+'res-partner/all',type='json',methods=["GET"], auth='public')
    def res_partner_all(self):
        partner=Utils('res.partner')
        data=partner.all()
        del partner
        return data

    @http.route(_AULR+'res-partner/limit/<int:limit>',type='json',methods=["GET"], auth='public')
    def res_partner_limit(self,limit):
        partner=Utils('res.partner')
        return partner.where('name','ilike','man').where('id','=',40).take(limit).get()