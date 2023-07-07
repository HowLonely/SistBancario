# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:44:47 2023
@author: Carlos Luco Montofré

Módulo de la Clase Menu que permite generar y administrar las interfaces 
para la interacción entre el usuario y el sistema
"""

class Menu():
    
    def __init__(self,tipo):
        match tipo:
            case 1: 
               self.menu = "\nSistema de Gestión División Bancaria\n   1- Operación Banca Comercial\n   2- Operación Banca Consumo\n   3- Salir del Sistema\n" 
               self.opciones = ["1", "2", "3"]
            case 2: 
               self.menu = "\nMódulo de Servicios Bancarios\n   1- Operación Mantenimiento cuentas\n   2- Operación Transacciones Cuentas\n   3- Volver menu principal del Sistema\n"
               self.opciones = ["1", "2", "3"]
            case 3: 
               self.menu =  "\nMódulo de Operaciones Bancarias\n   1- Operación Cuentas Cuentas Corrientes\n   2- Operación Cuentas Líneas Créditos\n   3- Operación Cuentas Depósitos Plazo\n   4- Volver menu principal del Sistema\n"             
               self.opciones = ["1", "2", "3", "4"]
            case other: 
               self.menu =  ""             
               self.opciones = []               
         
               
    def Mostrar_Menu_Seleccion(self):
        while True:
            print(chr(27) + "[2J")
            
            print(self.menu)
            self.opcion = input("Digite opción y presione Enter: ")
            
            if self.opcion in self.opciones:
                break
            else: 
                x = input("Opción erronea, Presione Enter para continuar")
            
        return self.opcion
    
    
    def Mostrar_Menu_Transaccion(self, transaccion):
        match transaccion:

            case 111: 
               self.menu =  "\nTransacciones Cuentas Comercial\n   1- Operación Crear Cuentas Corrientes\n   2- Operación Cerrar Cuentas corrientes\n   3- Volver menu Anterior del Sistema\n"             
               self.opciones = ["1", "2", "3"]                       
 
            case 121: 
               self.menu =  "\nTransacciones Cuentas Comercial\n   1- Operación Depositar Cuentas Corrientes\n   2- Operación Retirar Cuentas corrientes\n   3- Operación Consultar Cuentas corrientes\n   4- Volver menu Anterior del Sistema\n"             
               self.opciones = ["1", "2", "3", "4"]            
        
        while True:
            print(chr(27) + "[2J")
            
            print(self.menu)
            self.opcion = input("Digite opción y presione Enter: ")
            
            if self.opcion in self.opciones:
                break
            else: 
                x = input("Opción erronea, Presione Enter para continuar")
            
        return self.opcion