#!/usr/bin/python
#-*- coding: utf-8-*-
# Autor: Victor Roig 
# Data: 12/02/2013
# Versio:1
## ENUNCIAT: Modul de funcions de IPs:

	# binadecimal(ipBinaria) * int(str(cadena),2)
	# decimalabin(ipdecimal)
	# ipBinariDecimal(ipBinaria)
	# ipDecimalBinari(ipdecimal)
	
	# ipDec_to_list(ipdecimal)
	# ipListStr_to_dec(iplistStr)
	
	# validaIpBin(ipBinaria)
	# VALIDA_FORMAT_IpDec(ipdecimal)
	# validaIpdec(ipdecimal)
	
	# classe_IPDec_detall(IPdecimal1)
	# classeIPDec(IPdecimal)
	# classeIPBin(IPbinaria)
	# tipus_ip(IPdecimal1)
	# mascaraIpDec(Ipdecimal)
	
	# ipBinStr_to_pointsStr(ipBinaria)
	# ipXarxa(ipDecStr,mascOctal)
	# ipBroadcast(ipDecStr,mascOctal)
	# mascara(mascOctal)
	# rangIP(ipDecStr,mascOctal)
##################################################################
#### Per passar una cadena binària al seu valor decimal:
####  int(str(cadena),2)
#### o:
## FUNCIO binadecimal()
def binadecimal(binari):
	'''funció que donada una cadena binària calculi el seu valor decimal
	entrada: cadena ceros o uns, 
	sortida: enter positiu o 0'''
	n = len(binari)
	valor = 0
	for bit in binari:
		if bit == "1":
			valor = valor + 2 ** (n-1)
		n -= 1
	return valor

#### FUNCIO  decimal a binari
def decimalabin(decimal):
    """ funció que donada una cadena torna el valor del seu enter en binari
	entrada : enter
	sortida: cadena de 0 / 1"""
    binari1=bin(int(decimal))
    binari=binari1[2:] 	# treiem el "0b" generat per bin()
    return binari
    
#### FUNCIO ipBinariDecimal(ipBinaria)
def ipBinariDecimal(ipBinaria):
	'''funció que donada una IP binària (32 ceros/uns) calculi el seu valor decimal
	entrada: cadena de 32 ceros o uns (IP en format binari valid), 
	sortida: llista de 4 enters que representa una IP en decimal '''
	# tallar l'octet
	# per a cada un dels 4 octets:
	octets_4=""
	ipDecimal=""
	for inici in [0, 8, 16, 24]:
		octets_4=ipBinaria[inici:(inici+8)]
		octetDecimal=int(octets_4,2)
		ipDecimal += str(octetDecimal) + "."
	ipDecimal=ipDecimal[:-1]
	return ipDecimal
	
##### FUNCIO ipDecimalBinari()
def ipDecimalBinari(ipdecimal):
	'''funció que donada una IP en format decimal  
	calculi el seu valor en binari.
	entrada: cadena de caracters , 
	sortida: cadena de 32 ceros o uns '''
	# definir variables
	ipbinaria=""
	octetbinari2=""
	valorBIN=""
	# transformem en llista
	llistadec=ipdecimal.split(".")
	# convertir la ip: FER SERVIR LA FUNCIO decimalabin(cadena)
	for elem in llistadec:
		octetbinari1=decimalabin(int(elem))
		# Afegir ceros que faltin
		octetbinari2=((8-len(octetbinari1))*"0")+octetbinari1
		ipbinaria+=octetbinari2
	return ipbinaria
	
### FUNCIO ipDec_to_list()
def ipDec_to_list(ipdecimal):
	'''funcio que donada una IP en format decimal 
	retorni una llista de 4 enters
	entrada: string fotmat valid "num.num.num.num"
	sortida: llista de 4 enters'''
	return ipdecimal.split(".")
	
### FUNCIO ipListStr_to_dec()
def ipListStr_to_dec(iplistStr):
	'''funcio que donada una llista de 4 Str (IP en format decimal
	['192', '2', '2', '2'] retorni un Str en format IP decimal
	entrada: llista de 4 string (IP en format decimal
	['192', '2', '2', '2'] fotmat valid "num.num.num.num"
	sortida: String fotmat  "num.num.num.num"
	(".").join(llista)'''
	ipDecimal=""
	for octet in iplistStr:
		ipDecimal += octet + "."
	
		
	return ipDecimal[:-1]
	
