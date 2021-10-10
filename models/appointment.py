# _*_ Coding: utf-8 _*_

from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string='Registration Note')
    appointment_date = fields.Date(string='Date', required=True)