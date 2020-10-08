import pygame, sys, os, random
from pygame.locals import *
from time import sleep
from pdb import set_trace as st

fps = pygame.time.Clock()
pygame.init()

#Display
pygame.display.set_caption("Tame Elements")
icono = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","icon","man.png"))
pygame.display.set_icon(icono)

#Pantalla
ancho = 1500
alto = 950
pantalla = pygame.display.set_mode((ancho, alto))

#Fuentes
fuente = pygame.font.SysFont(None, 20)
fuente2 = pygame.font.SysFont(None, 50)

#Botones
iniciar_img = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","Menu","iniciar juego.png"))
opciones_img = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","Menu","opciones.png"))
salir_img = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","Menu","salir.png"))
atras_img = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","Menu","atras.png"))
opacidad_img = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","Menu","opacidad.png"))
pasar_turno_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Menu", "turno.png"))
rondas_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Menu", "rondas.png"))

#Imagen de fondo
fondo_img = pygame.image.load(os.path.join(os.path.dirname(__file__),"bin","Menu","fondo.png"))
tablero_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "fondo", "tablero.png"))

#interfaz
turno_jug_1_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "turno jugador 1.png"))
turno_jug_2_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "turno jugador 2.png"))
vencedor_jug_1_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "Vencedor jugador 1.png"))
vencedor_jug_2_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "Vencedor jugador 2.png"))
empate_ronda_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "empate ronda.png"))
ganador_ronda_1_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "ganador ronda 1.png"))
ganador_ronda_2_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "ganador ronda 2.png"))
empate_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "interfaz", "empate.png"))


#Otros elementos del juego
click = False
baraja = []
baraja2 = []

