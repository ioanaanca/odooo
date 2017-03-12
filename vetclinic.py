from openerp.osv import osv, fields

class vetclinic_animal(osv.Model):
	_name = "vetclinic.animal"
	_columns = {
		'name': fields.char('Name', size=30, required=True),
		'birthdate': fields.date('Birth Date'),
		'tags_ids': fields.many2many('vetclinic.tags', string='Tags'),
		'classification_id': fields.many2one('vetclinic.classification', 'Classification'),
		'clinic_ids': fields.many2many('vetclinic.clinic', string='Clinic'),
		'appointment_ids': fields.many2many('vetclinic.appointment', string='Appointments', readonly=True),
		# 'res_partner_id':fields.many2one('res.partner', 'Owner'),
	}
	
# class vetclinic_res_partner(osv.Model):
	# _inherit = "res.partner"
	# _columns = {
		# 'animal_ids':fields.one2many('vetclinic.animal','res_partner_id',string="Pets"), #o relatie one2many trebuie sa aiba si o relatie many2one
	# }
class vetclinic_tags(osv.Model):
	_name = "vetclinic.tags"
	_columns = {
		'name': fields.char('Name', size=30),
		'animal_ids': fields.many2many('vetclinic.animal', string='Animals', readonly=True),
	}
	
class vetclinic_classification(osv.Model):
	_name = "vetclinic.classification"
	_columns = {
		'name': fields.char('Name', size=30, required=True),
	}
	
class vetclinic_doctor(osv.Model):
	_name = "vetclinic.doctor"
	_columns = {
		'name': fields.char('Name', size=30),
		'mail': fields.char('E-mail', size=30),
		'clinic_ids': fields.many2many('vetclinic.clinic', string='Clinic'),
	}
	
class vetclinic_extended(osv.Model):
	_name = "vetclinic.extended"
	_inherit = "vetclinic.animal"
	_columns = {
		'name': fields.char('Name', size=30),
		'classification_id': fields.many2one('vetclinic.classification', 'Classification'),
		'doctor_id': fields.many2one('vetclinic.doctor', 'Doctor'),
	}
	
class vetclinic_clinic(osv.Model):
	_name = "vetclinic.clinic"
	_columns = {
		'name': fields.char('Name', size=30),
		'animal_ids': fields.many2many('vetclinic.animal', string='Animals', readonly=True),
		'doctor_ids': fields.many2many('vetclinic.doctor', string='Doctors', readonly=True),
	}
	
class vetclinic_appointment(osv.Model):
	_name = "vetclinic.appointment"
	_columns = {
		'name': fields.char('Name', size=30),
		'date': fields.date('Date'),
		'description':  fields.char('Description', size=50),
		'animal_ids': fields.many2many('vetclinic.animal', string='Animal'),
		'doctor_id': fields.many2one('vetclinic.doctor', 'Doctor'),
		'clinic_id': fields.many2one('vetclinic.clinic', 'Clinic'),
	}

