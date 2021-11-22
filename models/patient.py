# _*_ Coding: utf-8 _*_

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name_seq, rec.patient_name)))
        return res

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('The Ae must be greater than 5 year'))

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    def action_patient_appointment(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def _get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    name = fields.Char(string="Test")
    name_seq = fields.Char(string="Patient ID", required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male', string='Gender')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], string='Age Group', compute='set_age_group')
    patient_name = fields.Char(string="Name", required=True, track_visibility="always")
    patient_age = fields.Integer(string="Age", track_visibility="always")
    notes = fields.Text(string="Registration Note")
    image = fields.Binary(string="Image", attachment=True)
    appointment_count = fields.Integer(string='Appointment', compute='_get_appointment_count')
    active = fields.Boolean(string='Active', default=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    doctor_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Doctor Gender')
    patient_pro = fields.Many2one('res.users', string='PRO')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    email = fields.Char(string='Email')

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    def action_send_card(self):
        template_id = self.env.ref('odoomates_hospital.mail_template_patient_card').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
