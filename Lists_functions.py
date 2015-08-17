#!/usr/bin/python
#-*- coding: utf-8-*-
#
# Autor: Victor Roig 
# Data: 06/03/2013
# Versio:1
# ENUNCIAT: FUNCIONS PER LLISTES: 
#	funcio list_str_to_list_int()(donada una llista de arguments 
#	caracters separats per espais, LA TRANSFORMA EN 
#		una llista de numeros int. /FLOAT & QUE RETORNA FALSE SI NO POT.
	#	ESPECIFICACIONS:
	#entrada : llista de cadenes ("2","2.3","-01")
	#sortida : BOOLEANA & MODIFICA LA LLISTA STR A LLISTA INT /FLOAT (2,23,01)
	
	# funcio maximNombres()
	# funcio ParellsNums()
	# FUNCIO ParellsPos()


#### FUNCIO enter
def esSencer(cadena):
	'''funcio que Llegueix un nombre, i si es enter torna TRUE, sino, FALSE.
	ESPECIFICACIONS:La entrada caracter, 
					la sortida booleana.
	
	'''
	a = float(cadena)
	return int(a) == float(a)

#### FUNCIO real
def real(cadena):
	'''digui si una cadena és un nombre real (True) o no (False)
	Los números reales son los que tienen decimales.
	ESPECIFICACIONS:La entrada ha de ser real, 
					la sortida booleana.
	
	'''
	return str(cadena) == str(float(cadena))
	
# FUNCIO list_str_to_list_int()
def list_str_to_list_int(cadenes):
	''' fer funcio que donada una llista de caracters
	, LA TRANSFORMA EN una llista de numeros int./float
	i QUE RETORNA FALSE SI NO POT.(.2  False)
	ESPECIFICACIONS:
	entrada : llista de cadenes ("2","2.3","01")
	sortida : BOOLEANA'''

	lletres="abcçdefghijklmnñopqrstuvwxyzABCÇDEFGHIJKLMNÑOPQRSTUVWXYZ"
	for pos in range(0,len(cadenes)):
		if cadenes[pos] in lletres or not real(cadenes[pos]) and not esSencer(cadenes[pos]):
			return False
		# si es enter:
		if esSencer(cadenes[pos]):
			cadenes[pos]=int(cadenes[pos])
		# si es float:
		if real(cadenes[pos]):
			cadenes[pos]=float(cadenes[pos])

	return True
	
# FUNCIO maximNombres()
def maximNombres(llistaEnters):
	'''funcio que mostri el màxim dels ENTERS/floats
	en: lllista d'enters/floats no buida
	sor:enter/float
	'''
	maxim=llistaEnters[0]
	for elem in llistaEnters:
		if elem >  maxim:
			maxim = elem
	return maxim
	
# funcio f1(a)
def f1(a):
	'''
	'''
	a = a+1
	return
	
# funcio f2(a)
def f2(a):
	'''
	'''
	a[0] = a[0]+1
	return
	
# FUNCIO ParellsNums()
def ParellsNums(llistaCar):
	''' donada una llista de caracters(sys.argv) entrada per argument,
	#  crear una llista numerica, cambiant els parells per ceros, i mostrarla.
	# ESPECIFICACIONS:entrada llista de cadenes ("1,2,3,4,5,6,7,8")
	#               sortida : LLISTA DE cadenes  (1,0,3,0,5,0,7,0))'''
	
	# passem a ints
	llistaInt=list_str_to_list_int(llistaCar)
	
	# substituir els parells per ceros
	comt=0
	for elem in llistaInt:
		if elem % 2 == 0:
			del llistaInt[comt]
			llistaInt.insert(comt,0)
		comt += 1
	
	return llistaInt
		
######	FUNCIO parellspos()
def ParellsPos(llistaCar):
	''' donada una llista de caracters(sys.argv) entrada per argument,
#  crear una llista numerica, cambiant els de posició parells per ceros, i mostrarla.
# ESPECIFICACIONS:entrada llista de cadenes ("1,2,3,4,5,6,7,8")
#               sortida : LLISTA DE cadenes  (0,2,0,4,0,6,0,8)'''

	# passem a ints
	llistaInt=modul_llistes.list_str_to_list_int(llistaCar)
	
	# substituir els parells per ceros
	for pos in range(0,len(llistaInt)):
	    if pos % 2 == 0:
			del llistaInt[pos]
			llistaInt.insert(pos,0)
	return llistaInt
	
########################TESTS DRIVERS
if __name__=='__main__':
	#b=5
	#f1(5)
	#print f1(b)
	#print "b:",b

	#b=[5]
	#print "b:",b
	#print f2(b)
	#print "b:",b

