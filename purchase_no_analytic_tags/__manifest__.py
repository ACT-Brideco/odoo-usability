# -*- coding: utf-8 -*-
# © 2017 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase No Analytic Tags',
    'version': '10.0.1.0.0',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'summary': 'No Analytic Tags in Purchases',
    'description': """
Purchase No Analytic Tags
=========================

This module hides analytic tags on purchase orders.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase'],
    'data': ['purchase_view.xml'],
    'installable': True,
}