def inicio():
	# TIERRA
	twix_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "TIERRA", "TWIX.png"))
	toshinori_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "TIERRA", "TOSHINORI.png"))
	izales_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "TIERRA", "IZALES.png"))
	dasgar_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "TIERRA", "DASGAR.png"))
	badontom_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "TIERRA", "BADONTOM.png"))

	twix = {"nombre": "twix",
			"ataque": 3,
			"defensa": 5,
			"imagen": twix_img,
			"puntos": 12}
	toshinori = {"nombre": "toshinori",
				 "ataque": 5,
				 "defensa": 3,
				 "imagen": toshinori_img,
				 "puntos": 8}
	izales = {"nombre": "izales",
			  "ataque": 2,
			  "defensa": 6,
			  "imagen": izales_img,
			  "puntos": 20}
	dasgar = {"nombre": "dasgar",
			  "ataque": 6,
			  "defensa": 3,
			  "imagen": dasgar_img,
			  "puntos": 6}
	badontom = {"nombre": "badontom",
				"ataque": 10,
				"defensa": 8,
				"imagen": badontom_img,
				"puntos": 17}

	# AGUA
	miklos_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "AGUA", "MIKLOS.png"))
	thesus_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "AGUA", "THESUS.png"))
	nell_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "AGUA", "NELL.png"))
	petya_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "AGUA", "PETYA.png"))
	theda_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "AGUA", "THEDA.png"))

	miklos = {"nombre": "miklos",
			  "ataque": 2,
			  "defensa": 3,
			  "imagen": miklos_img,
			  "puntos": 10}
	thesus = {"nombre": "thesus",
			  "ataque": 2,
			  "defensa": 7,
			  "imagen": thesus_img,
			  "puntos": 5}
	nell = {"nombre": "nell",
			"ataque": 4,
			"defensa": 3,
			"imagen": nell_img,
			"puntos": 3}
	petya = {"nombre": "petya",
			 "ataque": 7,
			 "defensa": 4,
			 "imagen": petya_img,
			 "puntos":9}
	theda = {"nombre": "theda",
			 "ataque": 9,
			 "defensa": 7,
			 "imagen": theda_img,
			 "puntos": 19}

	# FUEGO
	rimur_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "FUEGO", "RIMUR.png"))
	ahra_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "FUEGO", "AHRA.png"))
	hill_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "FUEGO", "HILL.png"))
	dovros_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "FUEGO", "DOVROS.png"))
	baelpho_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "FUEGO", "BAELPHO.png"))

	rimur = {"nombre": "rimur",
			 "ataque": 4,
			 "defensa": 4,
			 "imagen": rimur_img,
			 "puntos": 14}
	ahra = {"nombre": "ahra",
			"ataque": 4,
			"defensa": 8,
			"imagen": ahra_img,
			"puntos": 7}
	hill = {"nombre": "hill",
			"ataque": 2,
			"defensa": 1,
			"imagen": hill_img,
			"puntos":2}
	dovros = {"nombre": "dovros",
			  "ataque": 5,
			  "defensa": 4,
			  "imagen": dovros_img,
			  "puntos": 8}
	baelpho = {"nombre": "baelpho",
			   "ataque": 8,
			   "defensa": 7,
			   "imagen": baelpho_img,
			   "puntos": 18}

	# ACERO
	ferret_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "ACERO", "FERRET.png"))
	debnya_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "ACERO", "DEBNYA.png"))
	atheod_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "ACERO", "ATHEOD.png"))
	tyra_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "ACERO", "TYRA.png"))
	zero_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "bin", "Cartasimg", "ACERO", "ZERO.png"))

	ferret = {"nombre": "ferret",
			  "ataque": 4,
			  "defensa": 3,
			  "imagen": ferret_img,
			  "puntos": 9}
	debnya = {"nombre": "debnya",
			  "ataque": 3,
			  "defensa": 7,
			  "imagen": debnya_img,
			  "puntos": 6}
	atheod = {"nombre": "atheod",
			  "ataque": 5,
			  "defensa": 2,
			  "imagen": atheod_img,
			  "puntos": 9}
	tyra = {"nombre": "tyra",
			"ataque": 7,
			"defensa": 2,
			"imagen": tyra_img,
			"puntos": 7}
	zero = {"nombre": "zero",
			"ataque": 10,
			"defensa": 7,
			"imagen": zero_img,
			"puntos": 20}

	agua = ([miklos, thesus, nell, petya, theda])

	tierra = ([twix, toshinori, izales, dasgar, badontom])

	fuego = ([rimur, ahra, hill, dovros, baelpho])

	acero = ([ferret, debnya, atheod, tyra, zero])

	# Listado de baraja

	for j in (agua):
		carta_agua = "{} de AGUA".format(j)
		baraja.append(j)
		baraja2.append(j)

	for l in (tierra):
		carta_tierra = "{} de TIERRA".format(l)
		baraja.append(l)
		baraja2.append(l)

	for e in (fuego):
		carta_fuego = "{} de FUEGO".format(e)
		baraja.append(e)
		baraja2.append(e)

	for z in (acero):
		carta_acero = "{} de ACERO".format(z)
		baraja.append(z)
		baraja2.append(z)

	random.shuffle(baraja)  # Barajamos las cartas
	random.shuffle(baraja2)

	cont = 0

	fps = pygame.time.Clock()
	pygame.init()
	pantalla = pygame.display.set_mode((1500, 950))
	

	carta_x = 400
	carta_y = 350

	juego()


# Jugador 1 = el de abajo

# Cartas centrales
posicion_cartas_nuevas = [(334,290),(612,290),(890,290)]
cartas_nuevas = [None,None,None] #Se crea una variable sin un valor especifico
colision_cartas_nuevas = [None,None,None]

# Cartas jugador 1
posicion_cartas_jug_1 = [(335,505),(612,505),(890,505)]
cartas_jug_1 = [None,None,None]
colision_cartas_jug_1 = [None,None,None]

# Cartas jugador 2
posicion_cartas_jug_2 = [(335,100),(611,100),(890,100)]
cartas_jug_2 = [None,None,None]
colision_cartas_jug_2 = [None,None,None]

