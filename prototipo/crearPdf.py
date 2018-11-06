from reportlab.pdfgen import canvas


def crear_aula(departamento, carrera, nombreaula, nombredirector, emaildirector, nombredocente, apellidodocente,
               dni, emailprofesor, rol, descripcion):
    c = canvas.Canvas("crear_aula.pdf")
    c.drawString(100, 750, departamento)
    c.drawString(100, 740, carrera)
    c.drawString(100, 730, nombreaula)
    c.drawString(100, 720, nombredirector)
    c.drawString(100, 710, emaildirector)
    c.drawString(100, 700, nombredocente)
    c.drawString(100, 690, apellidodocente)
    c.drawString(100, 680, dni)
    c.drawString(100, 670, emailprofesor)
    c.drawString(100, 660, rol)
    c.drawString(100, 650, descripcion)

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
    c.drawString(100, 690, carrera)
    c.drawString(100, 680, motivo)
    c.drawString(100, 690, microtaller)

    c.save()