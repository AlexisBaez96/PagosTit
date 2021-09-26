# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Sale & Purchase Vouchers',
    'version' : '1.0',
    'summary': 'Manage your debts and credits thanks to simple sale/purchase receipts',
    'description': """
TODO

El sistema de facturación incluye recibos y comprobantes (una forma sencilla de realizar un seguimiento de las ventas y compras). 
También le ofrece un método sencillo para registrar pagos, sin tener que codificar resúmenes completos de la cuenta.

Este módulo gestiona:

* Entrada de cupón
* Recibo de cupón [Ventas y compras]
* Pago de cupones [clientes y proveedores]
    """,
    'category': 'Accounting',
    'sequence': 20,
    'depends' : ['account'],
    'demo' : [],
    'data' : [
        'security/ir.model.access.csv',
        'views/account_voucher_views.xml',
        'security/account_voucher_security.xml',
        'data/account_voucher_data.xml',
    ],
    'auto_install': False,
    'installable': True,
}
