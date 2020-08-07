import logging

from odoo import http
from odoo.http import request
from operator import attrgetter
from .utils import Utils

_logger = logging.getLogger(__name__)
_AULR='/api/'

class MyViewModule(http.Controller):
    @http.route(_AULR+'check-health', auth='public')
    def index(self, **kw):
        return "Health Is Still Alive"

    @http.route(_AULR+'get-all-respartner',type='json',methods=["GET"], auth='public')
    def res_partner_env(self, **kw):
        partner=Utils('res.partner')
        return partner.all()