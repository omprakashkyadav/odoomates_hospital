# _*_ Coding: utf-8 _*_

from odoo import models, fields, api, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    name = fields.Char(string="Test")
    name_seq = fields.Char(string="Patient ID", required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male', string='Gender')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], string='Age Group', compute='set_age_group')
    patient_name = fields.Char(string="Name", required=True, track_visibility="always")
    patient_age = fields.Integer(string="Age", track_visibility="always")
    notes = fields.Text(string="Registration Note")
    image = fields.Binary(string="Image", attachment=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result