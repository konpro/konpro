# KonPro - Kontrola Prostoty Języka
# narzędzie sprawdza, czy wyrazy w badanym tekście znajdują się na liście słów
# lista słów wygenerowana jest na podstawie korpusu ok. 2700 artykułów z SuperExpressu i Faktu, co gwarantuje prostotę języka
# zależności: psi-toolkit https://github.com/filipg/psi-toolkit
# todo: 
# - oznaczanie potencjalnych nazw własnych (wielkie litery poza początkiem zdania: znaleźć początki zdań - oznaczyć - znaleźć pozostałe wielkie litery - otagować)
# - długość zdań - oznaczanie tasiemców
# - Django+JSON

# KonPro - Language Simplicity Controller
# this utility checks if words in the analysed text are on the word list
# the default word list was generated using the corpus of 2700 articles from Polish tabloids SuperExpress and Fakt, which guaranteed simplicity of the language
# dependencies: psi-toolkit https://github.com/filipg/psi-toolkit
# todo: 
# - marking the potential proper names (uppercase outside of the sentence beginning: find sentence beginnings, mark, find  the remaining uppercase letters, tag)
# - sentences length - mark too long ones
# - Django+JSON
