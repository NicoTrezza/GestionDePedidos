#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM

import time


def crear_aula(departamento, carrera, nombreaula, lista_personas, descripcion):
    carrera_nombre = 'no'
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    departamento_nombre = departamento_abm.traer(departamento).getNombreDepartamento()
    if departamento == '1':
        try:
            carrera_nombre = carrera_abm.traer(carrera).getNombreCarrera()
        except:
            carrera_nombre = 'no tiene'

    c = canvas.Canvas("crear_aula.pdf")
    c.setLineWidth(.3)

    """c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\silversonic.jpg", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Crear aula')"""
    c.setFont('Helvetica', 12)
    c.drawString(85, 315, 'Descripcion:')
    c.drawString(95, 300, descripcion.encode("utf-8"))
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula.encode("utf-8"))

    """
    for id in idpersona:
        c.drawString(95, 345 + contador, str(id))
        contador = contador + 5
    """

    for persona in lista_personas:
        c.drawString(430, 765, time.strftime("%c"))
        c.drawImage("static\silversonic.jpg", 80, 780, 50, 50)
        c.line(60, 760, 535, 760)
        c.line(85, 665, 205, 665)
        c.setFont('Helvetica', 15)
        c.drawString(85, 670, 'Datos ingresados:')
        c.setFont('Helvetica', 18)
        c.drawString(170, 800, 'Universidad Tecnologica Nacional')
        c.drawString(200, 720, 'Solicitud: Crear aula')
        c.setFont('Helvetica', 12)

        #nombrepersona = unicode(persona.getNombre(), 'latin-1')

        c.drawString(85, 540, 'Nombre del Docente:')
        c.drawString(95, 525, persona.getNombre().encode("utf-8"))
        c.drawString(85, 495, 'Apellido del docente:')
        c.drawString(95, 480, persona.getApellido().encode("utf-8"))
        c.drawString(85, 450, 'Dni:')
        c.drawString(95, 435, str(persona.getDni()))
        c.drawString(85, 405, 'Email del profesor:')
        c.drawString(95, 390, persona.getMail().encode("utf-8"))
        c.drawString(85, 360, 'Rol del profesor:')
        c.drawString(95, 345, str(persona.getTipoPersona()))
        c.showPage()


    """
    c.drawString(85, 540, 'Nombre del Docente:')
    c.drawString(95, 525, nombredocente)
    c.drawString(85, 495, 'Apellido del docente:')
    c.drawString(95, 480, apellidodocente)
    c.drawString(85, 450, 'Dni:')
    c.drawString(95, 435, dni)
    c.drawString(85, 405, 'Email del profesor:')
    c.drawString(95, 390, emailprofesor)
    c.drawString(85, 360, 'Rol del profesor:')
    c.drawString(95, 345, rol)
    """

    c.save()


def modificar_aula(departamento, carrera, nombreaula, direccion, lista_personas, nuevonombre, otros):
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    departamento_nombre = departamento_abm.traer(departamento).getNombreDepartamento()
    carrera_nombre = 'no tiene'
    if departamento == '1':
        try:
            carrera_nombre = carrera_abm.traer(carrera).getNombreCarrera()
        except:
            carrera_nombre = 'no tiene'

    c = canvas.Canvas("modificar_aula.pdf")
    c.setLineWidth(.3)

    """c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\silversonic.jpg", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Crear aula')"""
    c.setFont('Helvetica', 12)
    c.drawString(85, 315, 'Direccion ULR:')
    c.drawString(95, 300, direccion.decode("utf-8"))
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula.encode("utf-8"))

    """
    for id in idpersona:
        c.drawString(95, 345 + contador, str(id))
        contador = contador + 5
    """

    for persona in lista_personas:
        c.drawString(430, 765, time.strftime("%c"))
        c.drawImage("static\silversonic.jpg", 80, 780, 50, 50)
        c.line(60, 760, 535, 760)
        c.line(85, 665, 205, 665)
        c.setFont('Helvetica', 15)
        c.drawString(85, 670, 'Datos ingresados:')
        c.setFont('Helvetica', 18)
        c.drawString(170, 800, 'Universidad Tecnologica Nacional')
        c.drawString(200, 720, 'Solicitud: Crear aula')
        c.setFont('Helvetica', 12)

        #nombrepersona = unicode(persona.getNombre(), 'latin-1')

        c.drawString(85, 540, 'Nombre del Docente:')
        c.drawString(95, 525, persona.getNombre().encode("utf-8"))
        c.drawString(85, 495, 'Apellido del docente:')
        c.drawString(95, 480, persona.getApellido().encode("utf-8"))
        c.drawString(85, 450, 'Dni:')
        c.drawString(95, 435, str(persona.getDni()))
        c.drawString(85, 405, 'Email del profesor:')
        c.drawString(95, 390, persona.getMail().encode("utf-8"))
        c.drawString(85, 360, 'Rol del profesor:')
        c.drawString(95, 345, str(persona.getTipoPersona()))
        c.showPage()


    """
    c.drawString(85, 540, 'Nombre del Docente:')
    c.drawString(95, 525, nombredocente)
    c.drawString(85, 495, 'Apellido del docente:')
    c.drawString(95, 480, apellidodocente)
    c.drawString(85, 450, 'Dni:')
    c.drawString(95, 435, dni)
    c.drawString(85, 405, 'Email del profesor:')
    c.drawString(95, 390, emailprofesor)
    c.drawString(85, 360, 'Rol del profesor:')
    c.drawString(95, 345, rol)
    """

    c.save()


