#!/usr/bin/python
#-*- coding: utf-8-*-
# Autor: Victor Roig 
# Data: 17/03/2013
# Versio:1
# ENUNCIAT:programa que donada una IP en format decimal i la seva 
#			MASCARA en format octal, mostri:
#	ip en binari
# 	1-CLASSE
#	-tipus
#	-mascara
#	2-BITS DE hosts i de XARXA, BASANT-SE EN LA CLASSE.
# 	3-ÉS UNA IP VÀLIDA? (MOSTRAR TIPUS)
# 	-en format binari i decimal:
#		4-IP ADREÇA DE XARXA,
#		5-IP ADREÇA DE BROADCAST,
#		6-la MASCARA,
#		7-NUMERO DE HOSTS POSSIBLES PER XARXA EN FORMAT bits, POTENCIA Y NORMAL.
# 		8-RANG DE IP HOSTS POSIBLES de la xarxa sencera

# IMPORTS
import sys
from modul_ip import *

# COS DEL PROGRAMA
# DESCARTAR CAS ERROR D'ARGUMENTS
# VALIDAR NUM ARGUMENTS = 2
if len(sys.argv) != 3:
	print "ERROR:numero d'arguments incorrecte"
	print "Usage: prog IP MASC (IP en decimal, 4 enters positius separats per PUNTS)"
	print "			i la MASC com 1 enter (2 A 30): prog 126.23.7.0 27"
	exit()
	
# LLEGIR LA IP & LA MASC
ipDecimal=sys.argv[1]
mascOctal=int(sys.argv[2])

# VALIDAR LA IP : FER SERVIR LA FUNCIO validaIpdec(CADENA)
if not validaIpdec(ipDecimal):
	print "ERROR: IP incorrecte"
	print "Usage: prog IP (en decimal, 4 enters positius (0-255) separats per punts)"
	exit()

# VALIDAR LA MASCARA 
if mascOctal <= 1 or mascOctal >= 31:
	print "ERROR: MASCARA incorrecte"
	print "Usage: MASC com 1 enter (2 A 30)"
	exit()
	
# CONVERTIR LA IP: FER SERVIR LA FUNCIO ipDecimalBinari(cadena)
ipbinaria=ipDecimalBinari(ipDecimal)

# CALCULAR LA CLASSE i info--> funcions classe_IP(),dades_ip(), mascara()
classe=classe_IPDec_detall(ipDecimal)
tipus=tipus_ip(ipDecimal)
mascara=mascara(mascOctal)

# MOSTRAR LA IP I LA CLASSE i les dades
print "ip binaria:",ipbinaria
print "classe",classe
print "tipus",tipus
print "mascara: ",mascara,mascOctal

# mostrar rang IPs

rangIP(ipDecimal,mascOctal)