## FUNCIO VALIDA IP BINARIA
def validaIpBin(ipBinaria):
	'''FUNCIO  que valida el format i el rang d'una cadena, 
	torna True si es 0 o 1 i fa 32
	ENTRADA: cadena de caracters
	SORTIDA: booleana
	'''
	# VALIDEM FORMAT IP 32 BITS 0/1
	for car in ipBinaria:
		# if car not in ['0','1'] 
		# if not (car == '0' or car == '1')
		# if car != '0' and car != "1"
		if car not in "01":
			return False
	if len(ipBinaria) != 32:
		return False
	return True

# FUNCIO VALIDA_FORMAT_IpDec(cadena)
def VALIDA_FORMAT_IpDec(cadena):
	''' donada una cadena, valida si cumpleix el format num.num.num.num,
	retorna True si cumpleix: 1 num + "." + 1 num + "." + 1 num + "." + 1 num
	ENTRADA : cadena str
	SORTIDA : booleana'''
	# 1. VALIDAR FORMAT
	separador = "."
	# 1.2 VALIDAR LONGITUD ( 0.0.0.0 (7) 255.255.255.255 (15)
	# len(data) >= 7 and <= 15 , ok)
	longok = len(cadena) >=7 and len(cadena) <= 15
	if not longok:
		#print "longok entre 7 i 15 false,sortim de la funció",cadena,":",len(cadena)
		return False
#	print "longitud total bien",cadena,":",len(cadena)
	# 1.3 VALIDAR FORMAT 1 num (si es digit, i de lenght 1 a 3)+ 1 separador
	# 1 num (si es digit, i de lenght 1 a 3)+ 1 separador + 1 num (si es 
	# digit, i de lenght 1 a 3)+ 1 separador + 1 num (si es digit, i 
	# de lenght 1 a 3): num + "." + num + "." + num + "." + num
	# rangs valids
	# minims: 0.0.0.0		 total 7, punts 4, digits 4
	# maxims: 255.255.255.255 total 15, punts 4, digits 12
	# long total min - max: 7 - 15
	llista=list(cadena)
	#print "cadena",cadena,llista
	total_digits=0
	cont_punts=0
	cont_digits=0
	anterior = ""
	for elem in llista:
		total_digits += 1
		if elem not in "0123456789.":
			#print "1",elem,"no es valid 0 a 9 o un punt"
			return False
		if elem == "." and anterior == ".":
			#print "punts seguits"
			return False
		if elem == "." and anterior !=".":
			cont_punts += 1
			#print "2 ",elem,"es punt,augmentem conta punts ,validem cont digits i el reiniciem ",cont_punts
			if cont_digits > 3:
				#print "num digits major de 3 , return False"
				return False
			# "reiniciem cont digits" ¿perque no dona error sense comentar?
			# print " timooo"
			cont_digits = 0
			
		else:
			if not elem.isdigit():
				#print "3 ",elem,"no es punt, y no es digit()"
				return False
			cont_digits += 1
			#print "4 ",elem,"es de 1 a 3 digits(), augmentem conta digits i total digits",cont_digits
		anterior = elem
	#print "punts:",cont_punts,"total digits:",total_digits
	longsok = cont_punts == 3 and total_digits >=4 and total_digits <=15
	#print "longituds parcials (4 punts totals  i entre 4 i 12 digits totals=",longsok
	long_totalok = total_digits >= 7 and total_digits <= 15 # aixó ja es valida al punt 1.2, on es millor?
	#print cadena,longsok
	#print cadena,long_totalok
	return longsok and long_totalok

#### FUNCIO validaIpdec(ipdecimal)
def validaIpdec(ipdecimal):
	'''funció que donada una IP decimal en format num.num.num.num,
	valida el RANG de num es vàlid ,retorna True si està dins del rang
	de 0 a 255.
	entrada: ip en format decimal, 4 enters separats per punts
	sortida: booleana
	'''
	# validar el format
	if not VALIDA_FORMAT_IpDec(ipdecimal):
		#print "format invalid"
		return False
	llista=ipdecimal.split(".")
	for elem in llista:
		if not elem.isdigit() or not(int(elem) <= 255 and int(elem) >= 0):
			#print "IP fora de rang",elem
			return False
	return True

