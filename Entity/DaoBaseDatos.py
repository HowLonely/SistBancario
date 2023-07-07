# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:44:47 2023
@author: Carlos Luco Montofré

Módulo que aloja el DAO de acceso a la base de datos. Recibe peticiones de 
trabajo de la capa de Control, comunicandose por DTO 
"""

from Control.Clientes import Cliente_Cuenta

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Dao_Nosql(metaclass=Singleton):
    def __init__(self, gestor_BD):
        self.gestor = gestor_BD
        self.gestor.abrir_BD()
        
    def grabar(self, cliente):
        rut = cliente.muestra_cuenta()
        data = {}
        data['nombre'] = cliente.muestra_nombre()
        data['edad'] = cliente.muestra_edad()
        data['sueldo'] = cliente.muestra_sueldo()
                   

        if isinstance(cliente, Cliente_Cuenta):
            cuenta = {}
            cuenta['tipo'] = 1
            cuenta['saldo'] = cliente.muestra_saldo()

        data['cuenta'] = cuenta
        
        
        self.gestor.insertar_BD(rut, data)
        
    def consultar(self,cliente):
        rut = cliente.muestra_cuenta()
        
        data = self.gestor.recuperar_BD(rut)

        if data:
            cliente.define_nombre(data["nombre"])
            cliente.define_edad(data["edad"])
            cliente.define_sueldo(data["sueldo"])
            registro = data["cuenta"]
            cliente.define_saldo(registro["saldo"])
        else:
            cliente = None
        
        return cliente

    def modificar(self, cliente):
        rut = cliente.muestra_cuenta()  
        data = {}
        data['nombre'] = cliente.muestra_nombre()
        data['edad'] = cliente.muestra_edad()
        data['sueldo'] = cliente.muestra_sueldo()
                   
        
        if isinstance(cliente, Cliente_Cuenta):
            cuenta = {}
            cuenta['tipo'] = 1
            cuenta['saldo'] = cliente.muestra_saldo()
        
        data['cuenta'] = cuenta
        
        self.gestor.actualizar_BD(rut, data)
        
        return cliente
    
    def desconectar(self):
        self.gestor.cerrar_BD()