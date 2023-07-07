# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:44:47 2023
@author: Carlos Luco Montofré

Módulo que registra el Dominio de la aplicación. Los objetos del dominio son
gestioandos por una factoría que presta servicio a los objetos operativos de
la capa de Control
"""

from abc import ABC
from abc import abstractmethod

class Cliente():
    def __init__(self, numero, nombre, edad, sueldo):
        self.numCuenta = numero
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        
        
class Cliente_Cuenta(Cliente):
    def __init__(self, numero, nombre, edad, sueldo):
        super().__init__(numero, nombre, edad, sueldo)
        self.saldo = 0
        
    def muestra_cuenta(self):
        return self.numCuenta

    def define_nombre(self, nombre):
        self.nombre = nombre

    def muestra_nombre(self):
        return self.nombre

    def define_edad(self, edad):
        self.edad = edad
        
    def muestra_edad(self):
        return self.edad

    def define_sueldo(self, sueldo):
        self.sueldo = sueldo
            
    def muestra_sueldo(self):
        return self.sueldo

    def define_saldo(self, saldo):
        self.saldo = saldo
            
    def muestra_saldo(self):
        return self.saldo
        
    def credita_cuenta(self, monto):
        self.saldo += monto

    def debita_cuenta(self, monto):
        self.saldo -= monto 
        
        
class Cliente_Credito(Cliente):
     def __init__(self, numero, nombre, edad, sueldo, limite):
         super().__init__(numero, nombre, edad, sueldo)
         self.limite_monto = limite
         self.deuda = 0
        
class Cliente_Deposito(Cliente):
    def __init__(self,numero, nombre, edad, sueldo, monto, interes, plazo):
        super().__init__(numero, nombre, edad, sueldo)
        self.monto = monto
        self.interes = interes
        self.plazo = plazo

        
class Factory_Banco(ABC):

    @abstractmethod
    def crea_cliente_cuenta(self):
        pass

    @abstractmethod
    def crea_cliente_credito(self):
        pass
        
    @abstractmethod
    def crea_cliente_deposito(self):
        pass
    
    
class Banco_Comercial(Factory_Banco):
    
    def crea_cliente_cuenta(self, numero, nombre, edad, sueldo):
        return Cliente_Cuenta(numero, nombre, edad, sueldo)
        

    def crea_cliente_credito(self, numero, nombre, edad, sueldo, limite):
        return Cliente_Credito(numero, nombre, edad, sueldo, limite)
        

    def crea_cliente_deposito(self, numero, nombre, edad, sueldo, monto, interes, plazo):
        return Cliente_Deposito(numero, nombre, edad, sueldo, monto, interes, plazo)    
    
class Banco_Consumo(Factory_Banco):
      
      def crea_cliente_cuenta(self, numero,  nombre, edad, sueldo):
          return Cliente_Cuenta(numero,  nombre, edad, sueldo)
          

      def crea_cliente_credito(self, numero,  nombre, edad, sueldo, limite):
          return Cliente_Credito(numero,  nombre, edad, sueldo, limite)
          

      def crea_cliente_deposito(self, numero,  nombre, edad, sueldo, monto, interes, plazo):
          return Cliente_Deposito(numero,  nombre, edad, sueldo, monto, interes, plazo)      
