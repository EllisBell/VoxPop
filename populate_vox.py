import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voxpopproj.settings')

import django
django.setup()

from voxpop.models import Firm, Review

import codecs

####### Atencao #########
# a adicionar - Linklaters, MLGTS, Pinto de Abreu, PMBGR, Raposo Subtil, Campos Ferreira, Teixeira de Freitas etc... (nao tao in lex)
# ver tb legal500 etc.
# e isto: http://www.asap.pt/associadas_lista.html

def populate():
	eg_tagline = "de longe o pior sitio onde ja trabalhei. a evitar."

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

	# vda = add_firm('Vieira de Almeida')
	# mlgts = add_firm('MLGTS')
	# plmj = add_firm('PLMJ')

	# add_review(vda, eg_role, eg_salary, eg_pro, eg_con, eg_est)
	# add_review(mlgts, eg_role, eg_salary, eg_pro, eg_con, eg_est)
	# add_review(plmj, eg_role, eg_salary, eg_pro, eg_con, eg_est)
	
	firms = []
	f = codecs.open('namefile.txt', encoding="utf-8")
	
	for line in f:
		firm = add_firm(line)
		firms.append(firm)

	for i in range(0,5):
		add_review(firms[i], eg_tagline, 2, eg_role, eg_salary, eg_pro, eg_con, eg_est)


def add_firm(name):
	f = Firm.objects.get_or_create(name=name)[0]
	return f

def add_review(firm, tagline, rating, role, salary, pros, cons, estagio):
	r = Review.objects.create(firm=firm, rating=rating)
	r.tagline = tagline
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

