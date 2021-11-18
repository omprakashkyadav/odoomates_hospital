# _*_ Coding: UTF-8 _*_

{
    "name": "Hospital Management",
    "summery": "*** This Module for managing the hospital ***",
    "version": "12.0.0.0",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "author": "Omprakash Yadav",
    "website": "https://github.com/omprakashkyadav/",
    "depends": ['base', 'mail', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/mail_template.xml',
        'data/data.xml',
        'data/sequence.xml',
        'wizard/create_appointment.xml',
        'views/appointment.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'reports/reports.xml',
        'reports/patient_card.xml',
        'menu/menu.xml'
    ],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False
}