def asignar_carta_nueva(carta,posicion):
	global cartas_nuevas
	cartas_nuevas[posicion] = carta

def asignar_colision_carta_nueva(colision,posicion):
	global colision_cartas_nuevas
	colision_cartas_nuevas[posicion] = colision

def asignar_carta_jug_1(carta,posicion):
	global cartas_jug_1
	cartas_jug_1[posicion] = carta

def asignar_colision_carta_jug_1(colision,posicion):
	global colision_cartas_jug_1
	colision_cartas_jug_1[posicion] = colision

def asignar_carta_jug_2(carta,posicion):
	global cartas_jug_2
	cartas_jug_2[posicion] = carta

def asignar_colision_carta_jug_2(colision,posicion):
	global colision_cartas_jug_2
	colision_cartas_jug_2[posicion] = colision


estado = "repartiendo_jug_1"

def juego():
	contador_tiempo = 0
	global cartas_nuevas #Global para utilizar las variables en otras funciones
	global colision_cartas_nuevas
	global cartas_jug_1
	global colision_cartas_jug_1
	global cartas_jug_2
	global colision_cartas_jug_2
	global estado
	global pantalla
	global baraja
	global baraja2

	#La ronda comienza en uno
	num_ronda = 1
	puntos_jug_1 = 0
	puntos_jug_2 = 0

	while True:
		opacidad()
		mousex, mousey = pygame.mouse.get_pos()
		pantalla.fill((255, 255, 255))
		pantalla.blit(tablero_img, (0,0))
		# Mostrar cartas

		# Se muestra solo las cartas que existen
		for i in [0,1,2]:
			if cartas_jug_1[i] != None: # Si no hay cartas nuevas son none, entonces si es diferente a none se muestran dichas cartas
				colision_cartas_nuevas[i] = pantalla.blit(cartas_jug_1[i]["imagen"], posicion_cartas_jug_1[i])
		for i in [0,1,2]:
			if cartas_jug_2[i] != None:
				colision_cartas_nuevas[i] = pantalla.blit(cartas_jug_2[i]["imagen"], posicion_cartas_jug_2[i])
		for i in [0,1,2]:
			if len(cartas_nuevas) == 1:
				cartas_nuevas.append(None)
			if len(cartas_nuevas) == 2:
				cartas_nuevas.append(None)
			if cartas_nuevas[i] != None:
				colision_cartas_nuevas[i] = pantalla.blit(cartas_nuevas[i]["imagen"], posicion_cartas_nuevas[i])

		colision_pasar_turno = pantalla.blit(pasar_turno_img,(1130,850))
		colision_rondas = pantalla.blit(rondas_img,(10,10))


		font_pequena = pygame.font.Font(pygame.font.get_default_font(), 30)
		font_grande = pygame.font.Font(pygame.font.get_default_font(), 54)
		pantalla.blit(font_grande.render(str(num_ronda), True, (255,255,255) , pygame.SRCALPHA), (250,19)) 
		pantalla.blit(font_pequena.render("#1:"+str(puntos_jug_1), True, (255,255,255) , pygame.SRCALPHA), (70,465))
		pantalla.blit(font_pequena.render("#2:"+str(puntos_jug_2), True, (255,255,255) , pygame.SRCALPHA), (1320,465))

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				click = True
			if event.type == MOUSEBUTTONUP and event.button == 1:
				click = False
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				menu_principal()


		if estado == "repartiendo_jug_1": #Estado nos sirve para saber en donde se encuentra funcionando el juego
			pantalla.blit(turno_jug_1_img,(10,850))
			# Cartas nuevas
			if len(baraja) == 0:
				# jugador 1 se quedo sin cartas
				estado = "gano_jugador_2"
			else:
				if len(baraja) >= 3:
					cartas_nuevas = [baraja[0],baraja[1],baraja[2]]
					baraja.pop(0)
					baraja.pop(0)
					baraja.pop(0)
				elif len(baraja) == 2:
					cartas_nuevas = [baraja[0],baraja[1],None]
					baraja.pop(0)
					baraja.pop(0)
				elif len(baraja) == 1:
					cartas_nuevas = [baraja[0],None]
					baraja.pop(0)
				estado = "eligiendo_cartas_nuevas_jug_1"

		elif estado == "eligiendo_cartas_nuevas_jug_1":
			pantalla.blit(turno_jug_1_img,(10,850))
			for i in [0,1,2]:
				if colision_cartas_nuevas[i] != None:
					if click == True and colision_cartas_nuevas[i].collidepoint((mousex, mousey)):
						carta_nueva = cartas_nuevas[i]
						cartas_nuevas[i] = None
						colision_cartas_nuevas[i] = None
						agregar_carta_al_jugador(carta_nueva, True)
						sleep(0.2)

			# Click del boton para pasar al siguiente estado/turno
			if click == True and colision_pasar_turno.collidepoint((mousex, mousey)) and cartas_jug_1 != [None,None,None]:
				# Devolvemos al mazo las que no fueron elegidas
				for carta in cartas_nuevas:
					if carta != None:
						baraja.append(carta)
						random.shuffle(baraja)
				sleep(0.2)
				estado = "repartiendo_jug_2"

		elif estado == "repartiendo_jug_2":
			pantalla.blit(turno_jug_2_img,(10,850))

			if len(baraja2) == 0: #Si la baraja del jugador dos es igual a 0, automaticamente gana el jugador 1
				# El jugador se quedo sin cartas
				estado = "gano_jugador_1"
			else:
				if len(baraja2) >= 3:
					cartas_nuevas = [baraja2[0],baraja2[1],baraja2[2]]
					baraja2.pop(0)
					baraja2.pop(0)
					baraja2.pop(0)
				elif len(baraja2) == 2:
					cartas_nuevas = [baraja2[0],baraja2[1],None]
					baraja2.pop(0)
					baraja2.pop(0)
				elif len(baraja2) == 1:
					cartas_nuevas = [baraja2[0],None]
					baraja2.pop(0)
				estado = "eligiendo_cartas_nuevas_jug_2"


		elif estado == "eligiendo_cartas_nuevas_jug_2":
			pantalla.blit(turno_jug_2_img,(10,850))
			for i in [0,1,2]:
				if colision_cartas_nuevas[i] != None:
					if click == True and colision_cartas_nuevas[i].collidepoint((mousex, mousey)):
						carta_nueva = cartas_nuevas[i]
						asignar_carta_nueva(None,i)
						asignar_colision_carta_nueva(None,i)
						agregar_carta_al_jugador(carta_nueva, False)
						sleep(0.2)

			# Boton para pasar al siguiente estado/turno
			if click == True and colision_pasar_turno.collidepoint((mousex, mousey)) and cartas_jug_2 != [None,None,None]:
				# Devolvemos al mazo las que no fueron elegidas
				for carta in cartas_nuevas:
					if carta != None:
						baraja2.append(carta)
						random.shuffle(baraja2)
				cartas_nuevas = [None,None,None]
				sleep(0.2)
				estado = "procesando_ganador_de_ronda"

		elif estado == "procesando_ganador_de_ronda":
			# Pelean las cartas de los jugadores
			# El que gana mas peleas gana la ronda
			# En caso de empate el que puso mas cartas gana la ronda
			peleas_ganadas_jug_1 = 0
			peleas_ganadas_jug_2 = 0

			potencial_puntaje_ganado_jug_1 = 0
			for carta in cartas_jug_1:
				if carta != None:
					potencial_puntaje_ganado_jug_1 += carta["puntos"]

			potencial_puntaje_ganado_jug_2 = 0
			for carta in cartas_jug_2:
				if carta != None:
					potencial_puntaje_ganado_jug_2 += carta["puntos"]

			for i in [0,1,2]:
				# El ganador de la pelea se determina por ataque+defensa
				if cartas_jug_1[i] != None and cartas_jug_2[i] != None:
					ataque_y_defensa_jug_1 = cartas_jug_1[i]["ataque"]+cartas_jug_1[i]["defensa"]
					ataque_y_defensa_jug_2 = cartas_jug_2[i]["ataque"]+cartas_jug_2[i]["defensa"]

					if (ataque_y_defensa_jug_1 > ataque_y_defensa_jug_2):
						peleas_ganadas_jug_1 += 1
						potencial_puntaje_ganado_jug_1 += cartas_jug_2[i]["puntos"]

					elif (ataque_y_defensa_jug_2 > ataque_y_defensa_jug_1):
						peleas_ganadas_jug_2 += 1
						potencial_puntaje_ganado_jug_2 += cartas_jug_1[i]["puntos"]
			

			# El ganador gana los puntos de las cartas que jugo + los puntos de las cartas que mató
			if peleas_ganadas_jug_1 > peleas_ganadas_jug_2:
				# Gano la ronda el jugador 1
				puntos_jug_1 += potencial_puntaje_ganado_jug_1
				estado = "gano_ronda_1"
			elif peleas_ganadas_jug_1 < peleas_ganadas_jug_2:
				# Gano la ronda el jugador 2
				puntos_jug_2 += potencial_puntaje_ganado_jug_2
				estado = "gano_ronda_2"
			else:
				cant_cartas_jug_1 = 0
				for carta in cartas_jug_1:
					if carta != None:
						cant_cartas_jug_1+=1

				cant_cartas_jug_2 = 0
				for carta in cartas_jug_2:
					if carta != None:
						cant_cartas_jug_2+=1

				# Se desempata por quien puso mas cartas
				if cant_cartas_jug_1 > cant_cartas_jug_2:
					puntos_jug_1 += potencial_puntaje_ganado_jug_1
					estado = "gano_ronda_1"
				elif cant_cartas_jug_1 < cant_cartas_jug_2:
					puntos_jug_2 += potencial_puntaje_ganado_jug_2
					estado = "gano_ronda_2"
				else:
					# empate en la ronda
					estado = "empate_ronda"

		#Pantallas finales
		elif estado == "gano_jugador_1":
			pantalla.blit(vencedor_jug_1_img, (0,0))
			pantalla.blit(font_grande.render("Puntuación final:", True, (255,255,255) , pygame.SRCALPHA), (520,830))
			pantalla.blit(font_grande.render("   #1:"+str(puntos_jug_1)+"    |    "+"#2:"+str(puntos_jug_2), True, (255,255,255) , pygame.SRCALPHA), (520,880)) 

		elif estado == "gano_jugador_2":
			pantalla.blit(vencedor_jug_2_img, (0,0))
			pantalla.blit(font_grande.render("Puntuación final:", True, (255,255,255) , pygame.SRCALPHA), (520,830))
			pantalla.blit(font_grande.render("   #1:"+str(puntos_jug_1)+"    |    "+"#2:"+str(puntos_jug_2), True, (255,255,255) , pygame.SRCALPHA), (520,880)) 

		elif estado == "empate":
			pantalla.blit(empate_img, (0,0))
			pantalla.blit(font_grande.render("Puntuación final:", True, (255,255,255) , pygame.SRCALPHA), (520,830))
			pantalla.blit(font_grande.render("   #1:"+str(puntos_jug_1)+"    |    "+"#2:"+str(puntos_jug_2), True, (255,255,255) , pygame.SRCALPHA), (520,880)) 

		elif estado == "gano_ronda_1":
			contador_tiempo += 1
			if contador_tiempo > 65:
				estado = "final_ronda"
				contador_tiempo = 0
			pantalla.blit(ganador_ronda_1_img, (533,420))

		elif estado == "gano_ronda_2":
			contador_tiempo += 1
			if contador_tiempo > 65:
				estado = "final_ronda"
				contador_tiempo = 0
			pantalla.blit(ganador_ronda_2_img, (533,420))

		elif estado == "empate_ronda":
			contador_tiempo += 1
			if contador_tiempo > 65:
				estado = "final_ronda"
				contador_tiempo = 0
			pantalla.blit(empate_ronda_img, (533,420))

		elif estado == "final_ronda":
			cartas_jug_1 = [None,None,None]
			cartas_jug_2 = [None,None,None]
			cartas_nuevas = [None,None,None]
			num_ronda += 1
			estado = "repartiendo_jug_1"
			if num_ronda > 10:
				if puntos_jug_1 > puntos_jug_2:
					estado = "gano_jugador_1"
				elif puntos_jug_1 < puntos_jug_2:
					estado = "gano_jugador_2"
				else:
					estado = "empate"

		pygame.display.update()
		fps.tick(60)

