#!/usr/bin/env python
# -*- coding: utf-8 -*-

from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM
from negocio.aulaABM import AulaABM
from negocio.tipoPersonaABM import TipoPersonaABM
from negocio.personaABM import PersonaABM
from negocio.loginABM import LoginABM


def main():
    departamento_abm = DepartamentoABM()
    carrera_abm = CarreraABM()
    aula_abm = AulaABM()
    tipo_persona_abm = TipoPersonaABM()
    persona_abm = PersonaABM()
    login_abm = LoginABM()

    login = login_abm.traerXMail('mailrandom@lalal.com')

    for a in persona_abm.listar():
        print u'{}'.format(a)


if __name__ == '__main__':
    main()
