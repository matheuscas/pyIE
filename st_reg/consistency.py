# -*- coding: utf-8 -*-
import states.ac as ac
import states.al as al
import states.am as am
import states.ap as ap
import states.ce as ce
import states.es as es
import states.ma as ma
import states.ms as ms
import states.pa as pa
import states.pe as pe

def check(st_reg_number, state_index):
    """
        This function is like a Facade to another modules that
        makes their own state validation.

        st_reg_number - string brazilian state registration number
        state_index  - integer index that references the state

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
        1:"ac.check("+ "\"" + st_reg_number + "\"" + ")",
        2:"al.check("+ "\"" + st_reg_number + "\"" + ")",
        3:"am.check("+ "\"" + st_reg_number + "\"" + ")",
	4:"ap.check("+ "\"" + st_reg_number + "\"" + ")",
	6:"ce.check("+ "\"" + st_reg_number + "\"" + ")",
	8:"es.check("+ "\"" + st_reg_number + "\"" + ")",
	10:"ma.check("+ "\"" + st_reg_number + "\"" + ")",
	12:"ms.check("+ "\"" + st_reg_number + "\"" + ")",
	14:"pa.check("+ "\"" + st_reg_number + "\"" + ")",
	16:"pe.check("+ "\"" + st_reg_number + "\"" + ")"
    }

    exec('validity = ' + states_validations[state_index])
    return validity
