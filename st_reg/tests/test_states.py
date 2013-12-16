# -*- coding: utf-8 -*-
"""File to test states validations"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import st_reg.states.ac as ac
import st_reg.states.al as al
import st_reg.states.am as am
import st_reg.states.ap as ap
#import st_reg.states.ba as ba
#import st_reg.states.ce as ce
#import st_reg.states.df as df
#import st_reg.states.es as es
#import st_reg.states.go as go
#import st_reg.states.ma as ma
#import st_reg.states.mt as mt
#import st_reg.states.ms as ms
#import st_reg.states.mg as mg
#import st_reg.states.pa as pa
#import st_reg.states.pb as pb
#import st_reg.states.pr as pr
#import st_reg.states.pi as pi
#import st_reg.states.rj as rj
#import st_reg.states.rs as rs
#import st_reg.states.rn as rn
#import st_reg.states.rs as rs
#import st_reg.states.ro as ro
#import st_reg.states.rr as rr
#import st_reg.states.sc as sc
#import st_reg.states.sp as sp
#import st_reg.states.se as se
#import st_reg.states.to as to





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
    assert ac.check(invalid_number) == False

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
    """Test if a invalid number is really invalid"""

    invalid_number = '999999999'
    assert am.check(invalid_number) == False

def test_am_validation_rigth_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '100000010'
    assert am.check(valid_number) == True

def test_am_validation_big_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '9999999999'
    assert am.check(invalid_number) == False

def test_am_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number ='99999999'
    assert am.check(invalid_number) == False


'''


#########################################################
#                                                       #
#                     Espaço reservado para ap          #
#########################################################

























'''

