#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from voxpop.models import Review

class ReviewForm(forms.ModelForm):
	tagline = forms.CharField(max_length=128, help_text="Descreva a sua experiência numa frase")
	rating = forms.IntegerField()
	role = forms.CharField(max_length=128, help_text="Qual a sua posição na sociedade?")
	salary = forms.IntegerField(help_text="Quanto ganha por mês?")
	pros = forms.CharField(max_length=300, help_text="Good stuff") # test/change this
	cons = forms.CharField(max_length=300, help_text="Bad stuff")
	estagio = forms.CharField(max_length=300, help_text="notas sobre o estágio")

	class Meta:
		model = Review
		exclude = ('firm',)