def eliminar_aula(departamento, carrera, nombreaula, direccion, motivo):
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    departamento_nombre = departamento_abm.traer(departamento).getNombreDepartamento()
    carrera_nombre = 'no tiene'
    if departamento == '1':
        try:
            carrera_nombre = carrera_abm.traer(carrera).getNombreCarrera()
        except:
            carrera_nombre = 'no tiene'

    c = canvas.Canvas("eliminar_aula.pdf")
    c.setLineWidth(.3)

    c.setFont('Helvetica', 12)
    c.drawString(85, 315, 'Direccion ULR:')
    c.drawString(95, 300, direccion.encode("utf-8"))
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula.encode("utf-8"))

    c.drawString(85, 400, 'Motivo:')
    c.drawString(95, 405, motivo.encode("utf-8"))

    c.save()


def microtaller(nombre, apellido, mail, telefono, dni, departamento, carrera, motivo, microtaller):
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    departamento_nombre = departamento_abm.traer(departamento).getNombreDepartamento()
    carrera_nombre = 'no tiene'
    if departamento == '1':
        try:
            carrera_nombre = carrera_abm.traer(carrera).getNombreCarrera()
        except:
            carrera_nombre = 'no tiene'

    c = canvas.Canvas("microtaller.pdf")
    c.setLineWidth(.3)
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Crear aula')
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 12)
    c.drawString(85, 630, 'Nombre:')
    c.drawString(95, 615, nombre)
    c.drawString(85, 585, 'Apellido:')
    c.drawString(95, 570, apellido)
    c.drawString(85, 540, 'E-mail:')
    c.drawString(95, 525, mail)
    c.drawString(85, 495, 'Telefono:')
    c.drawString(95, 480, telefono)
    c.drawString(85, 450, 'Dni:')
    c.drawString(95, 435, dni)
    c.drawString(85, 405, 'Departamento:')
    c.drawString(95, 390, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 360, 'Carrera:')
        c.drawString(95, 345, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 360, 'Microtaller:')
        c.drawString(95, 345, microtaller)
    c.drawString(85, 315, 'Motivo:')
    c.drawString(95, 300, motivo)
    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("venv\silversonic.jpg", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)

    c.save()


def tutoria(motivo, nombre, apellido, email, telefono, dni, departamento, carrera, rol, cant_personas,
            dia1, dia1_hora1, dia1_hora2, dia2, dia2_hora1, dia2_hora2, dia3, dia3_hora1, dia3_hora2,):
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    departamento_nombre = departamento_abm.traer(departamento).getNombreDepartamento()
    carrera_nombre = 'no tiene'
    if departamento == '1':
        try:
            carrera_nombre = carrera_abm.traer(carrera).getNombreCarrera()
        except:
            carrera_nombre = 'no tiene'

    c = canvas.Canvas("tutoria.pdf")
    c.drawString(100, 760, motivo)
    c.drawString(100, 750, nombre)
    c.drawString(100, 740, apellido)
    c.drawString(100, 730, email)
    c.drawString(100, 720, telefono)
    c.drawString(100, 710, dni)
    c.drawString(100, 700, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(100, 690, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(100, 690, '------------')
    c.drawString(100, 680, rol)
    c.drawString(100, 670, cant_personas)
    c.drawString(100, 660, dia1)
    c.drawString(100, 650, dia1_hora1)
    c.drawString(100, 640, dia1_hora2)
    c.drawString(100, 630, dia2)
    c.drawString(100, 620, dia2_hora1)
    c.drawString(100, 610, dia2_hora2)
    c.drawString(100, 600, dia3)
    c.drawString(100, 590, dia3_hora1)
    c.drawString(100, 580, dia3_hora2)

    c.save()


def matricular(departamento, carrera):
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    departamento_nombre = departamento_abm.traer(departamento).getNombreDepartamento()
    carrera_nombre = 'no tiene'
    if departamento == '1':
        try:
            carrera_nombre = carrera_abm.traer(carrera).getNombreCarrera()
        except:
            carrera_nombre = 'no tiene'

    c = canvas.Canvas("matricular.pdf")
    c.drawString(100, 750, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(100, 740, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(100, 740, '------------')

    c.save()
