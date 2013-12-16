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
