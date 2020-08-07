###########################################
# Author : PANG-SORAM-DEPO
# Github : https://github.com/PangSoramDepo
###########################################

from odoo.http import request
from operator import attrgetter

models={
    'res.partner'   :   ['id','name','company_id','display_name']
}

class Utils:
    def __init__(self, model):
        self.model=model

    def all(self):
        return self._private_all()

    def take(self,take):
        return self._private_all(take)

    def _private_all(self,limit=None):
        if limit is None:
            raw_data=request.env[self.model].search([])
        else:
            raw_data=request.env[self.model].search([],limit=limit)
        data=[]
        for x in raw_data:
            data.append(attrgetter(*models[self.model])(x))
        return data