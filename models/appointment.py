# _*_ Coding: utf-8 _*_

from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date desc'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def _get_default_note(self):
        return "Hi! You can write note here"

    def _get_default_patient(self):
        return 1

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, default=_get_default_patient)
    patient_age = fields.Integer(string='Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration Note', default=_get_default_note)
    appointment_date = fields.Date(string='Date', required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             string='Status', readonly=True, default='draft')
    doctor_note = fields.Text(string="Note")
    pharmacy_note = fields.Text(string="Note")

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

