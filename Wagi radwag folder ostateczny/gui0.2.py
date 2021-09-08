import os
import sys
import random
import serial
import time
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import *


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

global new_mass,separated_mass,tare_part
global id_wagi_na_serwerze


while 1:
        a=0

if(len(sys.argv)>1):
        print("Ciąg znaków:")
        print(sys.argv[1])
        if(sys.argv[1]=='-?' or sys.argv[1]=='-help' or sys.argv[1]=='-h'):
                print('Welcome to help file')
                print('by git: MarcinanBabarzynca.')
                print('Algoritm:')
                print('1. Get string of arguments (example): "Waga lewa piecowa^SCALE_ID#123456&PILOT_ID#pilot_jeden|pozX=0|pozY=0"')
                print('2. Split string by "^" as Waga name, "#" as serial question for Waga, "&" as name of external serial controller and "|" as gui position on screen, secound "#" as ')
                print('3. Start serial comunicator for Waga and ask question to Waga')
                print('4. If response is incorrect display message that there is other response or no response at all')
                print('5. Start another serial comunicator for external controller and ask question for name')
                print('6. If response is incorrect display message that there is other response or no response at all')
                print('7. If both succeed --> Start gui, set name')
        if('^' in sys.argv[1]):
                window_title = sys.argv[1].split('^')
                window_title = window_title[0]
                print('Name of Waga: "'+window_title+'"')
        else:
                print('Błędne argumenty podane podczas startu programu wpisz -h aby otrzymać pomoc')

        if('SCALE_ID#' in sys.argv[1]):
                scale_id = sys.argv[1].split('SCALE_ID#')
                scale_id = scale_id[1].split('&')
                scale_id=scale_id[0]
                print('Identyfikator wagi: "'+scale_id+ '"')
        else:
                print('Błędne argumenty podane podczas startu programu wpisz -h aby otrzymać pomoc')

        if('PILOT_ID#' in sys.argv[1]):
                pilot_id = sys.argv[1].split('PILOT_ID#')
                pilot_id = pilot_id[1].split('|')
                pilot_id = pilot_id[0]
                print('Identyfikator pilota użytego do tego urządzenia: "'+pilot_id+ '"')
        else:
                print('Błędne argumenty podane podczas startu programu wpisz -h aby otrzymać pomoc')

        exit()




window_title="Tytuł okienka"

#uchwyt pilota
#tu jest fajne ustawienie timeoutu. W sekundach... czyli po jednej sekundzie zwróci wartość lub 0 jeżeli się nie uda odebrać danych.
#można ustawić na 0. to wtedy otrzymamy ostatni bufor.
scale = serial.Serial(
    port='COM6',
    baudrate=9600,
    timeout=0.5
)

#uchwyt pilota
pilot = serial.Serial(
    port='COM14',
    baudrate=9600,
    timeout=0.5
)


root = tk.Tk()
id_wagi_na_serwerze = IntVar(root,name="id_wagi_na_serwerze",value=9)
adres_serwera_i_skryptu = StringVar(root, name="adres_serwera_i_skryptu", value="localhost/test/insert.php")
#?nazwa=9&dane=1213
new_mass = StringVar(root, name="new_mass", value ="Brak danych")
sended_mass = StringVar(root,name="sended_mass",value = "0")
tare_part = StringVar(root,name="tare_part",value="0")
p1 = PhotoImage(file = 'ikona_wag.png')
root.iconphoto(False, p1)
#root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png'))
#root.iconbitmap('/ikona-wag.ico')


def update_mass():
        #tu będzie obsługa serial portu
        #new_mass = (str(random.randint(13123,1231313))+ " g")
        root.setvar("new_mass",value = serial_read_line(scale))
        serial_clear_read_buffer(scale)
        pilot_message = serial_read_line(pilot)
        #(text=root.getvar(name="new_mass"))
        if(tare_part.get()=="1"):
                serial_write(scale,"C1\r\n")
                tare_part.set(value="0")
                stan_wagi.config(text="Wytarowano")
        if(pilot_message ==(b't\r\n') or pilot_message ==('t')):
                print("Wysyłam tarowanie do wagi")
                #tare_btnClickFunction()
                serial_write(scale,"T\r\n")
                tare_change_text()
                tare_part.set(value="1")
                #masa.after(500, cd_of_tare)
                #serial_write(scale,"C1\r\n")
        if(pilot_message ==(b'w\r\n') or pilot_message ==('w')):
                print("Staram się wysłać wagę do serwera")
                send_btnClickFunction()
        if(pilot_message ==(b'c\r\n') or pilot_message ==('c')):
                print("Wysyłam ujemną wagę do serwera")
                minus_send_btnClickFunction()
        masa.config(text=root.getvar(name="new_mass"))#root.getvar(name="new_mass"))
        
        masa.after(500, update_mass)
        

