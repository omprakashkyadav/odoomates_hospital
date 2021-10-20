# _*_ Coding: UTF-8 _*_

{
    "name": "Hospital Management",
    "summery": "*** This Module for managing the hospital ***",
    "version": "12.0.0.0",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "author": "Omprakash Yadav",
    "website": "https://github.com/omprakashkyadav/",
    "depends": ['base', 'mail'],
    "data": [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/sequence.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'reports/reports.xml',
        'reports/patient_card.xml',
    ],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False
}
