# _*_ coding: utf-8 _*_

from odoo import models, fields, api, _


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string='Appointment Date')

    def action_create_new_appointment(self):
        """
        Method for create New Appointment
        """
        pass