#### FUNCIO classe_IPDec_detall(IPdecimal1)
def classe_IPDec_detall(IPdecimal1):
	"""Donada una IP valida en format DECIMAL,(4 nums separats per punts)
	retorna la classe
	ENTRADA: IP valida en format DECIMAL(126.12.4.4)
	SORTIDA: cadena 'Classe A' 'Classe B' 'Classe C' 'Classe D' 
	'['E','Red de  encaminamiento por defecto']"
	'['A','direcciones reservadas o privadas'], ['C','dirección loopback'], 
	'['E','reservades per a usos  futurs'].
	"""
	lletra_classe = ""
	Info_adicional=""
	IPdecimal=IPdecimal1.split(".")
	
	octet1=int(IPdecimal[0])
	octet2=int(IPdecimal[1])
	octet3=int(IPdecimal[2])
	octet4=int(IPdecimal[3])
	
							# Classe A 
				# /8 1.0.0.0 - 127.255.255.255 
	# LLETRA CLASSE
	if octet1 <= 127:
		lletra_classe="A"
	# Info_adicional
	if octet1 == 0:
		Info_adicional="IP de  encaminamiento por defecto."
		# 10.0.0.0 hasta 10.255.255.255 (direcciones reservadas o privadas)
	elif octet1 == 10 :
		Info_adicional="Direccio reservada/privada."
	elif octet1 == 127:
		Info_adicional="Direccio de bucle local o loopback."
		
							# Classe B 
				# /16 128.0.0.0 - 191.255.255.255
	# LLETRA CLASSE
	if octet1 > 127 and octet1 < 192:
		lletra_classe="B"
	# Info_adicional
		# 172.16.0.0 hasta 172.31.0.0 (direcciones reservadas o privadas)
			# 172.16.0.0 hasta 172.31.0.0
	if (octet1 == 172 and octet2 >= 16 and octet2 <= 31):
		Info_adicional="Direccio reservada/privada."
			# 172.32.0.0 hasta 191.255.255.255

							# Classe C 
				# /24 192.0.0.0 - 223.255.255.255
	# LLETRA CLASSE
	if octet1 >= 192 and octet1 < 224:
		lletra_classe="C"
	# Info_adicional
		# 192.168.0.0 hasta 192.168.255.255 (direcciones reservadas o privadas)
			# 192.168.0.0 hasta 192.168.255.255
	if octet1 == 192 and octet2 == 168: 
		Info_adicional="Direccio reservada/privada." #no va be amb accent??
			
			# Classe D /30 224.0.0.0 - 239.255.255.255
	# LLETRA CLASSE
	if octet1 >= 224 and octet1 < 240:
		lletra_classe="D"

			# Classe E 240.0.0.0 - 255.255.255.255
	# LLETRA CLASSE
	if octet1 >= 248 and octet1 < 252:
		lletra_classe="E"
	# Info_adicional
	elif octet1 >= 240 and octet1 <=255:
		lletra_classe="E"
		Info_adicional="Direccio reservada/privada."
	sortida=str(lletra_classe)+"."+str(Info_adicional)
	return sortida
	
#### FUNCIO classeIPDec(IPdecimal)
def classeIPDec(IPdecimal1):
	'''Donada una IP valida en format DECIMAL VALID
	retorna la classe
	ENTRADA: IP valida en format DECIMAL 4 ENTERS SEPAR="."
	SORTIDA: STR 'Classe A','Classe B','Classe C','Classe D''ni A ni B ni C'
	'''
	IPdecimal=IPdecimal1.split(".")
	octet1=int(IPdecimal[0])
	octet2=int(IPdecimal[1])
	octet3=int(IPdecimal[2])
	octet4=int(IPdecimal[3])
	
	classe=""
	if octet1 >= 0 and octet1 < 128: #/ octet1 1-127
		classe="Classe A"
	elif octet1 >= 128 and octet1 < 192: #/ octet 128-191
		classe="Classe B"
	elif octet1 >= 192 and octet1 < 224: #/ octet 192-223
		classe="Classe C"
	elif octet1 >= 224 and octet1 < 240: #/ octet 224-239
		classe="Classe D"
	elif octet1 >= 240 and octet1 < 256: #/ octet 240-255
		classe="Classe E"
	else:
		classe="----"
	return classe
	