def check_server_connection():
        r = requests.get('http://localhost/test/key.php?key=keykeykey')
        if(r.text == "keykeykey"):
                stan_wagi.config(text="SERWER OK")
        else:
                stan_wagi.config(text="BRAK POŁĄCZENIA Z SERWEREM")
        stan_wagi.after(30000, check_server_connection)


######################################### Funkcje przycisków

#Po kliknięciu wyslij
#1. Wyswietl w konsoli info o tym że coś napisano
#2. Wywietl mase ktora jest ostatnio odczytana i zapisana w zmiennej new_mass
def send_btnClickFunction():
        print(window_title+':send')
        print(new_mass.get())
        print("Rozpoczynam komunikacje z serwerem")
        stan_wagi.config(text="Nadaje")
        #response = requests.get('10.186.10.2/test/insert_dla_wag.php'+ "?data="+str(new_mass))
        #wiadomosc = response.content
        #print(wiadomosc)
        #if(wiadomosc == "zapisalem"):
        #        sended_mass = new_mass
        #        return 1
        #else:
        #       return 0


def tare_btnClickFunction():
        print(window_title+':tare')
        #serial_write(scale,"C1\r\n")
        serial_write(scale,"T\n\r")
        stan_wagi.config(text="Taruje")

def tare_change_text():
        stan_wagi.config(text="Taruje")

def minus_send_btnClickFunction():
        print(window_title+':minus_send')
        print(new_mass.get())
        print("Rozpoczynam komunikacje z serwerem")
        stan_wagi.config(text="Cofam")
        #response = requests.get('10.186.10.2/test/insert_dla_wag.php'+ "?data=-"+new_mass)
        #sended_mass = 0
        #wiadomosc = response.content
        #print(wiadomosc)
        #if(wiadomosc == "zapisalem"):
        #        return 1
        #else:
        #        return 0

#########################################END Funkcje przycisków

# This is the section of code which creates the main window
#root.geometry('317x200')
root.configure(background='#ecf0f1')
root.title(window_title)
root.resizable(False, False)

# This is the section of code which creates the a label
stan_wagi = Label(root, text='Stan wagi', font=('arial', 40, 'normal'),background='#3498db')
stan_wagi.grid(row = 0,column = 0, columnspan=3, sticky="")
############################Funkcje obsługi seriala

#serial_write("COM2","text")
#return 1 on success
#return 0 on fail
def serial_write(obj, string):
        if(obj.write(string.encode('utf-8'))):
                return 1 #on success
        else:
                return 0 #on fail
        
#serial_read("COM2")
#return text on success
#return 0 on fail.
#def serial_read(chosen_port): #return 0 if no data was readed
#        recived_string = chosen_port.readline()
def serial_read_line(obj):
        wiadomosc = obj.readline()
        if(wiadomosc != "b''"):
                if(len(wiadomosc)!=0):
                        print( wiadomosc)
                        wiadomosc = wiadomosc.decode("utf-8") 
                        wiadomosc = wiadomosc.replace('\r','')
                        wiadomosc = wiadomosc.replace('\n','')
                        print('Po odkodowaniu: "'+ wiadomosc+'"')
                        return(wiadomosc)
                
def serial_clear_read_buffer(obj):
        obj.reset_input_buffer()

############################END Funkcje obsługi seriala




# This is the section of code which creates the a label
var = StringVar()
var.set("brak odczytu")
masa = Label(root, text=var, font=('arial', 40, 'normal'),anchor='e',background='#2980b9',fg='#f1c40f')
masa.grid(row = 3,column = 0, columnspan=3, sticky="e")

# Przycisk wysylania --> Komunikuj z serwerem
wyslij_buton = Button(root, text='Wyślij', bg='#bdc3c7', font=('arial', 22, 'normal'), command=send_btnClickFunction)
wyslij_buton.grid(row=5,column=0)
# Przycisk tarowania --> komunikuj do wagi tarowanie
taruj_buton = Button(root, text='Taruj', bg='#bdc3c7', font=('arial', 22, 'normal'), command=tare_btnClickFunction)
taruj_buton.grid(row=5,column=1)
# Przycisk cofania --> Nadaj stary komunikat z minusem xD
cofnij_buton =Button(root, text='Cofnij', bg='#bdc3c7', font=('arial', 22, 'normal'), command=minus_send_btnClickFunction)
cofnij_buton.grid(row=5,column=2)


tare_part.set(value="0")


update_mass()
check_server_connection()
root.mainloop()
