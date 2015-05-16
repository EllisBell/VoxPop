#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from voxpop.models import Review

class ReviewForm(forms.ModelForm):
	tagline = forms.CharField(max_length=140, help_text="Descreva a sua experiência numa frase", widget=forms.Textarea(attrs={'class': 'rev-box rev-small'}))
	rating = forms.IntegerField(help_text="nota de 1 a 5", widget=forms.NumberInput(attrs={'class': 'rev-box rev-num', 'min': '1', 'max': '5'}))
	role = forms.CharField(max_length=100, help_text="Qual a sua posição na sociedade?", widget=forms.TextInput(attrs={'class': 'rev-box rev-small'}))
	salary = forms.IntegerField(help_text="Quanto ganha por mês (€)?", widget=forms.NumberInput(attrs={'class': 'rev-box rev-num'}))
	pros = forms.CharField(max_length=1000, help_text="Good stuff", widget=forms.Textarea(attrs={'class': 'rev-box rev-big'})) # test/change this
	cons = forms.CharField(max_length=1000, help_text="Bad stuff", widget=forms.Textarea(attrs={'class': 'rev-box rev-big'}))
	estagio = forms.CharField(max_length=1000, help_text="notas sobre o estágio", widget=forms.Textarea(attrs={'class': 'rev-box rev-big'}))

	class Meta:
		model = Review
		exclude = ('firm',)