#### FUNCIO classeIPBin(IPbinaria)
def classeIPBin(IPBinaria):
	'''Donada una IP valida en format BINARI 
	retorna la classe
	ENTRADA: IP valida en format 32 bits
	SORTIDA: cadena 'A','B','c','ni A ni B ni C'
	'''
	classe=""
	if IPBinaria[0:1] == "0": #/ octet1 Patró "0..."
		classe="Classe A"
	elif IPBinaria[0:2] == "10": #/ octet Patró "1..."
		classe="Classe B"
	elif IPBinaria[0:3] == "110": #/ octet Patró "110.."
		classe="Classe C"
	elif IPBinaria[0:4] == "1110": #/ octet Patró "1110.."
		classe="Classe D"
	elif IPBinaria[0:5] == "11110": #/ octet Patró "11110.."
		classe="Classe E"

	return classe

#### FUNCIO tipus_ip(IPdecimal1)
def tipus_ip(IPdecimal1):
	"""Donada una IP valida en format DECIMAL
	retorna EL TIPUS (BROAD CAST/DE XARXA O HOST)
	ENTRADA: IP valida en format 32 bits
	SORTIDA: cadena 'A','B','c','ni A ni B ni C'
	"""
	tipus = "HOST."
	IPdecimal=IPdecimal1.split(".")
	
	octet1=int(IPdecimal[0])
	octet2=int(IPdecimal[1])
	octet3=int(IPdecimal[2])
	octet4=int(IPdecimal[3])
	
	if octet1 == 255 and octet2 == 255 and octet3 == 255 and octet4 == 255:
		tipus="BROAD CAST."
	if octet1 != 255 and octet2 != 255 and octet3 != 255 and octet4 == 255:
		tipus="BROAD CAST."
	if octet1 != 255 and octet2 != 255 and octet3 == 255 and octet4 == 255:
		tipus="BROAD CAST."
	if octet1 != 255 and octet2 == 255 and octet3 == 255 and octet4 == 255:
		tipus="BROAD CAST."
		
	if octet4 == 0:
		tipus="adreça de XARXA."
	if octet3 == 0 and octet4 == 0:
		tipus="adreça de XARXA."
	if octet2 == 0 and octet3 == 0 and octet4 == 0:
		tipus="adreça de XARXA."
	return tipus
	
# FUNCIO mascaraIpDec()
def mascaraIpDec(Ipdecimal):
	'''funcio que donada una IP en format DECIMAL,
	mostra la mascara en format decimal y "/" octal basantse en la classe
	ESPECIFICACIONS:  
	entrada: IP en format DECIMAL (4 enters positius separats per punts) 
	sortida: cadena de caracters 32 0/1
	'''
	mascara = ""
	IPdecimal1=Ipdecimal.split(".")
	
	octet1=int(IPdecimal1[0])
	octet2=int(IPdecimal1[1])
	octet3=int(IPdecimal1[2])
	octet4=int(IPdecimal1[3])
	
	if octet1 >= 0 and octet1 < 128:
		mascara="8 255.0.0.0"
	elif octet1 >= 128 and octet1 < 192:
		mascara="16 255.255.0.0"
	elif octet1 >= 192 and octet1 < 224:
		mascara="24 255.255.255.0"
	elif octet1 >= 224 and octet1 < 239:
		mascara="30 252.255.255.255"
	elif octet1 >= 240:
		mascara="32 255.255.255.255"
	return mascara

# FUNCIO ipBinStr_to_pointsStr(ipBinaria)
def ipBinStr_to_pointsStr(ipBinaria):
	'''funcio que donada un STR ip en format binari valid
	32 0/1, retorna un str de la ip separada cada 8 bits per 1 punt
	, es a dir, en format de 4 octets separats per un punt
	entrada: str IP format binari 32 0/1
	sortida: str IP format octets separats per punts'''
	ip_octets=""
	count=0
	for car in ipBinaria:
		count += 1
		ip_octets += car 
		if count == 8:
			ip_octets += "."
			count = 0
	return ip_octets[:-1]
	
# funcio ipXarxa(ipDecStr,mascOctal)
def ipXarxa(ipDecStr,mascOctal):
	'''donada un str IP decimal format valid "122.13.14.15",
	y una mascara en Octal, retorna la IP de xarxa
	 basantse en la classe
	entrada: str IP decimal y mascara en octal format valid "122.13.14.15,8"
	sortida: Str IP de xarxa'''
	# transformar ipDecStr a binari
	ipBinaria=ipDecimalBinari(ipDecStr)
	# posar a cero la part de hosts
	mascOctal=int(mascOctal)
	partXarxa=ipBinaria[:mascOctal]
	partHost=ipBinaria[mascOctal:]
	
	partHost='0'*(32-mascOctal)
	# CREAR IP DE XARXA
	ipXarxa=partXarxa+partHost
	ipXarxaDec=ipBinariDecimal(ipXarxa)
	return ipXarxaDec
	
