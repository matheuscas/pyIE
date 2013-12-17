# -*- coding: utf-8 -*-
"""File to test states validations"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import st_reg.states.ac as ac
import st_reg.states.al as al
import st_reg.states.am as am
import st_reg.states.ap as ap
import st_reg.states.ba as ba
import st_reg.states.ce as ce
import st_reg.states.df as df
import st_reg.states.es as es
#import st_reg.states.go as go
import st_reg.states.ma as ma
#import st_reg.states.mt as mt
import st_reg.states.ms as ms
#import st_reg.states.mg as mg
import st_reg.states.pa as pa
import st_reg.states.pe as pe
import st_reg.states.pr as pr
#import st_reg.states.pb as pb
#import st_reg.states.pi as pi
#import st_reg.states.rj as rj
#import st_reg.states.rs as rs
import st_reg.states.rn as rn
#import st_reg.states.rs as rs
#import st_reg.states.ro as ro
import st_reg.states.rr as rr
import st_reg.states.sc as sc
import st_reg.states.sp as sp
import st_reg.states.se as se
import st_reg.states.to as to



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

#BAHIA

def test_ba_validation_right_size_invalid_number_8_digits_and_second_digit_different_6_7_9():
    """Test if a invalid number is really invalid with 8 digits"""

    invalid_number = '12345665'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_8_digits_and_second_digit_different_6_7_9():
    """Test if a valid number is really valid with 8 digits"""

    valid_number = '74694200'
    print ba.check(valid_number)
    assert ba.check(valid_number) == True

def test_ba_validation_right_size_invalid_number_8_digits_and_second_digit_equal_6_7_9():
    """Test if a invalid number is really invalid with 8 digits"""

    invalid_number = '61234559'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_8_digits_and_second_digit_equal_6_7_9():
    """Test if a valid number is really valid with 8 digits"""

    valid_number = '61234557'
    assert ba.check(valid_number) == True

def test_ba_validation_right_size_invalid_number_9_digits_and_second_digit_different_6_7_9():
    """Test if a invalid number is really invalid with 9 digits"""

    invalid_number = '123456749'
    print ba.check(invalid_number)
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_9_digits_and_second_digit_different_6_7_9():
    """Test if a valid number is really valid with 9 digits"""

    valid_number = '123456748'
    assert ba.check(valid_number) == True

def test_ba_validation_right_size_invalid_number_9_digits_and_second_digit_equal_6_7_9():
    """Test if a invalid number is really invalid with 9 digits"""

    invalid_number = '162345652'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_9_digits_and_second_digit_equal_6_7_9():
    """Test if a valid number is really valid with 9 digits"""

    valid_number = '162345651'
    assert ba.check(valid_number) == True

def test_ba_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ba.check(invalid_number) == False

def test_ba_validation_big_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '0030964575'
    assert ba.check(invalid_number) == False

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

# DISTRITO FEDERAL

def test_df_validation_rigth_size_invalid_number():
    """Test if a invalid number is invalid start with 07"""

    invalid_number = '063000100195'
    assert df.check(invalid_number) == False

def test_df_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number= '0716109443381'
    print df.check(invalid_number)
    assert df.check(invalid_number) == False

def test_df_validation_right_size_valid_number():
    """Test if a valid number is really valid"""
    valid= '0716109443382'
    assert df.check(valid) == True

def test_df_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '071610944338'
    assert df.check(invalid_number) == False

def test_df_validation_big_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '07161094433822'
    assert df.check(invalid_number) == False

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

#MARANHÃO

def test_ma_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1220309645'
    assert ma.check(invalid_number) == False

def test_ma_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '1272030'
    assert ma.check(invalid_number) == False

def test_ma_validation_start_different_12():
    """Test if a invalid number start is different 12"""

    invalid_number = '172030964'
    assert ma.check(invalid_number) == False

def test_ma_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '120000387'
    assert ma.check(invalid_number) == False

def test_ma_validation():
    """Test if valid number"""

    valid_number = '120000385'
    assert ma.check(valid_number)

#MATO GROSSO DO SUL

def test_ms_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '2820309645'
    assert ms.check(invalid_number) == False

def test_ms_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '2872030'
    assert ms.check(invalid_number) == False

def test_ms_validation_start_different_28():
    """Test if a invalid number start is different 28"""

    invalid_number = '172030964'
    assert ms.check(invalid_number) == False

def test_ms_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '280000008'
    assert ms.check(invalid_number) == False

def test_ms_validation():
    """Test if valid number"""

    valid_number = '280000006'
    assert ms.check(valid_number)

#PARA

def test_pa_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pa.check(invalid_number) == False

def test_pa_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pa.check(invalid_number) == False

def test_pa_validation_start_different_15():
    """Test if a invalid number start is different 15"""

    invalid_number = '172030964'
    assert pa.check(invalid_number) == False

def test_pa_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '159999990'
    assert pa.check(invalid_number) == False

def test_pa_validation():
    """Test if valid number"""

    valid_number = '159999995'
    assert pa.check(valid_number)

#PERNAMBUCO

def test_pe_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pe.check(invalid_number) == False

def test_pe_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pe.check(invalid_number) == False

def test_pe_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '032141830'
    assert pe.check(invalid_number) == False

def test_pe_validation():
    """Test if valid number"""

    valid_number = '032141840'
    assert pe.check(valid_number)

#PARANÁ

def test_pr_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '15203096458'
    assert pr.check(invalid_number) == False

def test_pr_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pr.check(invalid_number) == False

def test_pr_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '1234567857'
    assert pr.check(invalid_number) == False

def test_pr_validation():
    """Test if valid number"""

    valid_number = '1234567850'
    assert pr.check(valid_number)

#RIO GRANDE DO NORTE

def test_rn_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '20172030964577'
    assert rn.check(invalid_number) == False

def test_rn_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '207030'
    assert rn.check(invalid_number) == False

def test_rn_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '200400405'
    assert rn.check(invalid_number) == False

def test_rn_validation():
    """Test if valid number"""

    valid_number = '200400401'
    assert rn.check(valid_number)

#RORAIMA

def test_rr_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert rr.check(invalid_number) == False

def test_rr_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert rr.check(invalid_number) == False

def test_rr_validation_start_different_24():
    """Test if a invalid number start is different 24"""

    invalid_number = '172030964'
    assert rr.check(invalid_number) == False

def test_rr_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '240013406'
    assert rr.check(invalid_number) == False

def test_rr_validation():
    """Test if valid number"""

    valid_number = '240061536'
    assert rr.check(valid_number)

#SANTA CATARINA

def test_sc_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert sc.check(invalid_number) == False

def test_sc_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert sc.check(invalid_number) == False

def test_sc_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '251040858'
    assert sc.check(invalid_number) == False

def test_sc_validation():
    """Test if valid number"""

    valid_number = '251040852'
    assert sc.check(valid_number)

#SERGIPE

def test_se_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert se.check(invalid_number) == False

def test_se_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert se.check(invalid_number) == False

def test_se_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '271234566'
    assert se.check(invalid_number) == False

def test_se_validation():
    """Test if valid number"""

    valid_number = '271234563'
    assert se.check(valid_number)

#SÃO PAULO

def test_sp_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert sp.check(invalid_number) == False

def test_sp_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert sp.check(invalid_number) == False


def test_sp_validation_digit_verification_with_12_digits():
    """Test if digit verification is invalid"""

    invalid_number = '110042490115'
    assert sp.check(invalid_number) == False

def test_sp_validation_digit_verification_with_13_digits():
    """Test if digit verification is invalid"""

    invalid_number = 'P011004248003'
    assert sp.check(invalid_number) == False

def test_sp_validation_start_different_P_with_13_digits():
    """Test if a invalid number start is different P"""

    invalid_number = 'U172030964897'
    assert sp.check(invalid_number) == False

def test_sp_validation_with_12_digits():
    """Test if valid number"""

    valid_number = '110042490114'
    assert sp.check(valid_number)

def test_sp_validation_with_13_digits():
    """Test if valid number"""

    valid_number = 'P011004243002'
    assert sp.check(valid_number)


#TOCANTINS

def test_to_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert to.check(invalid_number) == False

def test_to_validation_small_size_number():
    """Test if a invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert to.check(invalid_number) == False

def test_to_validation_third_and_fourth_digit():
    """Test if invalid third and fourth digit"""

    invalid_number = '06087879999'
    assert to.check(invalid_number) == False

def test_to_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '29010227833'
    assert to.check(invalid_number) == False

def test_to_validation():
    """Test if valid number"""

    valid_number = '29010227836'
    assert to.check(valid_number)

