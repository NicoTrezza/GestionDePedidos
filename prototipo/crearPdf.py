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

    pagina = 1
    c.setFont('Helvetica', 12)
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula.encode("utf-8"))

    for persona in lista_personas:
        c.drawString(430, 765, time.strftime("%c"))
        c.drawImage("static\logo-ead.png", 80, 780, 80, 50)
        c.line(60, 760, 535, 760)
        c.line(85, 665, 205, 665)
        c.setFont('Helvetica', 15)
        c.drawString(85, 670, 'Datos ingresados:')
        c.setFont('Helvetica', 18)
        c.drawString(170, 800, 'Universidad Tecnologica Nacional')
        c.drawString(200, 720, 'Solicitud: Crear aula')
        c.setFont('Helvetica', 12)

        #nombrepersona = unicode(persona.getNombre(), 'latin-1')
        if pagina == 1:
            c.drawString(85, 540, 'Nombre del Docente:')
            c.drawString(95, 525, persona.getNombre().encode("utf-8"))
            c.drawString(85, 495, 'Apellido del docente:')
            c.drawString(95, 480, persona.getApellido().encode("utf-8"))
            c.drawString(85, 450, 'Dni:')
            c.drawString(95, 435, str(persona.getDni()))
            c.drawString(85, 405, 'Email del profesor:')
            c.drawString(95, 390, persona.getMailPersona().encode("utf-8"))
            c.drawString(85, 360, 'Rol del profesor:')
            c.drawString(95, 345, str(persona.getTipoPersona()))
            c.drawString(85, 315, 'Descripcion:')
            c.drawString(95, 300, descripcion.encode("utf-8"))
            c.drawString(480, 80, 'pagina:')
            c.drawString(525, 80, str(pagina))
            pagina = pagina + 1
            c.showPage()
        else:
            c.drawString(85, 600, 'Nombre del Docente:')
            c.drawString(95, 585, persona.getNombre().encode("utf-8"))
            c.drawString(85, 555, 'Apellido del docente:')
            c.drawString(95, 540, persona.getApellido().encode("utf-8"))
            c.drawString(85, 510, 'Dni:')
            c.drawString(95, 495, str(persona.getDni()))
            c.drawString(85, 465, 'Email del profesor:')
            c.drawString(95, 450, persona.getMailPersona().encode("utf-8"))
            c.drawString(85, 420, 'Rol del profesor:')
            c.drawString(95, 405, str(persona.getTipoPersona()))
            c.drawString(480, 80, 'pagina:')
            c.drawString(525, 80, str(pagina))
            pagina = pagina + 1
            c.showPage()

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
    pagina = 1
    c.setFont('Helvetica', 12)
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula.encode("utf-8"))

    for persona in lista_personas:
        c.drawString(430, 765, time.strftime("%c"))
        c.drawImage("static\logo-ead.png", 80, 780, 50, 50)
        c.line(60, 760, 535, 760)
        c.line(85, 665, 205, 665)
        c.setFont('Helvetica', 15)
        c.drawString(85, 670, 'Datos ingresados:')
        c.setFont('Helvetica', 18)
        c.drawString(170, 800, 'Universidad Tecnologica Nacional')
        c.drawString(200, 720, 'Solicitud: Reutilizar aula')
        c.setFont('Helvetica', 12)

        #nombrepersona = unicode(persona.getNombre(), 'latin-1')

        if pagina == 1:
            c.drawString(85, 540, 'Nombre del Docente:')
            c.drawString(95, 525, persona.getNombre().encode("utf-8"))
            c.drawString(85, 495, 'Apellido del docente:')
            c.drawString(95, 480, persona.getApellido().encode("utf-8"))
            c.drawString(85, 450, 'Dni:')
            c.drawString(95, 435, str(persona.getDni()))
            c.drawString(85, 405, 'Email del profesor:')
            c.drawString(95, 390, persona.getMailPersona().encode("utf-8"))
            c.drawString(85, 360, 'Rol del profesor:')
            c.drawString(95, 345, str(persona.getTipoPersona()))
            c.drawString(85, 315, 'Direccion ULR:')
            c.drawString(95, 300, direccion.decode("utf-8"))
            """c.drawString(85, 270, 'Nuevo nombre del aula:')
            c.drawString(95, 255, nuevonombre.decode("utf-8"))
            c.drawString(85, 225, 'Otros:')
            c.drawString(95, 210, otros.decode("utf-8"))"""
            c.drawString(480, 80, 'pagina:')
            c.drawString(525, 80, str(pagina))
            pagina = pagina + 1
        else:
            c.drawString(85, 600, 'Nombre del Docente:')
            c.drawString(95, 585, persona.getNombre().encode("utf-8"))
            c.drawString(85, 555, 'Apellido del docente:')
            c.drawString(95, 540, persona.getApellido().encode("utf-8"))
            c.drawString(85, 510, 'Dni:')
            c.drawString(95, 495, str(persona.getDni()))
            c.drawString(85, 465, 'Email del profesor:')
            c.drawString(95, 450, persona.getMailPersona().encode("utf-8"))
            c.drawString(85, 420, 'Rol del profesor:')
            c.drawString(95, 405, str(persona.getTipoPersona()))
            c.drawString(480, 80, 'pagina:')
            c.drawString(525, 80, str(pagina))
            pagina = pagina + 1
        c.showPage()

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

    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\logo-ead.png", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Eliminar aula')
    c.setFont('Helvetica', 12)
    pagina = 1

    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, '--------')

    c.drawString(85, 540, 'Nombre del aula:')
    c.drawString(95, 525, nombreaula.encode("utf-8"))
    c.drawString(85, 495, 'Direccion ULR:')
    c.drawString(95, 480, direccion.encode("utf-8"))
    c.drawString(85, 450, 'Motivo:')
    c.drawString(95, 435, motivo.encode("utf-8"))
    c.drawString(480, 80, 'pagina:')
    c.drawString(525, 80, str(pagina))

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
    pagina = 1
    c.setFont('Helvetica', 12)
    c.drawString(480, 80, 'pagina:')
    c.drawString(525, 80, str(pagina))
    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\logo-ead.png", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Inscripcion a microtaller')
    c.setFont('Helvetica', 12)

    c.drawString(85, 630, 'Nombre:')
    c.drawString(95, 615, nombre.encode("utf-8"))
    c.drawString(85, 585, 'Apellido:')
    c.drawString(95, 570, apellido.encode("utf-8"))
    c.drawString(85, 540, 'E-mail:')
    c.drawString(95, 525, mail.encode("utf-8"))
    c.drawString(85, 495, 'Telefono:')
    c.drawString(95, 480, telefono)
    c.drawString(85, 450, 'Dni:')
    c.drawString(95, 435, str(dni))
    c.drawString(85, 405, 'Departamento:')
    c.drawString(95, 390, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 360, 'Carrera:')
        c.drawString(95, 345, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 360, 'Carrera:')
        c.drawString(95, 345, '---------')
    c.drawString(85, 315, 'Microtaller:')
    c.drawString(95, 300, str(microtaller))
    c.drawString(85, 270, 'Motivo:')
    c.drawString(95, 255, motivo.encode("utf-8"))

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
    c.setLineWidth(.3)
    pagina = 1
    c.setFont('Helvetica', 12)
    c.drawString(480, 80, 'pagina:')
    c.drawString(525, 80, str(pagina))
    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\logo-ead.png", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Inscripcion a capacitacion')
    c.setFont('Helvetica', 12)

    c.drawString(85, 630, 'Nombre:')
    c.drawString(95, 615, nombre.encode("utf-8"))
    c.drawString(85, 585, 'Apellido:')
    c.drawString(95, 570, apellido.encode("utf-8"))
    c.drawString(85, 540, 'E-mail:')
    c.drawString(95, 525, email.encode("utf-8"))
    c.drawString(85, 495, 'Telefono:')
    c.drawString(95, 480, telefono)
    c.drawString(85, 450, 'Dni:')
    c.drawString(95, 435, str(dni))
    c.drawString(85, 405, 'Departamento:')
    c.drawString(95, 390, departamento_nombre.encode("utf-8"))
    if departamento == '11':
        c.drawString(85, 360, 'Carrera:')
        c.drawString(95, 345, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 360, 'Carrera:')
        c.drawString(95, 345, '--------')
    c.drawString(85, 315, 'Rol:')
    c.drawString(95, 300, str(rol))
    c.drawString(85, 270, 'Cantidad de personas:')
    if cant_personas != 1:
        c.drawString(95, 255, str(cant_personas))
    else:
        c.drawString(95, 255, '1')
    c.drawString(85, 225, 'Dias y horarios seleccionados:')
    c.drawString(95, 210, 'Dia:')
    c.drawString(120, 210, dia1)
    c.drawString(190, 210, 'Desde:')
    c.drawString(232, 210, dia1_hora1)
    c.drawString(300, 210, 'Hasta:')
    c.drawString(340, 210, dia1_hora2)
    c.drawString(95, 180, 'Dia:')
    c.drawString(120, 180, dia2)
    c.drawString(190, 180, 'Desde:')
    c.drawString(232, 180, dia2_hora1)
    c.drawString(300, 180, 'Hasta:')
    c.drawString(340, 180, dia2_hora2)
    c.drawString(95, 150, 'Dia:')
    c.drawString(120, 150, dia3)
    c.drawString(190, 150, 'Desde:')
    c.drawString(232, 150, dia3_hora1)
    c.drawString(300, 150, 'Hasta:')
    c.drawString(340, 150, dia3_hora2)
    c.drawString(85, 120, 'Motivo:')
    c.drawString(95, 105, motivo.encode("utf-8"))

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
    c.setLineWidth(.3)
    pagina = 1
    c.setFont('Helvetica', 12)
    c.drawString(480, 80, 'pagina:')
    c.drawString(525, 80, str(pagina))
    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\logo-ead.png", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Matricular usuarios')
    c.setFont('Helvetica', 12)

    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento_nombre.encode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera_nombre.encode("utf-8"))
    else:
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, '--------')

    c.save()
