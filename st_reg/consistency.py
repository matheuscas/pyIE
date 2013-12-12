# -*- coding: utf-8 -*-
import states.ba as ba

def check(st_reg_number, state_index):
    """
        This function is like a Facade to another modules that
        makes their own state validation.

        st_reg_number - brazilian state registration number
        state_index  - index that references the state

        1 => AC (Acre)
        2 => AL (Alagoas)
        3 => AM (Amazonas)
        4 => AP (Amapá)
        5 => BA (Bahia)
        6 => CE (Ceará)
        7 => DF (Distrito Federal)
        8 => ES (Espírito Santo')
        9 => GO (Goias)
        10 => MA (Maranhão)
        11 => MG (Minas Gerais)
        12 => MS (Mato Grosso do Sul)
        13 => MT (Mato Grosso)
        14 => PA (Pará)
        15 => PB (Paraíba)
        16 => PE (Pernambuco)
        17 => PI (Piauí)
        18 => PR (Paraná)
        19 => RJ (Rio de Janeiro)
        20 => RN (Rio Grande do Norte)
        21 => RO (Rondônia)
        22 => RR (Roraima)
        23 => RS (Rio Grande do Sul)
        24 => SC (Santa Catarina)
        25 => SE (Sergipe)
        26 => SP (São Paulo)
        27 => TO (Tocantins)
    """  

    states_validations = {
        1:"ac.check(" + str(st_reg_number) + ")"
    }

    exec('validity = ' + states_validations[state_index])
    return validity
