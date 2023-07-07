# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:44:47 2023
@author: Carlos Luco Montofré

Módulo que mantiene el trabajo simulado de una base de dato No Sql implementada
con el uso de diccionarios de Python. Los datos son cargados y descargados por
el objeto Gestor_BD de archivo texto en la capa Entity 
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Gestor_BD(metaclass=Singleton):

    def __init__(self):
        self.Basedatos = {}

    def abrir_BD(self):
        entrada = 'C:/Users/ellia/Documents/INACAP/PruebaSoftware/SistemaBancario/Entity/BaseDatos.txt'

        archivoInput = open(entrada, 'r')

        while True:
            linea = archivoInput.readline().strip()
            print(linea)
            if not linea:
                break

            data = linea.split(",")
            rut = int(data[0])
            nombre = data[1]
            edad = int(data[2])
            sueldo = int(data[3])
            tipo = int(data[4])

            datos = {}
            datos['nombre'] = nombre
            datos['edad'] = edad
            datos['sueldo'] = sueldo

            if tipo == 1:
                saldo = int(data[5])
                cuenta = {}
                cuenta['tipo'] = tipo
                cuenta['saldo'] = saldo

            datos['cuenta'] = cuenta

            self.Basedatos[rut] = datos

        archivoInput.close()

    def cerrar_BD(self):
        salida = 'C:/Users/ellia/Documents/INACAP/PruebaSoftware/SistemaBancario/Entity/BaseDatos.txt'

        archivoOutput = open(salida, 'w')

        for (clave, data) in self.Basedatos.items():
            rut = clave
            nombre = data["nombre"]
            edad = data["edad"]
            sueldo = data["sueldo"]
            registro = data["cuenta"]
            tipo = registro["tipo"]
            saldo = registro["saldo"]

            archivoOutput.write(f"{rut},{nombre},{edad},{sueldo},{tipo},{saldo}\n")

        archivoOutput.close()

    def insertar_BD(self, rut, datos):
        self.Basedatos[rut] = datos
        print(self.Basedatos.keys())
        print(self.Basedatos.values())

    def recuperar_BD(self, rut):

        if rut in self.Basedatos:
            return self.Basedatos[rut]
        else:
            return {}

    def actualizar_BD(self, rut, datos):
        data = {}
        data[rut] = datos
        self.Basedatos.update(data)

    def remover_BD(self, rut):
        pass


g = Gestor_BD()
g.abrir_BD()
g.cerrar_BD()
