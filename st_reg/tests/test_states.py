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
import st_reg.states.go as go
import st_reg.states.ma as ma
import st_reg.states.mt as mt
import st_reg.states.ms as ms
import st_reg.states.mg as mg
import st_reg.states.pa as pa
import st_reg.states.pe as pe
import st_reg.states.pr as pr
import st_reg.states.pb as pb
import st_reg.states.pi as pi
import st_reg.states.rj as rj
import st_reg.states.rn as rn
import st_reg.states.rs as rs
import st_reg.states.ro as ro
import st_reg.states.rr as rr
import st_reg.states.sc as sc
import st_reg.states.sp as sp
import st_reg.states.se as se
import st_reg.states.to as to

#ACRE
def test_ac_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '0172030964577'
    assert ac.check(invalid_number) == False

def test_ac_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '0172030964575'
    assert ac.check(valid_number)

def test_ac_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ac.check(invalid_number) == False

def test_ac_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '01720309645755'
    assert ac.check(invalid_number) == False

#ALAGOAS
def test_al_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert al.check(invalid_number) == False

def test_al_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert al.check(invalid_number) == False

def test_al_validation_start_different_24():
    """Test if an invalid number start is different 24"""

    invalid_number = '172030964'
    assert al.check(invalid_number) == False

def test_al_validation_third_digit_corresponds_to_type_of_company():
    """Test if invalid when the third digit is different to 0 or 3 or 5 or 7 or 8"""

    invalid_number = '172030964'
    assert al.check(invalid_number) == False

def test_al_validation_check_digit():
    """Test if invalid the check digit calculation"""

    invalid_number = '240071779'
    assert al.check(invalid_number) == False

#AMAZONAS
def test_am_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '999999999'
    assert am.check(invalid_number) == False

def test_am_validation_right_size_valid_number():
    """Test if an valid number is really valid"""

    valid_number = '100000010'
    assert am.check(valid_number) == True

def test_am_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '9999999999'
    assert am.check(invalid_number) == False

def test_am_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number ='99999999'
    assert am.check(invalid_number) == False

#AMAPÁ
def test_ap_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert ap.check(invalid_number) == False

def test_ap_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ap.check(invalid_number) == False

def test_ap_validation_start_different_03():
    """Test if an invalid number start is different 03"""

    invalid_number = '172030964'
    assert ap.check(invalid_number) == False

def test_ap_validation_check_digit():
    """Test if invalid the check digit calculation"""

    invalid_number = '030123456'
    assert ap.check(invalid_number) == False

def test_ap_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '030123459'
    assert ap.check(valid_number)

#BAHIA
def test_ba_validation_right_size_invalid_number_8_digits_and_second_digit_different_6_7_9():
    """Test if an invalid number is really invalid with 8 digits"""

    invalid_number = '12345665'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_8_digits_and_second_digit_different_6_7_9():
    """Test if a valid number is really valid with 8 digits"""

    valid_number = '74694200'
    assert ba.check(valid_number) == True

def test_ba_validation_right_size_invalid_number_8_digits_and_second_digit_equal_6_7_9():
    """Test if an invalid number is really invalid with 8 digits"""

    invalid_number = '61234559'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_8_digits_and_second_digit_equal_6_7_9():
    """Test if a valid number is really valid with 8 digits"""

    valid_number = '61234557'
    assert ba.check(valid_number) == True

def test_ba_validation_right_size_invalid_number_9_digits_and_second_digit_different_6_7_9():
    """Test if an invalid number is really invalid with 9 digits"""

    invalid_number = '123456749'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_9_digits_and_second_digit_different_6_7_9():
    """Test if a valid number is really valid with 9 digits"""

    valid_number = '123456748'
    assert ba.check(valid_number) == True

def test_ba_validation_right_size_invalid_number_9_digits_and_second_digit_equal_6_7_9():
    """Test if an invalid number is really invalid with 9 digits"""

    invalid_number = '162345652'
    assert ba.check(invalid_number) == False

def test_ba_validation_right_size_valid_number_9_digits_and_second_digit_equal_6_7_9():
    """Test if a valid number is really valid with 9 digits"""

    valid_number = '162345651'
    assert ba.check(valid_number) == True

def test_ba_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ba.check(invalid_number) == False

def test_ba_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0030964575'
    assert ba.check(invalid_number) == False

#CEARÁ
def test_ce_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert ce.check(invalid_number) == False

def test_ce_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ce.check(invalid_number) == False

def test_ce_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '060000014'
    assert ce.check(invalid_number) == False

def test_ce_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '060000015'
    assert ce.check(valid_number)

