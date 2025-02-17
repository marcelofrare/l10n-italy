import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-l10n-italy",
    description="Meta package for oca-l10n-italy Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-l10n_it_abicab',
        'odoo12-addon-l10n_it_account',
        'odoo12-addon-l10n_it_account_stamp',
        'odoo12-addon-l10n_it_account_tax_kind',
        'odoo12-addon-l10n_it_causali_pagamento',
        'odoo12-addon-l10n_it_codici_carica',
        'odoo12-addon-l10n_it_corrispettivi',
        'odoo12-addon-l10n_it_corrispettivi_fatturapa_out',
        'odoo12-addon-l10n_it_corrispettivi_sale',
        'odoo12-addon-l10n_it_ddt',
        'odoo12-addon-l10n_it_esigibilita_iva',
        'odoo12-addon-l10n_it_fatturapa',
        'odoo12-addon-l10n_it_fatturapa_in',
        'odoo12-addon-l10n_it_fatturapa_out',
        'odoo12-addon-l10n_it_fatturapa_out_ddt',
        'odoo12-addon-l10n_it_fatturapa_out_stamp',
        'odoo12-addon-l10n_it_fatturapa_pec',
        'odoo12-addon-l10n_it_fiscal_document_type',
        'odoo12-addon-l10n_it_fiscal_payment_term',
        'odoo12-addon-l10n_it_fiscalcode',
        'odoo12-addon-l10n_it_ipa',
        'odoo12-addon-l10n_it_pec',
        'odoo12-addon-l10n_it_rea',
        'odoo12-addon-l10n_it_sdi_channel',
        'odoo12-addon-l10n_it_split_payment',
        'odoo12-addon-l10n_it_vat_registries',
        'odoo12-addon-l10n_it_website_sale_fiscalcode',
        'odoo12-addon-l10n_it_withholding_tax',
        'odoo12-addon-l10n_it_withholding_tax_causali',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
