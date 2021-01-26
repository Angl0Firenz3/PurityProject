#Pandora
#P-B/HBSDCS
#Powered by Paraguas Inc.

import sqlite3

import calendar

import nltk

import pendulum

import webbrowser

import msvcrt

import os

import time

import tkinter

import playsound

from nltk.chat.util import Chat, reflections
from gtts import gTTS
from tkinter import Tk 
from tkinter.filedialog import askopenfilename
from sqlite3 import Error
#from datetime import date
#from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from googlesearch import search
#from datetime import time

#Bloque de variables

today = pendulum.now()
timezone = pendulum.timezone("America/Caracas")
lenguaje = 'es'



#Variable para bucles While: S0 = El programa dejara de ejecutarse; S1 = El programa se quedara en la pantalla inicial; S2 = El programa se quedara en la pestaña de ¿Que puedes hacer?

#S3 = Modo Conversacion

active_cl = "S1"

#Bloque de instrucciones dadas por el usuario


while active_cl == "S1":
	print("Hola, En que puedo ayudarte?")
	print()
	print("1. Que puedes hacer?")
	print("2. Dime la hora")
	
	print()

	opcion = int(input("Opcion Deseada: "))

	if opcion == 1:
		os.system("cls")
		active_cl = "S2"
		while active_cl == "S2":
			print("Actualmente puedo realizar las siguientes acciones:")
			print()
			print("1. Decirte la fecha y hora actual")
			print("2. Mostrarte el calendario de este año")
			print("3. Probar el TTS de google")
			print("4. Volver a la pantalla inicial")
			print()
			opcion = int(input("Opcion Deseada: "))
			print()

			if opcion == 1:
				print()
				print("La fecha y hora exacta actual es: ", today, "Aproximadamente")
				print()
				print("Presione cualquier tecla para continuar. ")
				msvcrt.getch()
				time.sleep(2)
				os.system("cls")

			elif opcion == 2:
				print("Este es el calendario del 2021, suerte!")
				print()
				cal = calendar.TextCalendar(calendar.SUNDAY)
				print(cal.formatyear(2021, 2, 1, 1, 3))
				print("Presione cualquier tecla para continuar. ")
				msvcrt.getch()
				time.sleep(2)

			elif opcion == 3:
				texto = input("Que quieres que diga pandora?: ")
			

				audio = gTTS(text = texto, lang = lenguaje, slow = False)
				audio.save('audio.mp3')

				playsound.playsound('audio.mp3')
				os.system("cls")

			elif opcion == 4:
				print()
				active_cl = "S1"
				os.system("cls")

			else:
				print("Esta opcion no es valida, vuelva a intentarlo")
				msvcrt.getch()
				os.system("cls")

	elif opcion == 2:

		print("La fecha y hora actual es:",today,"Aproximadamente")
		
		msvcrt.getch()
		os.system("cls")