#DISTRITO FEDERAL
def test_df_validation_starting_with_07():
    """Test if a invalid number is invalid start with 07"""

    invalid_number = '063000100195'
    assert df.check(invalid_number) == False

def test_df_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number= '0716109443381'
    assert df.check(invalid_number) == False

def test_df_validation_right_size_valid_number():
    """Test if a valid number is really valid"""
    valid= '0716109443382'
    assert df.check(valid) == True

def test_df_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '071610944338'
    assert df.check(invalid_number) == False

def test_df_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '07161094433822'
    assert df.check(invalid_number) == False

#ESPÍRITO SANTO
def test_es_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert es.check(invalid_number) == False

def test_es_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert es.check(invalid_number) == False

def test_es_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '999999991'
    assert es.check(invalid_number) == False

def test_es_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '999999990'
    assert es.check(valid_number)


#GOIAS
def test_go_validation_invalid_number_different_starting_of_10_11_15():
    """Test if the first two digits are different from 10,11,15"""

    invalid_number = '135236987'
    assert go.check(invalid_number) == False

def test_go_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '113636921'
    assert go.check(invalid_number) == False

def test_go_validation_right_size_valid_number():
    """Test if a valid number is really valid rest = 1 and number not be in (10103105, 10119997)"""

    valid_number = '113636920'
    assert go.check(valid_number) == True

#REFATORAR
#ESSE TESTE É IGUAL AO ANTERIOR? A ASSINATURA ESTÁ IGUAL
def test_go_validation_right_size_valid_number():
    """Test if a valid number is really valid rest = 1 and number in (10103105, 10119997)"""
    valid_number = '101199961'
    assert go.check(valid_number) == True

#REFATORAR
#ESSE TESTE É IGUAL AO ANTERIOR? A ASSINATURA ESTÁ IGUAL
def test_go_validation_right_size_valid_number():
    """Test if a valid number is really valid rest = 0"""
    valid_number = '110010000'
    assert go.check(valid_number) == True

def test_go_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '10119996'
    assert go.check(invalid_number) == False

def test_go_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1011999611'
    assert go.check(invalid_number) == False


#MARANHÃO
def test_ma_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1220309645'
    assert ma.check(invalid_number) == False

def test_ma_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1272030'
    assert ma.check(invalid_number) == False

def test_ma_validation_start_different_12():
    """Test if an invalid number start is different 12"""

    invalid_number = '172030964'
    assert ma.check(invalid_number) == False

def test_ma_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '120000387'
    assert ma.check(invalid_number) == False

def test_ma_validation_valid_digit_verification():
    """Test if a valid number is really valid"""

    valid_number = '120000385'
    assert ma.check(valid_number)

#MATO GROSSO
def test_mt_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '95192196672'
    assert mt.check(invalid_number) == False

def test_mt_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '00130000019'
    assert mt.check(valid_number) == True

def test_mt_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0013000001'
    assert mt.check(invalid_number) == False

def test_mt_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '10119996111'
    assert mt.check(invalid_number) == False

#MATO GROSSO DO SUL
def test_ms_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '2820309645'
    assert ms.check(invalid_number) == False

def test_ms_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '2872030'
    assert ms.check(invalid_number) == False

def test_ms_validation_start_different_28():
    """Test if an invalid number start is different 28"""

    invalid_number = '172030964'
    assert ms.check(invalid_number) == False

def test_ms_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '280000008'
    assert ms.check(invalid_number) == False

def test_ms_validation_valid_number_is_really_valid():
   """Test if a valid number is really valid"""

    valid_number = '280000006'
    assert ms.check(valid_number)

# MINAS GERAIS
def test_mg_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '5055050000003'
    assert mg.check(invalid_number) == False

def test_mg_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid = '4351289641815'
    assert mg.check(valid) == True

def test_mg_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '505505000000'
    assert mg.check(invalid_number) == False

def test_mg_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '50550500000053'
    assert mg.check(invalid_number) == False

#PARA
def test_pa_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pa.check(invalid_number) == False

def test_pa_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pa.check(invalid_number) == False

def test_pa_validation_start_different_15():
    """Test if an invalid number start is different 15"""

    invalid_number = '172030964'
    assert pa.check(invalid_number) == False

def test_pa_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '159999990'
    assert pa.check(invalid_number) == False

def test_pa_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '159999995'
    assert pa.check(valid_number)

#PARAIBA
def test_pb_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '060000014'
    assert pb.check(invalid_number) == False

def test_pb_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '060000015'
    assert pb.check(valid_number) == True

def test_pb_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '06000001'
    assert pb.check(invalid_number) == False

def test_pb_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0600000151'
    assert pb.check(invalid_number) == False

#PERNAMBUCO
def test_pe_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pe.check(invalid_number) == False

