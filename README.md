<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160643.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160643.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160713.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160713.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160719.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160719.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160725.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160725.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/gui.png"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/gui.png" height="100" width="100" ></a>

# What is this?
Its a python app that is used to controll industrial Radwag scale. It use tkinter gui to display mass obtained by serial communication with scale. User is obligated to use controller connected to usb port to "SEND" result to server, "TARE" the scale and "WITHDRAW" the result from server. 

##  Why You need this?
If You want to send results from your scale directly to MySQL database its now possible. 

## Modules used
- pySerial
- Requests
- time

## How to use?
1. Connect scale to USB port wia R232 --> usb dongle... or DIY one
2. Check if Arduino IDE sees your scale. Try to write "normal" communicates to it first. You need to learn how to speak to your Scale. 
3. Adapt my code. 

### Related
- [Remote controller for this scale](https://github.com/MarcinanBarbarzynca/Pilot-do-komputera-Arduino-NANO "Remote controller for this scale")
- [How to read serial from scale](https://github.com/MarcinanBarbarzynca/Read-two-Arduino-serial-with-PYSerial "How to read serial from scale")
- [Scale emulator](https://github.com/MarcinanBarbarzynca/Emulator-wagi-radwag-arduino "Scale emulator")

#### Contact to me :)
Write 10 mails to p_ir@o2.pl


# BUGS! and how to deal with them
- It works slow. 
- Its crashing when it cannot open serial port
- It need some clearence. 

------------

# Co to jest?
To aplikacja pythonowa kt??ra pozwala na komunikacj?? mi??dzy komputerem, pilotem a wag?? przemys??ow?? Radwaga. U??ywa gui wygenerowanego w Tkinterze i wy??wietla stan odczytany z portu seryjnego wagi. U??ytkownik pomo??e sterowa?? procesami przy u??yciu trzech przycisk??w na dodatkowym pilocie: "WY??LIJ" kt??ry wysy??a stan wagi do serwera z baz?? danych, "TARUJ" kt??ry resetuje komunikacj?? z wag?? i rozkazuje jej odpowiednimi komendami tak aby przywr??ci?? komunikacj?? z komputerem, "COFNIJ" kt??ry cofa ostatnio wys??any wynik do serwera (inaczej wysy??a warto???? ujemn??)

##  Why You need this?
Mo??esz szybko przesy??a?? wyniki z wagi do serwera bazodanowego. Mo??esz budowa?? sobie w??asne makra przy u??yciu mojego kodu. 

## Modu??y u??yte
- pySerial
- Requests
- time

## Jak u??ywa???
1. Pod????cz wag?? do USB komputera. Mo??esz zakupi?? przej??ci??wki RS232 --> usb lub samodzielnie takie co?? wykona??. Ja u??ywam modu????w arduino CH340 i dodatk??w MAX3232
2. Sprawd?? czy waga co?? nadaje. Aby tego dokona?? mo??esz pod????czy?? piny RX i TX do przej??ci??wki MAX3232 lub wykorzysta?? inny spos??b np. u??y?? arduino mega z wieloma portami uart. Nast??pnie wykorzystaj kod pushthru aby pods??uchiwa?? komunikacj?? mi??dzy wag?? a komputerem. Naucz si?? rozmawia?? ze swoj?? wag??.
3. Adaptuj si??

1. Uruchom list_all_ports0.2_pyserial.py. Ten program skanuje dost??pne porty w poszukiwaniu wag i przypisanych do nich pilot??w.
2. Zaczekaj a?? uruchomi si?? okienko wagi. Mo??e to potrwa?? 3*liczba port??w com sekund... czyli w przypadku 8 port??w com b??dzie to trwa??o ok 30 sekund. Czas ten jest mo??na w przysz??o??ci zoptymalizowa??, ale teraz dzia??a wystarczaj??co dobrze. 
3. Je??eli si?? nie uruchamia to przejd?? do procedury naprawiania

- Wy??wietlaj?? si?? okienka z komunikatami o b????dach!

## Jak naprawia???
- Otw??rz wybrany program w edytorze python IDE. Uruchom i sprawd?? co wypisuje ci konsola pythona. Nie usun????em jeszcze wiadomo??ci s??u????cych do debugowania. 
- Uruchom Arduino IDE i sprawd?? co wypisuj?? porty do kt??rych jest podpi??ta waga i pilot. 
- Odpowiednio zmie?? plik ustawienia.txt. Znajduj?? si?? tam pary pilot-waga zapisane z pomoc?? odpowiedniej sekwencji znak??w

## B??dzie jeszcze instrukcja instalacji
1. Postaw element na szalce
2. Zaczekaj a?? masa si?? ustabilizuje
3. Naci??nij odpowiedni przycisk: 
 - Wy??lij -> wysy??a mas?? z szalki do serwera
 - Cofnij -> wysy??a mas?? do serwera, ale z ujemnym znakiem
 - Taruj -> Wysy??a do wagi rozkaz tarowania i pisania bez przerwy w jednostce podstawowej. 

## Powi??zane
- [Kontroler, pilot do wagi](https://github.com/MarcinanBarbarzynca/Pilot-do-komputera-Arduino-NANO "Kontroler, pilot do wagi")
- [Jak zbudowa?? komunikator](https://github.com/MarcinanBarbarzynca/Read-two-Arduino-serial-with-PYSerial "Jak zbudowa?? komunikator")
- [Wagi emulator](https://github.com/MarcinanBarbarzynca/Emulator-wagi-radwag-arduino "Wagi emulator")

#### Contact to me :)
Write 10 mails to p_ir@o2.pl


# BUGS! and how to deal with them
- Dzia??a wolno. Wymaga optymalizacji i czyszczenia bufora odczytu i zapisu.
- Wywala si?? w momencie b????du u??ytkownika i braku portu com.
- Wymaga jeszcze troch?? szlif??w w kodzie. Bo wygl??da on ??le. 
