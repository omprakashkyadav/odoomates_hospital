# _*_ Coding: utf-8 _*_

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals_list):
        res = super(ResPartner, self).create(vals_list)
        print("yes working")
        # do the custom code here
        return res