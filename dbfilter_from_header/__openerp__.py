# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "dbfilter_from_header",
    "version": "9.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "complexity": "normal",
    "description": """
    This addon lets you pass a dbfilter as a HTTP header.

    This is interesting for setups where database names can't be mapped to
    proxied host names.

    In nginx, use one of
    proxy_set_header X-OpenERP-dbfilter [your filter];
    proxy_set_header X-Odoo-dbfilter [your filter];

    The addon has to be loaded as server-wide module.
    """,
    "category": "Tools",
    "depends": [
        'web',
    ],
    "data": [
    ],
    "js": [
    ],
    "css": [
    ],
    "auto_install": False,
    'installable': True,
    "external_dependencies": {
        'python': [],
    },
}