def agregar_carta_al_jugador(carta_nueva, es_jugador_1):
	# Dependiendo de quien juega utilizo esa mano
	if es_jugador_1:
		# Asigno el primer recuadro disponible en la mano del jugador
		posicion_vacia = None
		for i in [2,1,0]:
			if cartas_jug_1[i] == None:
				posicion_vacia = i

		if posicion_vacia == None:
			# No hay posiciones libres
			return
		asignar_carta_jug_1(carta_nueva,posicion_vacia)
	else:
		# Asigno el primer recuadro disponible en la mano del jugador
		posicion_vacia = None
		for i in [2,1,0]:
			if cartas_jug_2[i] == None:
				posicion_vacia = i

		if posicion_vacia == None:
			# No hay posiciones libres
			return
		asignar_carta_jug_2(carta_nueva,posicion_vacia)

def opacidad():
	opacidad = pygame.Surface((1500,950))
	opacidad.fill((0,0,0))
	for alpha in range (300,0):
		opacidad.set_alpha(alpha)
		pantalla.blit(opacidad,(x,y))
		pygame.display.update()
		pygame.time.delay(5)

def dibujar_texto(texto, fuente, color, surface, x, y):
	texto = fuente.render(texto, 1, color)
	texto_rect = texto.get_rect()
	texto_rect.topleft = (x, y)
	surface.blit(texto, texto_rect)

