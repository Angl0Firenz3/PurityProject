#Purity-Core
#P-B/HBSDCS
#Powered by Vent-Dev
#Original Code By Diego Mendoza

#import sqlite3

import calendar

#import math

#import nltk

#import pendulum

#import webbrowser

import msvcrt

import os

import uuid

import time

#import tkinter

import playsound

#import subprocess

#import speech_recognition

#import tkinter.messagebox

#from nltk.chat.util import Chat, reflections
from gtts import gTTS
#from tkinter import *
#from tkinter import Tk 
#from tkinter.filedialog import askopenfilename
#from sqlite3 import Error
from os import remove
#Nota mental: cambiar a pendulum
#from datetime import date
from datetime import datetime
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from googlesearch import search
#from datetime import time

#Bloque de variables 
today = datetime.now()
lenguaje = 'es'
menu_loop = True
voice_out = str(uuid.uuid4()) + ".mp3"


try:

	def menu_principal():


		while menu_loop == True:
			print("Hola, En que puedo ayudarte?")
			print()
			print("1. Decirte la fecha y hora actual")
			print("2. Mostrarte el calendario de este año")
			print("3. Probar el TTS de google")
			print("4. Realizar operaciones matematicas")
			print("5. Realizar una busqueda en internet")
			print()
			opcion = int(input("Opcion Deseada: "))
			print()




			if opcion == 1:

				def mostrar_hora():

					print()
					print("La fecha y hora exacta actual es: ", today, "Aproximadamente")
					print()
					print("Presione cualquier tecla para continuar. ")
					msvcrt.getch()
					time.sleep(2)
					os.system("cls")

				print(mostrar_hora())

			elif opcion == 2:

				def mostrar_calendario():

					print("Este es el calendario del 2021, suerte!")
					print()
					cal = calendar.TextCalendar(calendar.SUNDAY)
					print(cal.formatyear(2021, 2, 1, 1, 3))
					print("Presione cualquier tecla para continuar. ")
					msvcrt.getch()
					time.sleep(2)

				print(mostrar_calendario())

			elif opcion == 3:

				def prueba_tts():

					texto = input("Que quieres que diga google?: ")
					audio = gTTS(text = texto, lang = lenguaje, slow = False)
					audio.save(voice_out)
					playsound.playsound(voice_out)
					remove(voice_out)
					os.system("cls")

				print(prueba_tts())

			elif opcion == 4:

					os.system("cls")
					def calc():

						print("Por favor seleccione una operacion")
						print("(1) Suma")
						print("(2) Resta")
						print("(3) Multiplicacion")
						print("(4) Division")
						print("(5) Volver al menu principal")

						calc_opc = int(input("Selecione Opcion: "))

						while (calc_opc >0 and calc_opc <5):

							x = int(input("Ingrese Numero\n"))
							y = int(input("Ingrese Otro Numero\n"))

							if (calc_opc==1):
								print("La Suma es:", x+y)
								calc_opc = int(input("Selecione Opcion: "))

							elif(calc_opc==2):
								print("La Resta es:",x-y)
								calc_opc = int(input("Selecione Opcion: "))
							elif(calc_opc==3):
								print("La Multiplicacion es:",x*y)
								calc_opc = int(input("Selecione Opcion: "))
							elif(calc_opc==4):
								try:
									print("La Division es:", x/y)
									calc_opc = int(input("Selecione Opcion: "))
								except ZeroDivisionError:
									print("No se Permite la Division Entre 0")
									calc_opc = int(input("Selecione Opcion: "))

							elif(calc_opc==5):

								os.system("cls")
								print(menu_principal())

			elif opcion == 5:

				def buscar_google():

					usr_search = input("Termino deseado a buscar: ")

					driver = webdriver.Firefox()
					driver.get("http://www.google.com")
					input_element = driver.find_element_by_name("q")
					input_element.send_keys(usr_search)
					input_element.submit()

				print(buscar_google())
				msvcrt.getch()
				time.sleep(2)
				os.system("cls")



			else:
				print("Esta opcion no es valida, vuelva a intentarlo")
				msvcrt.getch()
				os.system("cls")

		

	print(menu_principal())


except ValueError:
    print("Error = Por favor ingrese un numero valido")
    msvcrt.getch()
    os.system("cls")
    print(menu_principal())