def test_pe_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pe.check(invalid_number) == False

def test_pe_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '032141830'
    assert pe.check(invalid_number) == False

def test_pe_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '032141840'
    assert pe.check(valid_number)

#PIAUÍ
def test_pi_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pi.check(invalid_number) == False

def test_pi_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pi.check(invalid_number) == False

def test_pi_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '012345670'
    assert pi.check(invalid_number) == False

def test_pi_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '012345679'
    assert pi.check(valid_number)

#PARANÁ
def test_pr_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '15203096458'
    assert pr.check(invalid_number) == False

def test_pr_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pr.check(invalid_number) == False

def test_pr_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '1234567857'
    assert pr.check(invalid_number) == False

def test_pr_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '1234567850'
    assert pr.check(valid_number)

#RIO DE JANEIRO
def test_rj_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '15203096458'
    assert rj.check(invalid_number) == False

def test_rj_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert rj.check(invalid_number) == False

def test_rj_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '10022001'
    assert rj.check(invalid_number) == False

def test_rj_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '10022002'
    assert rj.check(valid_number)

def test_rn_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '20172030964577'
    assert rn.check(invalid_number) == False

def test_rn_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '207030'
    assert rn.check(invalid_number) == False

def ttest_rn_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '200400405'
    assert rn.check(invalid_number) == False

def test_rn_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '200400401'
    assert rn.check(valid_number)

#RONDÔNIA
def test_ro_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '201728030964577'
    assert ro.check(invalid_number) == False

def test_ro_validation_small_size_invalid_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '207030'
    assert ro.check(invalid_number) == False

def test_ro_validation_invalid_digit_verification_with_9_digits():
    """Test if digit verification is invalid"""

    invalid_number = '101625218'
    assert ro.check(invalid_number) == False

def test_ro_validation_valid_number_with_9_digits_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '101625213'
    assert ro.check(valid_number)

def test_ro_validation_invalid_digit_verification_with_14_digits():
    """Test if invalid digit verification is really invalid"""

    invalid_number = '00000000625215'
    assert ro.check(invalid_number) == False

def test_ro_validation_valid_number_with_14_digits_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '00000000625213'
    assert ro.check(valid_number)

#RORAIMA

def test_rr_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert rr.check(invalid_number) == False

def test_rr_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert rr.check(invalid_number) == False

def test_rr_validation_start_different_24():
    """Test if an invalid number start is different 24"""

    invalid_number = '172030964'
    assert rr.check(invalid_number) == False

def test_rr_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '240013406'
    assert rr.check(invalid_number) == False

def test_rr_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '240061536'
    assert rr.check(valid_number)

#RIO GRANDE DO SUL
def test_rs_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert rs.check(invalid_number) == False

def test_rs_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert rs.check(invalid_number) == False

def test_rs_validation_invalid_digit_verification ():
    """Test if digit verification is invalid"""

    invalid_number = '2243658791'
    assert rs.check(invalid_number) == False

def test_rs_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '2243658792'
    assert rs.check(valid_number)

#SANTA CATARINA
def test_sc_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert sc.check(invalid_number) == False

def test_sc_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert sc.check(invalid_number) == False

def test_sc_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '251040858'
    assert sc.check(invalid_number) == False

def test_sc_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '251040852'
    assert sc.check(valid_number)

#SERGIPE
def test_se_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert se.check(invalid_number) == False

def test_se_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert se.check(invalid_number) == False

def test_se_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '271234566'
    assert se.check(invalid_number) == False

def test_se_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '271234563'
    assert se.check(valid_number)

#SÃO PAULO
def test_sp_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert sp.check(invalid_number) == False

def test_sp_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

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
    """Test if an invalid number start is different P"""

    invalid_number = 'U172030964897'
    assert sp.check(invalid_number) == False

def test_sp_validation_valid_number_with_12_digits_is_really_valid():
    """Test if a valid number with 12 digits is really valid"""

    valid_number = '110042490114'
    assert sp.check(valid_number)

def test_sp_validation_valid_number_with_13_digits_is_really_valid():
    """Test if a valid number with 13 digits is really valid"""

    valid_number = 'P011004243002'
    assert sp.check(valid_number)


#TOCANTINS
def test_to_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert to.check(invalid_number) == False

def test_to_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert to.check(invalid_number) == False

def test_to_validation_invalid_number_with_third_and_fourth_digit_different_01_02_03_99():
    """Test if invalid number with third and fourth digit different of 01, 02, 03 e 99"""

    invalid_number = '06087879999'
    assert to.check(invalid_number) == False

def test_to_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '29010227833'
    assert to.check(invalid_number) == False

def test_to_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '29010227836'
    assert to.check(valid_number)

