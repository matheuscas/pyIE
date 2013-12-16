# -*- coding: utf-8 -*-
"""File to test states validations"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import st_reg.states.ac as ac
import st_reg.states.al as al
import st_reg.states.am as am
import st_reg.states.ap as ap
import st_reg.states.ce as ce
import st_reg.states.es as es

#ACRE
def test_ac_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '0172030964577'
    assert ac.check(invalid_number) == False

def test_ac_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '0172030964575'
    assert ac.check(valid_number)

def test_ac_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ac.check(invalid_number) == False

def test_ac_validation_big_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '01720309645755'
    assert ac.check(invalid_number) == False

#ALAGOAS

def test_al_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1720309645'
    assert al.check(invalid_number) == False

def test_al_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert al.check(invalid_number) == False

def test_al_validation_start_different_24():
    """Test if a invalid number start is different 24"""

    invalid_number = '172030964'
    assert al.check(invalid_number) == False

def test_al_validation_type_business():
    """Test if a invalid number is str[2] different 0 or 3 or 5 or 7 or 8"""

    invalid_number = '172030964'
    assert al.check(invalid_number) == False

def test_al_validation_digit_verification():
    """Test if a invalid digit verification"""

    invalid_number = '240071779'
    assert al.check(invalid_number) == False

#AMAZONAS

def test_am_validation_rigth_size_invalid_number():
    invalid_number = '999999999'
    assert am.check(invalid_number) == False

def test_am_validation_rigth_size_valid_number():
    invalid_number = '100000010'
    assert am.check(invalid_number) == True

def test_am_validation_big_size_number():
    invalid_number = '9999999999'
    assert am.check(invalid_number) == False

def test_am_validation_small_size_number():
    invalid_number ='99999999'
    assert am.check(invalid_number) == False

#AMAPÁ

def test_ap_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1720309645'
    assert ap.check(invalid_number) == False

def test_ap_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ap.check(invalid_number) == False

def test_ap_validation_start_different_03():
    """Test if a invalid number start is different 03"""

    invalid_number = '172030964'
    assert ap.check(invalid_number) == False


def test_ap_validation_digit_verification():
    """Test if a invalid digit verification"""

    invalid_number = '030123456'
    assert ap.check(invalid_number) == False

def test_ap_validation():
    """Test if valid number"""

    valid_number = '030123459'
    assert ap.check(valid_number)

#CEARÁ

def test_ce_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1720309645'
    assert ce.check(invalid_number) == False

def test_ce_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ce.check(invalid_number) == False

def test_ce_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '060000014'
    assert ce.check(invalid_number) == False

def test_ce_validation():
    """Test if valid number"""

    valid_number = '060000015'
    assert ce.check(valid_number)

#ESPÍRITO SANTO

def test_es_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1720309645'
    assert es.check(invalid_number) == False

def test_es_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert es.check(invalid_number) == False

def test_es_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '999999991'
    assert es.check(invalid_number) == False

def test_es_validation():
    """Test if valid number"""

    valid_number = '999999990'
    assert es.check(valid_number)