## testdrive list_str_to_list_int
	numeros=["2","4.4","4.5","4"]
	print "numeros avans=",numeros
	print list_str_to_list_int(numeros) # [2, 4, 5, 64]
	print "numeros despres=",numeros
	
	#print list_str_to_list_int([2,4,5,66,4,3,2,1]) # [2, 4, 5, 66, 4, 3, 2, 1]
	print list_str_to_list_int(["2","-4","5","64"]) # [2, -4, 5, 64]
	print list_str_to_list_int(["2","-4","a","64"]) #
	#print list_str_to_list_int(2,4,5,66,4,3,2,1) TypeError: list_str_to_list_int() takes exactly 1 argument (8 given)
	#print list_str_to_list_int("245644321") # [245644321]
	#print list_str_to_list_int("2 4 5 64 4 3 2 1") # ValueError: invalid literal for int() with base 10: '2 4 5 64 4 3 2 1'
	#print list_str_to_list_int("2,4,5,66,4,3,2,1") #[2, 4, 5, 66, 4, 3, 2, 1]######
	#print list_str_to_list_int("") # ValueError: invalid literal for int() with base 10: ''
	# print list_str_to_list_int(0) TypeError: 'int' object is not iterable
	print list_str_to_list_int("0")#[0]
	print list_str_to_list_int("01")#[1]
	print list_str_to_list_int("01a")#ValueError: invalid literal for int() with base 10: '01a'
	print list_str_to_list_int("0,1,2")#[0, 1, 2]
	# print list_str_to_list_int(a) NameError: name 'a' is not defined
	#print list_str_to_list_int("a")#
	#print list_str_to_list_int(",")#ValueError: invalid literal for int() with base 10: ''
	#print list_str_to_list_int(,) 
	#print list_str_to_list_int(,)
	#				 ^
	#SyntaxError: invalid syntax
	
## testdrive ParellsPos
##	print ParellsPos(2,4,5,66,4,3,2,1) TypeError: list_str_to_list_int() takes exactly 1 argument (8 given)
##	print ParellsPos("245644321") # TypeError: 'str' object doesn't support item deletion
	##print ParellsPos("2 4 5 64 4 3 2 1") # ValueError: invalid literal for int() with base 10: '2 4 5 64 4 3 2 1'
	#print ParellsNums("2,4,5,66,4,3,2,1") #[0, 0, 5, 0, 0, 3, 0, 1]######
	#print ParellsNums("1,2,3,4,5,6,7,8") # [1, 0, 3, 0, 5, 0, 7, 0]
	##print ParellsPos("") # ValueError: invalid literal for int() with base 10: ''
	## print ParellsPos(0) TypeError: 'int' object is not iterable
	#print ParellsNums("0")#[0]
	#print ParellsNums("01")#[0]
	##print ParellsPos("01a")#ValueError: invalid literal for int() with base 10: '01a'
	#print ParellsNums("0,1,2")#[0, 1, 0]
	## print ParellsPos(a) NameError: name 'a' is not defined
	##print ParellsPos("a")#
	##print ParellsPos(",")#ValueError: invalid literal for int() with base 10: ''
	##print ParellsPos(,) 
	##print ParellsPos(,)
	##				 ^
	##SyntaxError: invalid syntax
	
## testdrive ParellsPos
#if __name__=='__main__':
	##print ParellsPos(2,4,5,66,4,3,2,1) TypeError: list_str_to_list_int() takes exactly 1 argument (8 given)
##	print ParellsPos("245644321") # TypeError: 'str' object doesn't support item deletion
	##print ParellsPos("2 4 5 64 4 3 2 1") # ValueError: invalid literal for int() with base 10: '2 4 5 64 4 3 2 1'
	#print ParellsPos("2,4,5,66,4,3,2,1") #[0, 4, 0, 66, 0, 3, 0, 1]######
	#print ParellsPos("1,2,3,4,5,6,7,8") # [0, 2, 0, 4, 0, 6, 0, 8]
	##print ParellsPos("") # ValueError: invalid literal for int() with base 10: ''
	## print ParellsPos(0) TypeError: 'int' object is not iterable
	#print ParellsPos("0")#[0]
	#print ParellsPos("01")#[0]
	##print ParellsPos("01a")#ValueError: invalid literal for int() with base 10: '01a'
	#print ParellsPos("0,1,2")#[0, 1, 0]
	## print ParellsPos(a) NameError: name 'a' is not defined
	##print ParellsPos("a")#
	##print ParellsPos(",")#ValueError: invalid literal for int() with base 10: ''
	##print ParellsPos(,) 
	##print ParellsPos(,)
	##				 ^
	##SyntaxError: invalid syntax
	
########################TESTS DRIVERS
if __name__=='__main__':
	print maximNombres([1,2,3,4])
