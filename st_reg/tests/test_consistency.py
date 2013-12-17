# -*- coding: utf-8 -*-
"""File to test consistency module call"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import st_reg.consistency as con

def test_acre_call():
    invalid_number = '0172030964577'
    acre_index = 1
    assert con.check(invalid_number, acre_index) == False

def test_alagoas_call():
    invalid_number = '240071779'
    alagoas_index = 2
    assert con.check(invalid_number, alagoas_index) == False 

def test_amazonas_call():
    valid_number = '100000010'
    amazonas_index = 3
    assert con.check(valid_number, amazonas_index)

def test_amapa_call():
    invalid_number = '172030964'
    amapa_index = 4
    assert con.check(invalid_number, amapa_index) == False 

def test_bahia_call():
    valid_number = '162345651' 
    bahia_index = 5
    assert con.check(valid_number, bahia_index)
    
def test_ceara_call():
    invalid_number = '60000013'
    ceara_index = 6
    assert con.check(invalid_number, ceara_index) == False

def test_distrito_federal_call():
    valid_number = '0716109443382'
    distrito_federal_index = 7
    assert con.check(valid_number, distrito_federal_index) == True

def test_espirito_santo_call():
    invalid_number = '999999905'
    espirito_santo_index = 8
    assert con.check(invalid_number, espirito_santo_index) == False

def test_maranhao_call():
    invalid_number = '120000382'
    maranhao_index = 10
    assert con.check(invalid_number, maranhao_index) == False

def test_mato_grosso_do_sul_call():
    invalid_number = '280000009'
    mato_grosso_do_sul_index = 12
    assert con.check(invalid_number, mato_grosso_do_sul_index) == False

def test_para_call():
    invalid_number = '159999999'
    para_index = 12
    assert con.check(invalid_number, para_index) == False

def test_pernambuco_call():
    invalid_number = '032141833'
    pernambuco_index = 14
    assert con.check(invalid_number, pernambuco_index) == False
