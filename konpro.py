#!/usr/bin/python
# -*- coding: utf-8 -*-
# KonPro - Kontrola Prostoty Języka
# zależności: psi-toolkit https://github.com/filipg/psi-toolkit
# todo: 
# - oznaczanie potencjalnych nazw własnych (wielkie litery poza początkiem zdania: znaleźć początki zdań - oznaczyć - znaleźć pozostałe wielkie litery - otagować)
# - długość zdań - oznaczanie tasiemców
# - Django+JSON
import PSIToolkit
import re

# import wordlist 
# tutaj: 
f = open('wordlist.txt', 'r+')
lista = f.read()

input = """Gdy w 1920 doszło do podziału miasta na część polską (Cieszyn) i czechosłowacką (Czeski Cieszyn), tramwaj kursował bez zmian, lecz wzmożone kontrole na moście granicznym uniemożliwiały płynną komunikację. 2 kwietnia 1921 postanowiono zlikwidować linię tramwajową, a tabor sprzedano do Łodzi, gdzie najdłużej (do 1959 – jako doczepny) kursował wagon nr 4. Do dziś w Cieszynie zachował się budynek zajezdni oraz rozetki do zawieszania sieci trakcyjnej."""

# prepare input and output strings - mark newlines in input, mark proper names (to be corrected)
input = re.sub(r'\n', ' <LINEBREAK> ', input)
output = re.sub(r'(^|\.)(| )([A-ZĄĆĘŁŃÓŚŹŻ])', '#\2\3', input)

# split output string, initialise lemmatiser
output = input.split(' ')
lemmatiser = PSIToolkit.PipeRunner('lamerlemma --lang pl ! simple-writer --tags lemma')
input = re.sub(r'[\.,;/?!()]','', input)

# mark unknown words
i = 0
unknownWordsNo = 0
for word in input.split(' '):
	lemmatised = lemmatiser.run(word)
	lemmatised = lemmatised.lower()
# convert newlines to XHTML tags in output
	if word == '<LINEBREAK>':
		output[i] = '<br />'
# don't mark numerals as unknown
	elif re.search(r'[0-9\-\.]', word):
		output[i] = output[i]
#	elif lemmatised == '\n' and word != '<LINEBREAK>':
#		output[i] = ('<span class="compl">' + output[i] + '</span>')
#		unknownWordsNo += 1
	else:
# procedure if the word is ambiguous for the lemmatiser
		if '|' in lemmatised:
			a = lemmatised.split('|')
			a[-1] = a[-1][:-1]
			unknown = True
# check if in the list
			for b in a:
				if b in lista:
					unknown = False
			if unknown == True:
# look for numerals
				if re.search(r'[0-9\-\.]', word):
					output[i] = output[i]
				else:
# mark as unknown, increment unknown words no.
					output[i] = ('<span class="compl">' + output[i] + '</span>')
					unknownWordsNo += 1
		else: 	
# procedure if the word is unambiguous for the lemmatiser
			a = lemmatised[:-1]
# look for numerals
			if re.search(r'[0-9\-\.]', word):
				output[i] = output[i]
# mark as unknown, increment unknown words no.
			elif (a not in lista) and (a != ''): 
				output[i] = ('<span class="compl">' + output[i] + '</span>')
				unknownWordsNo += 1
	i += 1

# clean the output of empty unknown word tags
finalOutput = []
for element in output:
	if element != '<span class="compl"></span>':
		finalOutput.append(element)

# calculate unknown words ratio
print 'udział słów spoza listy: ' + str((float(unknownWordsNo) / float(len(finalOutput))) * 100.0) + '%'
# print output
print ' '.join(finalOutput)
