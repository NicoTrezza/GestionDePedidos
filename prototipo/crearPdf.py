from reportlab.pdfgen import canvas

import time


def crear_aula(departamento, carrera, nombreaula, lista_personas, descripcion):
    contador = 0
    ultimo = 0

    c = canvas.Canvas("crear_aula.pdf")
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento.decode("utf-8"))
    if departamento == '1':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera.decode("utf-8"))
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula.decode("utf-8"))

    """
    for id in idpersona:
        c.drawString(95, 345 + contador, str(id))
        contador = contador + 5
    """

    for persona in lista_personas:
        c.drawString(85, 540 + contador, 'Nombre del Docente:')
        c.drawString(95, 525 + contador, persona.getNombre().decode("utf-8"))
        c.drawString(85, 495 + contador, 'Apellido del docente:')
        c.drawString(95, 480 + contador, persona.getApellido().decode("utf-8"))
        c.drawString(85, 450 + contador, 'Dni:')
        c.drawString(95, 435 + contador, str(persona.getDni()))
        c.drawString(85, 405 + contador, 'Email del profesor:')
        c.drawString(95, 390 + contador, persona.getMail().decode("utf-8"))
        c.drawString(85, 360 + contador, 'Rol del profesor:')
        c.drawString(95, 345 + contador, str(persona.getTipoPersona()))

        contador = contador + 195
        ultimo = 345 + contador


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

    c.drawString(85, 315 + ultimo, 'Descripcion:')
    c.drawString(95, 300 + ultimo, descripcion.decode("utf-8"))

    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\silversonic.jpg", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Crear aula')

    c.save()


def microtaller(nombre, apellido, mail, telefono, dni, departamento, carrera, motivo, microtaller):
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
    c.drawString(95, 390, departamento)
    if departamento == '1':
        c.drawString(85, 360, 'Carrera:')
        c.drawString(95, 345, carrera)
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
    c = canvas.Canvas("tutoria.pdf")
    c.drawString(100, 760, motivo)
    c.drawString(100, 750, nombre)
    c.drawString(100, 740, apellido)
    c.drawString(100, 730, email)
    c.drawString(100, 720, telefono)
    c.drawString(100, 710, dni)
    c.drawString(100, 700, departamento)
    if departamento == '1':
        c.drawString(100, 690, carrera)
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
    c = canvas.Canvas("matricular.pdf")
    c.drawString(100, 750, departamento)
    if departamento == '1':
        c.drawString(100, 740, carrera)
    else:
        c.drawString(100, 740, '------------')

    c.save()