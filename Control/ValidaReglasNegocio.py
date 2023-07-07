# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:16:39 2023
@author: Carlos Luco Montofré

Módulo con la clase para validad reglas de negocio. La componente agrupa
los requisitos que deben cumplir los datos de las operaciones del Banco
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Validador_Reglas_Negocio(metaclass=Singleton):
    def __init__(self):
        pass
    
    def validar_edad(self,edad) -> bool:
        respuesta = False
        if 18 < edad < 65:
            respuesta = True
        return respuesta
            
    def validar_sueldo(self, sueldo)  -> bool:
        respuesta = False
        if sueldo >= 500000:
            respuesta = True
        return respuesta
            
    def validar_monto_deposito(self, monto)  -> bool:
        respuesta = False
        if monto >= 10000:
            respuesta = True
        return respuesta
            
    def validar_monto_retiro(self, monto)  -> bool:
        respuesta = False
        if monto >= 10000:
            respuesta = True
        return respuesta