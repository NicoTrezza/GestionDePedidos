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

    login_abm.insertar('mail@lalal.com', '1234', 3)

    persona_abm.insertar('martín', 'Lanús', 12345689, 'mail@lalal.com', 3, 3)


if __name__ == '__main__':
    main()