# funcio ipBroadcast(ipDecStr,mascOctal)
def ipBroadcast(ipDecStr,mascOctal):
	'''donada un str IP decimal format valid "122.13.14.15",
	y una mascara en Octal, retorna la IP de xarxa
	 basantse en la classe
	entrada: str IP decimal y mascara en octal format valid "122.13.14.15,8"
	sortida: Str IP de xarxa'''
	# transformar ipDecStr a binari
	ipBinaria=ipDecimalBinari(ipDecStr)
	# posar a UNS la part de hosts
	mascOctal=int(mascOctal)
	partXarxa=ipBinaria[:mascOctal]
	partHost=ipBinaria[mascOctal:]
	partHost='1'*(32-mascOctal)
	# CREAR IP DE XARXA
	ipBroadcast=partXarxa+partHost
	ipBroadcastDec=ipBinariDecimal(ipBroadcast)
	return ipBroadcastDec

# funcio mascara(mascOctal)
def mascara(mascOctal):
	'''donada una mascara en Octal, retorna la IP de xarxa
	 basantse en la classe
	entrada: str mascara en octal format valid de 2 a 30
	sortida: Str IP de xarxa'''
	# posar a UNS la part de xarxa, i a CEROS la part de host
	mascOctal=int(mascOctal)
	
	partXarxa='1'*(mascOctal)
	partHost='0'*(32-mascOctal)
	# CREAR mascara
	mascara=partXarxa+partHost
	mascaraDec=ipBinariDecimal(mascara)
	return mascaraDec
	
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
	ipDec_llista=ipDec_to_list(ipDecStr)
	
	# CALCULAR rang de IPs I MOSTRAR
	ip_octets=ipBinStr_to_pointsStr(ipbinaria)
	print "IP :",ip_octets
		
	# CREAR IP DE XARXA & BROADCAST
	ip_Xarxa=ipXarxa(ipDecStr,mascOctal)
	ip_Broadcast=ipBroadcast(ipDecStr,mascOctal)
	print "Ip nº 1: IP de xarxa:",ip_Xarxa
	print "Ip nº %i: IP de Broadcast: %s "%(hosts_pos,ip_Broadcast)
	
	xarxa_bin=ipDecimalBinari(ip_Xarxa)
	print "xarxa_bin:",xarxa_bin
	broadcast_bin=ipDecimalBinari(ip_Broadcast)
	print "broadcast_bin:",broadcast_bin
	
	# establir limits rang
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
	
	##################### TEST DRIVERS #####################

if __name__=='__main__':

# test driver binadecimal(binari)
	#print '------------test driver binadecimal(binari)------------'
	#jocProves = ("10000001000010100000101100001100", "1000000100001010", "100001010",
				#"0010110", "1", "0", "2", "a", "01", "001", "0001", "00000000000001",
				#"", "100000000000", "11110000", ".")
	#for prova in jocProves:
		#print 'binadecimal("%s"): %s' % (prova, binadecimal(prova))
		
## test driver int(ipBinaria)

	#print '------------test driver int(ipBinaria)------------'
	#jocProves = ("10000001000010100000101100001100", "1000000100001010", "100001010",
				#"0010110", "1", "0", "01", "001", "0001", "00000000000001",
				#"100000000000", "11110000") # error a: "a","",".","2"
	#for prova in jocProves:
		#print 'int(str("%s"),2): %s' % (prova, int(prova,2))

## test driver decimalabin(decimal)
	#print '------------test driver decimalabin(decimal)------------'
	#jocProves = ("123", "1", "2", "3", "4", "5", "6", "7" ,
				#"1", "0", "2", "128", "01", "001", "10", "100",
				#"1000", "10000", "2", "4", "8", "16", "32", "64", "128",
				#"256" ,"512", "1024", "2048", "4096", "8192", "1",
				#"3" ,"7", "15", "31", "63", "127", "255", "511" ,
				#"1023", "2047", "4095", "8191", "128", "192", "224" ,
				#"240", "248", "252", "254")# error en: "","."
	#for prova in jocProves:
		#print 'decimalabin("%s"): %s' % (prova, decimalabin(prova))


