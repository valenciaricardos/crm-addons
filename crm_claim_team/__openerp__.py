# -*- coding: utf-8 -*-
# (c) 2015 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Crm Claim Team",
    "version": "8.0.1.0.0",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "contributors": [
        "Esther Martín <esthermartin@avanzosc.es>",
        "Ana Juaristi <anajuaristi@avanzosc.es>",
    ],
    "depends": [
        "crm_claim",
        "sales_team",
    ],
    "category": "Customer Relationship Management",
    "data": [
        "views/crm_claim_view.xml",
        "views/crm_claim_stage_view.xml",
        "views/sales_team_view.xml",
    ],
    "installable": True
}
