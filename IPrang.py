#!/usr/bin/python
#-*- coding: utf-8-*-
# Autor: Victor Roig 
# Data: 17/03/2013
# Versio:1
# ENUNCIAT:programa que donada una IP en format decimal i la seva 
#			MASCARA en format octal, mostri:
#	
#		4-IP ADREÇA DE XARXA,
#		5-IP ADREÇA DE BROADCAST,
#		6-la MASCARA,
#		7-NUMERO DE HOSTS POSSIBLES PER XARXA EN FORMAT bits, POTENCIA Y NORMAL.
# 		8-RANG DE IP HOSTS POSIBLES de la xarxa sencera

# IMPORTS
import sys
from modul_ip import *

#### funcio rangIP(ipDecStr,mascOctal)
def rangIP(ipDecStr,mascOctal):
	'''donada un str IP decimal format valid "122.13.14.15",
	y una mascara en format Octal, retorna el rang de totes les ip possibles 
	basantse en la mascara, y diu també el tipus de IP(xarxa,host, o b.c)
	entrada: str IP decimal format valid "122.13.14.15" I MASCARA EN OCTAL
	sortida: str INFO + RANG paginat de IPs BINARI DECIMAL TIPUS'''
	# CONVERTIR LA IP: FER SERVIR LA FUNCIO ipDecimalBinari(cadena)
	ipbinaria=ipDecimalBinari(ipDecStr)
	# EXTREURE BITS DE XARXA I DE HOST
	bits_xarxa=int(mascOctal)
	bits_hosts=32-int(mascOctal)
	
	# CALCULAR PORCIO BINARIA XARXA I HOST
	porcio_xarxa=ipbinaria[:bits_xarxa]
	porcio_host=ipbinaria[bits_xarxa:]
	print bits_xarxa," bits de xarxa:",porcio_xarxa
	print bits_hosts," bits per hosts:",porcio_host
	
	# CALCULAR EL NUMERO DE HOSTS
	hosts_pos=2**bits_hosts
	print hosts_pos," IP's possibles - 2 =",hosts_pos-2," hosts."
	
	# CREAR LLISTA DE STR OCTETS IP DECIMAL i mostrar 
	ipDec_llista=ipDec_to_list(ipDecimal)
	
	# CALCULAR rang de IPs I MOSTRAR
	ip_octets=ipBinStr_to_pointsStr(ipbinaria)
	print "IP :",ip_octets
	
	
	# CREAR IP DE XARXA & BROADCAST
	ip_Xarxa=ipXarxa(ipDecimal,mascOctal)
	ip_Broadcast=ipBroadcast(ipDecimal,mascOctal)
	print "Ip nº 1: IP de xarxa:",ip_Xarxa
	print "Ip nº %i: IP de Broadcast: %s "%(hosts_pos,ip_Broadcast)
	
	xarxa_bin=ipDecimalBinari(ip_Xarxa)
	print "xarxa_bin:",xarxa_bin
	broadcast_bin=ipDecimalBinari(ip_Broadcast)
	print "broadcast_bin:",broadcast_bin
	primera_ip=binadecimal(xarxa_bin)
	ultima_ip=binadecimal(broadcast_bin)
	
	# mostrar rang
	print "RANG DE IPS.."
	contador=0
	conta_hosts=0
	punter=10
	raw_input("apreta return per continuar...")

	for ip in range(primera_ip,ultima_ip+1):
		
		# calcular tipus de IP
		if contador==0:
			tag="(IP DE XARXA)"
		elif ip == (ultima_ip):
			tag="(IP DE BROADCAST - DIFUSIÓ)"
		else:
			conta_hosts+=1
			tag="(HOST %i)"%(conta_hosts)
			
		# posar ceros que falten fins 32 bits
		ip_bin1=decimalabin(ip)
		ip_bin2='0'*(32-len(ip_bin1))+ip_bin1
		# passar la ip decimal a binari
		ip_dec=ipBinariDecimal(ip_bin2)
		# printar IPs i tipus
		print ipBinStr_to_pointsStr(ip_bin2),ip_dec,tag
		contador+=1
		
		#if contador % punter == 0:
			#raw_input("apreta return per continuar...")
	
	return 

# LLEGIR LA IP & LA MASC
ipDecimal=sys.argv[1]
mascOctal=int(sys.argv[2])
# printar rang

rangIP(ipDecimal,mascOctal)