### test driver ipBinariDecimal(ipBinaria)
	#print '------------ipBinariDecimal(ipBinaria)------------'
	#jocProves = ("10000001000010100000101100001100",
				#"10001001001010100000101100001101", "11110000110011001111111100010001",
				#)
	#for prova in jocProves:
		#print 'ipBinariDecimal("%s"): %s' % (prova, ipBinariDecimal(prova))		


## test driver ipDecimalBinari(ipdecimal)
	#print '------------test driver ipDecimalBinari(ipdecimal)------------'
	#jocProves = ("1.1.1.1", "1.133.220.122", "1.2.3.4",
				#"0.0.0.0", "255.127.63.31", "1.2.3", "1.2", "1.2.3.4.5.6", 
				#"255.254.253.252" ,	"1", "0", "2", "01", "001", "0001", "00000000000001",
				#"100000000000", "11110000")# error en: "","a","."
	#for prova in jocProves:
		#print 'ipDecimalBinari("%s"): %s' % (prova, ipDecimalBinari(prova))

## test driver ipDec_to_list(ipdecimal)
	#print '------------test driver ipDec_to_list(ipdecimal)------------'
	#jocProves = ("123.133.220.122", "1,133,220.122", "1....2.3.4",
				#"0.0.0.0", "255.127", "3.1.0", ".2.3.4", 
				#".252" ,	"1.", ".0", "-2", "01a", "001", "0001", "00000000000001",
				#"100000000000", "11110000")# error en: "","a","."
	#for prova in jocProves:
		#print 'ipDec_to_list("%s"): %s' % (prova, ipDec_to_list(prova))

## test driver ipListStr_to_dec(iplistStr)
	#print '------------test driver ipListStr_to_dec(iplistStr)------------'
	#jocProves = (('123', '133', '220', '122'), ('255', '13', '128'),('123', '133', '220', '122','2'),
				#['255', '13', '128', '17'])# error en: "","a","."
	#for prova in jocProves:
		#print 'ipListStr_to_dec(%s): %s' % (prova, ipListStr_to_dec(prova))

## test driver validaIpBin(ipBinaria)
	#print '------------test driver validaIpBin(ipBinaria)------------'
	#jocProves = ("10000001000010100000101100001100",
				#"10001001001010100000101100001101", "11110000110011001111111100010001",
				#"0000001000010100000101100001100",
				#"110001001001010100000101100001101", "11110000110011001111111100010002")
	#for prova in jocProves:
		#print 'validaIpBin("%s"): %s' % (prova, validaIpBin(prova))

## test driver VALIDA_FORMAT_IpDec(cadena)
	#print '------------test driver VALIDA_FORMAT_IpDec(cadena)------------'
	#jocProves = ("123.3333.290.122", "123.133.220.122", "123.133.220.a22",
				#"2123.0.0.1", "123..220.122", "123.220.122", "123.256.1.22",
				#"1.1.2.2", "", "a", "0.0.0.0", "255.255.255.255", "256.255.255.255")
	#for prova in jocProves:
		#print 'VALIDA_FORMAT_IpDec("%s"): %s' % (prova, VALIDA_FORMAT_IpDec(prova))
		
## test driver validaIpdec(ipdecimal)
	#print '------------test driver validaIpdec(ipdecimal)------------'
	#jocProves = ("123.3333.290.122", "123.133.220.122", "123.133.220.a22",
				#"2123.0.0.1", "123..220.122", "123.220.122", "123.256.1.22",
				#"1.1.2.2", "", "a", "0.0.0.0", "255.255.255.255",
				#"255.256.255.255", "255.255.256.255", "256.255.255.255")
	#for prova in jocProves:
		#print 'validaIpdec("%s"): %s' % (prova, validaIpdec(prova))
		
## test driver classe_IPDec_detall(IPdecimal1)
	#print '------------test driver classe_IPDec_detall(IPdecimal1)------------'
	#jocProves = ("123.3333.290.0", "172.133.220.255", "10.133.220.122",
				#"223.0.0.1", "224.3.220.122", "244.220.122.2", "0.256.1.22",
				#"1.1.2.2", "0.0.0.0", "255.255.255.255",
				#"255.256.255.255", "255.255.256.255", "256.255.255.255")
	#for prova in jocProves:
		#print 'classe_IPDec_detall("%s"): %s' % (prova, classe_IPDec_detall(prova))
		
