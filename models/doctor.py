# _*_ Coding: utf-8 _*_

from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char(string='Name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    user_id = fields.Many2one("res.users", string="Related User")
