import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voxpopproj.settings')

import django
django.setup()

from voxpop.models import Firm, Review


def populate():
	eg_pro = """But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was 
	born and I will give you a complete account of the system, and expound the actual teachings of the 
	great explorer of the truth, the master-builder of human happiness."""

	eg_con = """No one rejects, dislikes, or avoids pleasure itself, 
	because it is pleasure, but because those who do not know how to pursue pleasure 
	rationally encounter consequences that are extremely painful."""

	eg_role = "Associado"

	eg_salary = 12000

	eg_est = """Nor again is there anyone who loves or pursues or desires to obtain pain of itself, 
	because it is pain, but because occasionally circumstances occur in which toil and pain can procure 
	him some great pleasure."""

	vda = add_firm('Vieira de Almeida')
	mlgts = add_firm('MLGTS')
	plmj = add_firm('PLMJ')

	add_review(vda, eg_role, eg_salary, eg_pro, eg_con, eg_est)
	add_review(mlgts, eg_role, eg_salary, eg_pro, eg_con, eg_est)
	add_review(plmj, eg_role, eg_salary, eg_pro, eg_con, eg_est)


def add_firm(name):
	f = Firm.objects.get_or_create(name=name)[0]
	return f

def add_review(firm, role, salary, pros, cons, estagio):
	r = Review.objects.create(firm=firm)
	r.role = role
	r.salary = salary
	r.pros = pros
	r.cons = cons
	r.estagio = estagio
	r.save()
	return r

#start execution here
if __name__ == '__main__':
	print "populating..."
	populate()

