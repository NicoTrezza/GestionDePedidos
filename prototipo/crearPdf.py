from reportlab.pdfgen import canvas


def crear_aula(departamento, carrera, nombreaula, nombredocente, apellidodocente,
               dni, emailprofesor, rol, descripcion):
    c = canvas.Canvas("crear_aula.pdf")
    c.drawString(100, 750, departamento)
    if departamento == '11':
        c.drawString(100, 740, carrera)
    else:
        c.drawString(100, 740, '------------')
    c.drawString(100, 730, nombreaula)
    c.drawString(100, 720, nombredocente)
    c.drawString(100, 710, apellidodocente)
    c.drawString(100, 700, dni)
    c.drawString(100, 690, emailprofesor)
    c.drawString(100, 680, rol)
    c.drawString(100, 670, descripcion)

    c.save()


def matricular():
    c = canvas.Canvas("matricular.pdf")
    c.drawString(100, 750, "matricular")
    c.save()


def microtaller(nombre, apellido, mail, telefono, dni, departamento, carrera, motivo, microtaller):
    c = canvas.Canvas("microtaller.pdf")
    c.drawString(100, 750, nombre)
    c.drawString(100, 740, apellido)
    c.drawString(100, 730, mail)
    c.drawString(100, 720, telefono)
    c.drawString(100, 710, dni)
    c.drawString(100, 700, departamento)
    if departamento == '11':
        c.drawString(100, 690, carrera)
    else:
        c.drawString(100, 690, '------------')
    c.drawString(100, 680, motivo)
    c.drawString(100, 690, microtaller)

    c.save()