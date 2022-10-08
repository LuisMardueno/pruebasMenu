"""
Programador: Luis Mardueno
Instituto Tecnologico de Tijuana
Prototipo de pruebas de menu con microcontrolador Pi Pico W
y como muestra del menu en una pantalla oled ssd1306

Notas:
Revisar la forma de evaluar la funcion de switch
la variable opcion es una sumatoria de los valores de los
botones con multiplos (boton * N)

hace falta hacer mas pruebas con el tamaño de letra para
la pantalla oled.
"""
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C #Libreria: ssd1306 module for MicroPython Author: Stefan Lehmann
from oled import Write #Libreria: micropython-oled Author: Yeison Cardona
from oled.fonts import ubuntu_mono_15 
import utime

WIDTH=128
HEIGHT=64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000) #definicion de los pines de comunicacion con la pantalla
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) #Ajuste del tamaño de la pantalla
write10 = Write(oled, ubuntu_mono_15) #definicion de la fuente para la escritura

#Asignacion de los pines de los botones
botonR = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
botonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
botonV = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
botonB = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
opcion = (botonR.value()*2)+(botonA.value()*3)+(botonV.value()*4)+(botonB.value()*5)

while True:#Ciclo infinito
    oled.fill(0) 
    oled.show #limpieza de pantalla
    
    oled.text("Menu de pruebas: ",0,0)
    write10.text("Rojo "+str(botonR.value()*2),0,20)
    write10.text("Amar "+str(botonA.value()*3),0,40)
    write10.text("Verde "+str(botonV.value()*4),60,20)
    write10.text("Azul "+str(botonB.value()*5),60,40)
    oled.show() #Muestra de menu
    opcion = (botonR.value()*2)+(botonA.value()*3)+(botonV.value()*4)+(botonB.value()*5)
    

    def switch(opcion): #Definicion de la funcion de switch, en micropython parece que no hay funcion switch case
        if opcion == 2:
            oled.fill(0)
            oled.text("ROJO",50,20)
            oled.show()
            utime.sleep(1)
            return "Opcion 2"
        elif opcion == 3:
            oled.fill(0)
            oled.text("Amarillo",35,20)
            oled.show()
            utime.sleep(1)
            return "Opcion 3"
        elif opcion == 4:
            oled.fill(0)
            oled.text("Verde",45,20)
            oled.show()
            utime.sleep(1)
            return "Opcion 4"
        elif opcion == 5:
            oled.fill(0)
            oled.text("Azul",50,20)
            oled.show()
            utime.sleep(1)
            return "Opcion 5"
        else:
            return "else"
            
    switch(opcion) #inicio de la funcion de menu con la entrada de la sumatoria de los valores de los botones