def salir_juego():
	pygame.quit()
	sys.exit()

def menu_opciones():
	cerrar = True
	while cerrar:
		mousex, mousey = pygame.mouse.get_pos()
		pantalla.fill((255,255,255))
		pantalla.blit(fondo_img,(0,0))

		atras = pantalla.blit(atras_img,(ancho/2-130,550))
		if atras.collidepoint((mousex, mousey)):
			pantalla.blit(opacidad_img,(ancho/2-130,550))
			if click:
				cerrar = False

		click = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					cerrar = False
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		fps.tick(60)

# Musica de inicio
musica = pygame.mixer.music.load('musica.mp3')

def menu_principal():

	# Se pone play la musica
	pygame.mixer.music.play(-1, 0.0) #Se reproduce en un bucle infinito e inicia desde el principio la musica
	#Volumen de la musica
	pygame.mixer.music.set_volume(0.02)

	while True:
		click = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		mousex, mousey = pygame.mouse.get_pos()
		pantalla.fill((0, 0, 0))
		pantalla.blit(fondo_img,(0,0))

		iniciar_juego = pantalla.blit(iniciar_img,(ancho/2-130,350))
		opciones = pantalla.blit(opciones_img,(ancho/2-130,450))
		salir = pantalla.blit(salir_img,(ancho/2-130,550))

		if iniciar_juego.collidepoint((mousex, mousey)):
			pantalla.blit(opacidad_img,(ancho/2-130,350))
			if click:
				inicio()

		if opciones.collidepoint((mousex, mousey)):
			pantalla.blit(opacidad_img,(ancho/2-130,450))
			if click:
				menu_opciones()

		if salir.collidepoint((mousex, mousey)):
			pantalla.blit(opacidad_img,(ancho/2-130,550))
			if click:
				salir_juego()

		pygame.display.update()
		fps.tick(60)

menu_principal()