## test driver classeIPDec(IPdecimal1)
	#print '------------test driver classeIPDec(IPdecimal1)------------'
	#jocProves = ("127.3333.290.0", "128.133.220.255", "191.133.220.122",
				#"192.0.0.1", "223.3.220.122", "224.220.122.2", "239.256.1.22",
				#"240.1.2.2", "243.0.0.0", "244.255.255.255",
				#"247.253.255.255", "248.255.255.255", "251.255.255.255")
	#for prova in jocProves:
		#print 'classeIPDec("%s"): %s' % (prova, classeIPDec(prova))

## test driver classeIPBin(IPbinaria)
	#print '------------test driver classeIPBin(IPbinaria)------------'
	#jocProves = ("10000001000010100000101100001100",
				#"01001001001010100000101100001101", "11110000110011001111111100010001",
				#"0000001000010100000101100001100",
				#"110001001001010100000101100001101", "1110000110011001111111100010002")
	#for prova in jocProves:
		#print 'classeIPBin("%s"): %s' % (prova, classeIPBin(prova))
		
## test driver tipus_ip(IPdecimal1)
	#print '------------test driver tipus_ip(IPdecimal1)------------'
	#jocProves = ("127.3333.290.0", "128.133.220.255", "191.133.220.122",
				#"192.0.0.1", "223.3.220.122", "224.220.122.2", "239.256.1.22",
				#"240.1.2.2", "243.0.0.0", "244.255.255.255",
				#"247.253.255.255", "248.255.255.255", "251.255.255.255")
	#for prova in jocProves:
		#print 'tipus_ip("%s"): %s' % (prova, tipus_ip(prova))
		
## test driver mascaraIpDec(Ipdecimal)
	#print '------------test driver mascaraIpDec(Ipdecimal)------------'
	#jocProves = ("127.3333.290.0", "128.133.220.255", "191.133.220.122",
				#"192.0.0.1", "223.3.220.122", "224.220.122.2", "239.256.1.22",
				#"240.1.2.2", "243.0.0.0", "244.255.255.255",
				#"247.253.255.255", "248.255.255.255", "251.255.255.255")
	#for prova in jocProves:
		#print 'mascaraIpDec("%s"): %s' % (prova, mascaraIpDec(prova))

## test driver ipBinStr_to_pointsStr(ipBinaria)
	#print '------------test driver ipBinStr_to_pointsStr(ipBinaria)------------'
	#jocProves = ("10000001000010100000101100001100",
				#"01001001001010100000101100001101", "11110000110011001111111100010001",
				#"0000001000010100000101100001100",
				#"110001001001010100000101100001101", "1110000110011001111111100010002")
	#for prova in jocProves:
		#print 'ipBinStr_to_pointsStr("%s"): %s' % (prova, ipBinStr_to_pointsStr(prova))

### test driver ipXarxa(ipDecStr,mascOctal)
	#print '------------test driver ipXarxa(ipDecStr,mascOctal)------------'
	#masc=28
	#jocProves = ("127.122.234.8", "128.133.220.255", "191.133.220.122")
	#for prova in jocProves:
		#print 'ipXarxa %s/%s: %s' % (prova, masc, ipXarxa(prova,masc))

### test driver ipBroadcast(ipDecStr,mascOctal)
	#print '------------test driver ipBroadcast(ipDecStr,mascOctal)------------'
	#masc=28
	#jocProves = ("127.122.234.8", "128.133.220.255", "191.133.220.122")
	#for prova in jocProves:
		#print 'ipBroadcast %s/%s: %s' % (prova, masc, ipBroadcast(prova,masc))	

### test driver mascara(mascOctal)
	#print '------------test driver mascara(ipDecStr,mascOctal)------------'
	#jocProves = ("18", "28", "24", "30", "25", "26", "27", "29")
	#for prova in jocProves:
		#print 'mascara /%s: %s' % (prova, mascara(prova))	

## test driver rangIP(ipDecStr,mascOctal)
	print '------------test driver rangIP(ipDecStr,mascOctal)------------'
	masc=18
	jocProves = ("127.122.234.8", "128.133.220.255", "191.133.220.122")
	for prova in jocProves:
		rangIP(prova,masc)
