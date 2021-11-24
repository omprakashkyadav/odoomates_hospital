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
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': 'Patient Created by the Wizard'
        }
        self.patient_id.message_post(body='Appointment Created Successfully', subject='Appointment Creation')
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print("Get Data from Database")
        appointment_count = self.env['hospital.appointment'].search_count([])
        print("No. of Appointment", appointment_count)
        appointments = self.env['hospital.appointment'].search([])
        print("Appointments", appointments)
        for rec in appointments:
            print("Appointment Name", rec.name)

