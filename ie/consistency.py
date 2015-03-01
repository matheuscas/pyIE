# -*- coding: utf-8 -*-
"""Module de validation the states number"""

import states.ac as ac    
import states.al as al
import states.am as am
import states.ap as ap
import states.ba as ba
import states.ce as ce
import states.df as df
import states.es as es
import states.go as go
import states.ma as ma
import states.mt as mt
import states.ms as ms
import states.mg as mg
import states.pa as pa
import states.pb as pb
import states.pe as pe
import states.pr as pr
import states.pi as pi
import states.rj as rj
import states.rn as rn
import states.rs as rs
import states.ro as ro
import states.rr as rr
import states.sc as sc
import states.sp as sp
import states.se as se
import states.to as to

def check(state_registration_number, state_index):
    """
        This function is like a Facade to another modules that
        makes their own state validation.

        state_registration_number - string brazilian state registration number
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
        1: "ac.check(" + "\"" + state_registration_number + "\"" + ")",
        2: "al.check(" + "\"" + state_registration_number + "\"" + ")",
        3: "am.check(" + "\"" + state_registration_number + "\"" + ")",
        4: "ap.check(" + "\"" + state_registration_number + "\"" + ")",
        5: "ba.check(" + "\"" + state_registration_number + "\"" + ")",
        6: "ce.check(" + "\"" + state_registration_number + "\"" + ")",
        7: "df.check(" + "\"" + state_registration_number + "\"" + ")",
        8: "es.check(" + "\"" + state_registration_number + "\"" + ")",
        9: "go.check(" + "\"" + state_registration_number + "\"" + ")",
        10: "ma.check(" + "\"" + state_registration_number + "\"" + ")",
        11: "mg.check(" + "\"" + state_registration_number + "\"" + ")",
        12: "ms.check(" + "\"" + state_registration_number + "\"" + ")",
        13: "mt.check(" + "\"" + state_registration_number + "\"" + ")",
        14: "pa.check(" + "\"" + state_registration_number + "\"" + ")",
        15: "pb.check(" + "\"" + state_registration_number + "\"" + ")",
        16: "pe.check(" + "\"" + state_registration_number + "\"" + ")",
        17: "pi.check(" + "\"" + state_registration_number + "\"" + ")",
        18: "pr.check(" + "\"" + state_registration_number + "\"" + ")",
        19: "rj.check(" + "\"" + state_registration_number + "\"" + ")",
        20: "rn.check(" + "\"" + state_registration_number + "\"" + ")",
        21: "ro.check(" + "\"" + state_registration_number + "\"" + ")",
        22: "rr.check(" + "\"" + state_registration_number + "\"" + ")",
        23: "rs.check(" + "\"" + state_registration_number + "\"" + ")",
        24: "sc.check(" + "\"" + state_registration_number + "\"" + ")",
        25: "se.check(" + "\"" + state_registration_number + "\"" + ")",
        26: "sp.check(" + "\"" + state_registration_number + "\"" + ")",
        27: "to.check(" + "\"" + state_registration_number + "\"" + ")"

    }

    exec('validity = ' + states_validations[state_index])
    return validity
