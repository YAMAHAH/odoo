# -*- coding: utf-8 -*-
{
    'name': "财宝盒软件",
    'summary': """
       多公司财务软件(推广版)""",
    'description': """
        多公司总账和报表功能。以简单、直接、易用、智能为设计原则。没有繁琐的初始化和配置，不用结账和反结账、过账等冗余操作是中国会计的最佳实践。
    """,
    'author': "财宝盒软件",
    'website': "http://www.88v88v.com",
    'category': 'accountcore',
    'version': '13.12.25.20201027_gamma',
    'depends': ['base', 'web', 'base_import'],
    'application': True,
    'license': 'LGPL-3',
    'images': [
        'static/images/main_screenshot.png',
        'static/description/icon.png',
        'static/description/accountbalance.png',
        'static/description/begining.png',
        'static/description/cashflow.png',
        'static/description/report.png',
        'static/description/searchentry.png',
        'static/description/subsidiarybook.png',
        'static/description/voucher.png', ],
    'data': [
        'views/assetsAdd_templates.xml',
        'security/users.xml',
        'views/views.xml',
        'views/ac_currency_views.xml',
        'views/accounts_balance_views.xml',
        'wizard/build_voucher_views.xml',
        'wizard/clone_vouchers_views.xml',
        'wizard/begin_balance_views.xml',
        'wizard/import_vouchers_views.xml',
        'wizard/change_org_lock_date_views.xml',
        'wizard/change_org_class_views.xml',
        'report/voucher_print_templates.xml',
        'report/account_balance_report_template.xml',
        'report/account_subsidiary_book_template.xml',
        'views/reports.xml',
        'views/autoNumber.xml',
        'views/acshop_views.xml',
        'views/menu.xml',
        'data/default_currency_data.xml',
        'data/default_data.xml',
        'data/report_model.xml',
        'data/help_data.xml',
        'security/ir.model.access.csv',
        'security/record_group_role_ac.xml',
        'security/record_group_role_search.xml',
        'security/record_group_system.xml',
    ],
    'qweb': [
        'views/btn_templates.xml',
        'static/xml/jexcel.xml',
        'static/xml/base_extend.xml',
        'views/acshop_templates.xml',
    ],
    'css': [
        'static/css/accountcore.css',
        'static/css/jexcel.css',
        'static/css/jsuites.css',
    ],
    'post_init_hook': '_load',
    'uninstall_hook': '_uninstall',
}
