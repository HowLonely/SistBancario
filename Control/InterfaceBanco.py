# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:44:47 2023
@author: Carlos Luco Montofré

Módulo que reune las interfaces de la capa de control. Las interfaces entregan 
servicios a los objetos de la capa boundary. Además, administra las operaciones
del dominio de la aplicación, interactuando con la capa de Entity
"""

from Entity.BaseDatos import Gestor_BD
from abc import ABC
from abc import abstractmethod
from Entity.DaoBaseDatos import Dao_Nosql
from Control.Clientes import Banco_Comercial
from Control.ValidaReglasNegocio import Validador_Reglas_Negocio


class Interface_Mantenimiento(ABC):

    @abstractmethod
    def crea_instrumento(self, datos) -> bool:
        pass

    @abstractmethod
    def deconectar_Api(self) -> bool:
        pass


class Api_Mantenimiento(Interface_Mantenimiento):

    def __init__(self):
        self.DAObase = Dao_Nosql(Gestor_BD())
        self.factory = Banco_Comercial()
        self.Validador = Validador_Reglas_Negocio()

    def crea_instrumento(self, data):

        rut = data["rut"]
        nombre = data["nombre"]
        edad = data["edad"]
        sueldo = data["sueldo"]

        if self.Validador.validar_edad(edad) and self.Validador.validar_sueldo(sueldo):

            DTO_cliente = self.factory.crea_cliente_cuenta(rut, nombre, edad, sueldo)

            respuesta = self.DAObase.consultar(DTO_cliente)

            if respuesta is None:

                self.DAObase.grabar(DTO_cliente)
                return True
            else:
                return False
        else:
            return False

    def deconectar_Api(self) -> bool:
        self.DAObase.desconectar()
        return True


class Interface_Transacciones(ABC):

    @abstractmethod
    def consulta_instrumento(self, datos) -> bool:
        pass

    @abstractmethod
    def incrementa_instrumento(self, data) -> bool:
        pass

    @abstractmethod
    def decrementa_instrumento(self, data) -> bool:
        pass


class Api_Transacciones(Interface_Transacciones):

    def __init__(self):
        self.DAObase = Dao_Nosql(Gestor_BD())
        self.factory = Banco_Comercial()
        self.Validador = Validador_Reglas_Negocio()

    def consulta_instrumento(self, data):

        rut = data["rut"]

        DTO_cliente = self.factory.crea_cliente_cuenta(rut, "", "", "")
        DTO_cliente = self.DAObase.consultar(DTO_cliente)

        if DTO_cliente is not None:

            data = {}
            data[rut] = rut
            data["saldo"] = DTO_cliente.muestra_saldo()

            return data
        else:
            return {}

    def incrementa_instrumento(self, data):
        rut = data["rut"]
        monto = data["monto"]

        if self.Validador.validar_monto_deposito(monto):

            DTO_cliente = self.factory.crea_cliente_cuenta(rut, "", "", "")

            DTO_cliente = self.DAObase.consultar(DTO_cliente)

            DTO_cliente.credita_cuenta(monto)
            DTO_cliente = self.DAObase.modificar(DTO_cliente)

            data = {}
            data[rut] = rut
            data["saldo"] = DTO_cliente.muestra_saldo()

            return True, data
        else:
            data = {}
            return False, data

    def decrementa_instrumento(self, data):
        rut = data["rut"]
        monto = data["monto"]

        if self.Validador.validar_monto_retiro(monto):

            DTO_cliente = self.factory.crea_cliente_cuenta(rut, "", "", "")

            DTO_cliente = self.DAObase.consultar(DTO_cliente)

            DTO_cliente.debita_cuenta(monto)
            DTO_cliente = self.DAObase.modificar(DTO_cliente)

            data = {}
            data[rut] = rut
            data["saldo"] = DTO_cliente.muestra_saldo()

            return True, data
        else:
            data = {}
            return False, data
