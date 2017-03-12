#definitia modulului
{
	'name': 'Vet Clinic',
	'version': '1.0',
	'description': """
		Vet Clinic Application
			- list of animals
			- list of breeds
			- create appointments
	""",
	'author': 'Ioana Cotet',
	'depends': ['base_setup'],
	'data': ['vetclinic_view.xml',
			'report_animal.xml',
			'menus.xml',
	],
	'demo': [],
	'installable': True,
	'auto_install': False,
}