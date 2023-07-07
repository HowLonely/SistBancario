# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:44:47 2023

@author: Carlos Luco Montofré
"""

from Control.InterfaceBanco import Api_Mantenimiento, Api_Transacciones
from Boundary.ClaseMenu import Menu


def valida_digitacion(datos, valida_data):
    error_validacion = []

    for i, (clave, valor) in enumerate(datos.items()):
        match valida_data[i]:
            case "n":
                if valor.isdigit():
                    error_validacion.append(False)
                else:
                    error_validacion.append(True)
            case "l":
                if valor.isalpha():
                    error_validacion.append(False)
                else:
                    error_validacion.append(True)

    return error_validacion


def convertir_datos(datos, valida_data):
    data = {}

    for i, (clave, valor) in enumerate(datos.items()):
        match valida_data[i]:
            case "n":
                if valor.isdigit():
                    data[clave] = int(valor)
            case "l":
                if valor.isalpha():
                    data[clave] = valor

    return data


def crea_cliente_cuenta(api_Mantenimiento):
    rut = input("Digite número cédula identidad: ")
    nombre = input("Digite nombre: ")
    edad = input("Digite edad: ")
    sueldo = input("Digite sueldo: ")

    datos = {}
    datos["rut"] = rut
    datos["tipo"] = "corriente"
    datos["nombre"] = nombre
    datos["edad"] = edad
    datos["sueldo"] = sueldo

    valida_data = ["n", "l", "l", "n", "n"]
    if True in valida_digitacion(datos, valida_data):
        print("error digitación, Volver a digitar información")
    else:
        data = convertir_datos(datos, valida_data)

        resultado = api_Mantenimiento.crea_instrumento(data)

        if resultado:
            print("Cuenta exitosamente creada")
        else:
            print("Datos no cumplen requisitos del banco")

    x = input("Presione Enter para continuar")


def deposita_cliente_cuenta(api_Transacciones):
    rut = input("Digite número cédula identidad: ")
    monto = input("Digite monto a depositar: ")

    datos = {}
    datos["rut"] = rut
    datos["tipo"] = "corriente"
    datos["monto"] = monto

    valida_data = ["n", "l", "n"]
    if True in valida_digitacion(datos, valida_data):
        print("error digitación, Volver a digitar información")
    else:
        data = convertir_datos(datos, valida_data)

        (resultado, detalle) = api_Transacciones.incrementa_instrumento(data)

        if resultado:
            print("Deposito realizado. Monto actual: ", detalle["saldo"])
        else:
            print("Datos no cumplen requisitos del banco")

    x = input("Presione Enter para continuar")


def retira_cliente_cuenta(api_Transacciones):
    rut = input("Digite número cédula identidad: ")
    monto = input("Digite monto a retirar: ")

    datos = {}
    datos["rut"] = rut
    datos["tipo"] = "corriente"
    datos["monto"] = monto

    valida_data = ["n", "l", "n"]
    if True in valida_digitacion(datos, valida_data):
        print("error digitación, Volver a digitar información")
    else:
        data = convertir_datos(datos, valida_data)

        (resultado, detalle) = api_Transacciones.decrementa_instrumento(data)

        if resultado:
            print("Retiro realizado. Monto actual: ", detalle["saldo"])
        else:
            print("Datos no cumplen requisitos del banco")

    x = input("Presione Enter para continuar")


def consulta_cliente_cuenta(api_Transacciones):
    rut = input("Digite número cédula identidad: ")

    datos = {}
    datos["rut"] = rut
    datos["tipo"] = "corriente"

    valida_data = ["n", "l"]
    if True in valida_digitacion(datos, valida_data):
        print("error digitación, Volver a digitar información")
    else:
        data = convertir_datos(datos, valida_data)

        resultado = api_Transacciones.consulta_instrumento(data)

        if resultado:

            print("La cuanta tiene como saldo: ", resultado["saldo"])

        else:
            print("La cuanta solicitada no existe")

    x = input("Presione Enter para continuar")


def Menu_Sistema():
    api_Transacciones = Api_Transacciones()
    api_Mantenimiento = Api_Mantenimiento()
    menu1 = Menu(1)
    menu2 = Menu(2)
    menu3 = Menu(3)
    menu4 = Menu(111)

    while True:
        opcion1 = menu1.Mostrar_Menu_Seleccion()
        if opcion1 == "3":
            break

        if opcion1 == "1":
            while True:
                opcion2 = menu2.Mostrar_Menu_Seleccion()
                if opcion2 == "3":
                    break

                if opcion2 == "1":
                    while True:
                        opcion3 = menu3.Mostrar_Menu_Seleccion()
                        if opcion3 == "4":
                            break

                        if opcion3 == "1":
                            while True:
                                opcion4 = menu4.Mostrar_Menu_Transaccion(111)
                                if opcion4 == "3":
                                    break

                                if opcion4 == "1":
                                    crea_cliente_cuenta(api_Mantenimiento)

                if opcion2 == "2":
                    while True:
                        opcion3 = menu3.Mostrar_Menu_Seleccion()
                        if opcion3 == "4":
                            break

                        if opcion3 == "1":
                            while True:
                                opcion4 = menu4.Mostrar_Menu_Transaccion(121)
                                if opcion4 == "4":
                                    break

                                if opcion4 == "1":
                                    deposita_cliente_cuenta(api_Transacciones)

                                if opcion4 == "2":
                                    retira_cliente_cuenta(api_Transacciones)

                                if opcion4 == "3":
                                    consulta_cliente_cuenta(api_Transacciones)

    api_Mantenimiento.deconectar_Api()
    print("Base de datos desconectada")
