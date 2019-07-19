{
    'name': 'Peruvian Payroll & Human Resources',
    'author': 'Yubel Escobedo',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
            'hr_payroll'],
    'external_dependencies': {
        'python': [
                'num2words'
                ]
        },
    'contributors': [
        "Yubel Escobedo <yubel.92@hotmail.com>",
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.4',
    'description': """
Peruvian Payroll & Human Resources.
==================================
    -Payroll configuration for Peru localization.
    -All contributions rules for Peru payslip.
    * Employee Basic Info
    * Employee Contracts
    * Attendance, Holidays and Sick Licence   
    * Employee PaySlip
    * Allowances / Deductions / Company Inputs
    * Extra Time
    * Pention Chilean Indicators
    * Payroll Books 
    * Previred Plain Text
    , ...
    Report
  """,
    'category': 'Localization/Peru',
    'active': True,
    'data': [
        #'views/menu_root.xml',
        #'views/hr_indicadores_previsionales_view.xml',
        #'views/hr_salary_rule_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_employee.xml',
        #'views/hr_payslip_view.xml',
        'views/hr_afp_view.xml',
        #'views/hr_payslip_run_view.xml',
        'views/hr_contribution_register_view.xml',
        #'views/report_payslip.xml',
        #'views/report_hrsalarybymonth.xml',
        #'views/hr_salary_books.xml',
        'data/l10n_cl_hr_payroll_data.xml',
        #'wizard/wizard_export_csv_previred_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['demo/l10n_cl_hr_payroll_demo.xml'],
    'installable': True,
    'application': False,
    'auto_install': False
}
