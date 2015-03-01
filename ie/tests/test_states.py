# -*- coding: utf-8 -*-
"""File to test states validations"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import ie.states.ac as ac
import ie.states.al as al
import ie.states.am as am
import ie.states.ap as ap
import ie.states.ba as ba
import ie.states.ce as ce
import ie.states.df as df
import ie.states.es as es
import ie.states.go as go
import ie.states.ma as ma
import ie.states.mt as mt
import ie.states.ms as ms
import ie.states.mg as mg
import ie.states.pa as pa
import ie.states.pe as pe
import ie.states.pr as pr
import ie.states.pb as pb
import ie.states.pi as pi
import ie.states.rj as rj
import ie.states.rn as rn
import ie.states.rs as rs
import ie.states.ro as ro
import ie.states.rr as rr
import ie.states.sc as sc
import ie.states.sp as sp
import ie.states.se as se
import ie.states.to as to


#ACRE
def test_ac_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '0172030964577'
    assert ac.start(invalid_number) == False


def test_ac_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '0172030964575'
    assert ac.start(valid_number)


def test_ac_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ac.start(invalid_number) == False


def test_ac_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '01720309645755'
    assert ac.start(invalid_number) == False


#ALAGOAS
def test_al_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert al.start(invalid_number) == False


def test_al_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert al.start(invalid_number) == False


def test_al_validation_start_different_24():
    """Test if an invalid number start is different 24"""

    invalid_number = '172030964'
    assert al.start(invalid_number) == False


def test_al_validation_third_digit_corresponds_to_type_of_company():
    """Test if invalid when the third digit is different to 0_3_5_7_8"""

    invalid_number = '172030964'
    assert al.start(invalid_number) == False


def test_al_validation_check_digit():
    """Test if invalid the check digit calculation"""

    invalid_number = '240071779'
    assert al.start(invalid_number) == False


#AMAZONAS
def test_am_validation_right_size_valid_number():
    """Test if an valid number is really valid"""

    valid_number = '100000010'
    assert am.start(valid_number) == True


def test_am_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '9999999999'
    assert am.start(invalid_number) == False


def test_am_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '99999999'
    assert am.start(invalid_number) == False


#AMAPÁ
def test_ap_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert ap.start(invalid_number) == False


def test_ap_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ap.start(invalid_number) == False


def test_ap_validation_start_different_03():
    """Test if an invalid number start is different 03"""

    invalid_number = '172030964'
    assert ap.start(invalid_number) == False


def test_ap_validation_check_digit():
    """Test if invalid the check digit calculation"""

    invalid_number = '030123456'
    assert ap.start(invalid_number) == False


def test_ap_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '030123459'
    assert ap.start(valid_number)


#BAHIA
def test_ba_validation_right_size_invalid_number_8_digits_and_second_digit_different_6_7_9():
    """Test if an invalid number is really invalid with 8 digits"""

    invalid_number = '12345665'
    assert ba.start(invalid_number) == False


def test_ba_validation_right_size_valid_number_8_digits_and_second_digit_different_6_7_9():
    """Test if a valid number is really valid with 8 digits"""

    valid_number = '74694200'
    assert ba.start(valid_number) == True


def test_ba_validation_right_size_invalid_number_8_digits_and_second_digit_equal_6_7_9():
    """Test if an invalid number is really invalid with 8 digits"""

    invalid_number = '61234559'
    assert ba.start(invalid_number) == False


def test_ba_validation_right_size_valid_number_8_digits_and_second_digit_equal_6_7_9():
    """Test if a valid number is really valid with 8 digits"""

    valid_number = '61234557'
    assert ba.start(valid_number) == True


def test_ba_validation_right_size_invalid_number_9_digits_and_second_digit_different_6_7_9():
    """Test if an invalid number is really invalid with 9 digits"""

    invalid_number = '123456749'
    assert ba.start(invalid_number) == False


def test_ba_validation_right_size_valid_number_9_digits_and_second_digit_different_6_7_9():
    """Test if a valid number is really valid with 9 digits"""

    valid_number = '123456748'
    assert ba.start(valid_number) == True


def test_ba_validation_right_size_invalid_number_9_digits_and_second_digit_equal_6_7_9():
    """Test if an invalid number is really invalid with 9 digits"""

    invalid_number = '162345652'
    assert ba.start(invalid_number) == False


def test_ba_validation_right_size_valid_number_9_digits_and_second_digit_equal_6_7_9():
    """Test if a valid number is really valid with 9 digits"""

    valid_number = '162345651'
    assert ba.start(valid_number) == True


def test_ba_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ba.start(invalid_number) == False


def test_ba_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0030964575'
    assert ba.start(invalid_number) == False


#CEARÁ
def test_ce_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert ce.start(invalid_number) == False


def test_ce_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert ce.start(invalid_number) == False


def test_ce_validation_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '060000014'
    assert ce.start(invalid_number) == False


def test_ce_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '060000015'
    assert ce.start(valid_number)


#DISTRITO FEDERAL
def test_df_validation_right_size_invalid_number_star_with_07():
    """Test if a invalid number is really invalid. The state registration must start with 07"""

    invalid_number = '063000100195'
    assert df.start(invalid_number) == False


def test_df_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid. The number start 07"""

    invalid_number = '0716109443381'
    assert df.start(invalid_number) == False


def test_df_validation_right_size_valid_number():
    """Test if a valid number is really valid"""
    valid = '0716109443382'
    assert df.start(valid) == True


def test_df_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '071610944338'
    assert df.start(invalid_number) == False


def test_df_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '07161094433822'
    assert df.start(invalid_number) == False


#ESPÍRITO SANTO
def test_es_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1720309645'
    assert es.start(invalid_number) == False


def test_es_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0172030'
    assert es.start(invalid_number) == False


def test_es_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '999999991'
    assert es.start(invalid_number) == False


def test_es_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '999999990'
    assert es.start(valid_number)


#GOIAS
def test_go_validation_invalid_number_different_starting_of_10_11_15():
    """Test if the first two digits are different from 10,11,15"""

    invalid_number = '135236987'
    assert go.start(invalid_number) == False


def test_go_validation_right_size_invalid_number():
    """Test if a invalid number is really invalid"""

    invalid_number = '113636921'
    assert go.start(invalid_number) == False


def test_go_validation_right_size_valid_number_not_in_interval_10103105_the_10119997():
    """Test if a valid number is really valid rest = 1 and number not be in interval (10103105, 10119997)"""

    valid_number = '113636920'
    assert go.start(valid_number) == True


def test_go_validation_right_size_valid_number_in_interval_10103105_the_10119997():
    """Test if a valid number is really valid rest = 1 and number interval (10103105, 10119997)"""
    valid_number = '101199961'
    assert go.start(valid_number) == True


def test_go_validation_right_size_valid_number_digit_verifier_equal_the_zero():
    """Test if a valid number is really valid com digit verifier equal to zero"""
    valid_number = '110010000'
    assert go.start(valid_number) == True


def test_go_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '10119996'
    assert go.start(invalid_number) == False


def test_go_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1011999611'
    assert go.start(invalid_number) == False


#MARANHÃO
def test_ma_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1220309645'
    assert ma.start(invalid_number) == False


def test_ma_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1272030'
    assert ma.start(invalid_number) == False


def test_ma_validation_start_different_12():
    """Test if an invalid number start is different 12"""

    invalid_number = '172030964'
    assert ma.start(invalid_number) == False


def test_ma_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '120000387'
    assert ma.start(invalid_number) == False


def test_ma_validation_valid_digit_verification():
    """Test if a valid number is really valid"""

    valid_number = '120000385'
    assert ma.start(valid_number)


#MATO GROSSO
def test_mt_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '95192196672'
    assert mt.start(invalid_number) == False


def test_mt_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '00130000019'
    assert mt.start(valid_number) == True


def test_mt_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0013000001'
    assert mt.start(invalid_number) == False


def test_mt_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '10119996111'
    assert mt.start(invalid_number) == False


#MATO GROSSO DO SUL
def test_ms_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '2820309645'
    assert ms.start(invalid_number) == False


def test_ms_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '2872030'
    assert ms.start(invalid_number) == False


def test_ms_validation_start_different_28():
    """Test if an invalid number start is different 28"""

    invalid_number = '172030964'
    assert ms.start(invalid_number) == False


def test_ms_validation_invalid_digit_verification():
    """Test if invalid digit verification is really invalid"""

    invalid_number = '280000008'
    assert ms.start(invalid_number) == False


def test_ms_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '280000006'
    assert ms.start(valid_number) == True


#MINAS GERAIS
def test_mg_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '5055050000003'
    assert mg.start(invalid_number) == False


def test_mg_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid = '4351289641815'
    assert mg.start(valid) == True


def test_mg_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '505505000000'
    assert mg.start(invalid_number) == False


def test_mg_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '50550500000053'
    assert mg.start(invalid_number) == False


#PARA
def test_pa_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pa.start(invalid_number) == False


def test_pa_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pa.start(invalid_number) == False


def test_pa_validation_start_different_15():
    """Test if an invalid number start is different 15"""

    invalid_number = '172030964'
    assert pa.start(invalid_number) == False


def test_pa_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '159999990'
    assert pa.start(invalid_number) == False


def test_pa_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '159999995'
    assert pa.start(valid_number)


#PARAIBA
def test_pb_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '060000014'
    assert pb.start(invalid_number) == False


def test_pb_validation_right_size_valid_number():
    """Test if a valid number is really valid"""

    valid_number = '060000015'
    assert pb.start(valid_number) == True


def test_pb_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '06000001'
    assert pb.start(invalid_number) == False


def test_pb_validation_big_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '0600000151'
    assert pb.start(invalid_number) == False


#PERNAMBUCO
def test_pe_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pe.start(invalid_number) == False


def test_pe_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pe.start(invalid_number) == False


def test_pe_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '032141830'
    assert pe.start(invalid_number) == False


def test_pe_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '032141840'
    assert pe.start(valid_number)


#PIAUÍ
def test_pi_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '1520309645'
    assert pi.start(invalid_number) == False


def test_pi_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pi.start(invalid_number) == False


def test_pi_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '012345670'
    assert pi.start(invalid_number) == False


def test_pi_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '012345679'
    assert pi.start(valid_number)


#PARANÁ
def test_pr_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '15203096458'
    assert pr.start(invalid_number) == False


def test_pr_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert pr.start(invalid_number) == False


def test_pr_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '1234567857'
    assert pr.start(invalid_number) == False


def test_pr_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '1234567850'
    assert pr.start(valid_number)


#RIO DE JANEIRO
def test_rj_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '15203096458'
    assert rj.start(invalid_number) == False


def test_rj_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '1572030'
    assert rj.start(invalid_number) == False


def test_rj_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '10022001'
    assert rj.start(invalid_number) == False


def test_rj_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '10022002'
    assert rj.start(valid_number)


def test_rn_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '20172030964577'
    assert rn.start(invalid_number) == False


def test_rn_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '207030'
    assert rn.start(invalid_number) == False


def ttest_rn_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '200400405'
    assert rn.start(invalid_number) == False


def test_rn_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '200400401'
    assert rn.start(valid_number)


#RONDÔNIA
def test_ro_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '201728030964577'
    assert ro.start(invalid_number) == False


def test_ro_validation_small_size_invalid_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '207030'
    assert ro.start(invalid_number) == False


def test_ro_validation_invalid_digit_verification_with_9_digits():
    """Test if digit verification is invalid"""

    invalid_number = '101625218'
    assert ro.start(invalid_number) == False


def test_ro_validation_valid_number_with_9_digits_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '101625213'
    assert ro.start(valid_number)


def test_ro_validation_invalid_digit_verification_with_14_digits():
    """Test if invalid digit verification is really invalid"""

    invalid_number = '00000000625215'
    assert ro.start(invalid_number) == False


def test_ro_validation_valid_number_with_14_digits_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '00000000625213'
    assert ro.start(valid_number)


#RORAIMA
def test_rr_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert rr.start(invalid_number) == False


def test_rr_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert rr.start(invalid_number) == False


def test_rr_validation_start_different_24():
    """Test if an invalid number start is different 24"""

    invalid_number = '172030964'
    assert rr.start(invalid_number) == False


def test_rr_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '240013406'
    assert rr.start(invalid_number) == False


def test_rr_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '240061536'
    assert rr.start(valid_number)


#RIO GRANDE DO SUL
def test_rs_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert rs.start(invalid_number) == False


def test_rs_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert rs.start(invalid_number) == False


def test_rs_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '2243658791'
    assert rs.start(invalid_number) == False


def test_rs_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '2243658792'
    assert rs.start(valid_number)


#SANTA CATARINA
def test_sc_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert sc.start(invalid_number) == False


def test_sc_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert sc.start(invalid_number) == False


def test_sc_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '251040858'
    assert sc.start(invalid_number) == False


def test_sc_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '251040852'
    assert sc.start(valid_number)


#SERGIPE
def test_se_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert se.start(invalid_number) == False


def test_se_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert se.start(invalid_number) == False


def test_se_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '271234566'
    assert se.start(invalid_number) == False


def test_se_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '271234563'
    assert se.start(valid_number)


#SÃO PAULO
def test_sp_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert sp.start(invalid_number) == False


def test_sp_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert sp.start(invalid_number) == False


def test_sp_validation_digit_verification_with_12_digits():
    """Test if digit verification is invalid"""

    invalid_number = '110042490115'
    assert sp.start(invalid_number) == False


def test_sp_validation_digit_verification_with_13_digits():
    """Test if digit verification is invalid"""

    invalid_number = 'P011004248003'
    assert sp.start(invalid_number) == False


def test_sp_validation_start_different_P_with_13_digits():
    """Test if an invalid number start is different P"""

    invalid_number = 'U172030964897'
    assert sp.start(invalid_number) == False


def test_sp_validation_valid_number_with_12_digits_is_really_valid():
    """Test if a valid number with 12 digits is really valid"""

    valid_number = '110042490114'
    assert sp.start(valid_number)


def test_sp_validation_valid_number_with_13_digits_is_really_valid():
    """Test if a valid number with 13 digits is really valid"""

    valid_number = 'P011004243002'
    assert sp.start(valid_number)


#TOCANTINS
def test_to_validation_right_size_invalid_number():
    """Test if an invalid number is really invalid"""

    invalid_number = '24172030964577'
    assert to.start(invalid_number) == False


def test_to_validation_small_size_number():
    """Test if an invalid number, with wrong size, is really invalid"""

    invalid_number = '247030'
    assert to.start(invalid_number) == False


def test_to_validation_invalid_number_with_third_and_fourth_digit_different_01_02_03_99():
    """Test if invalid number with third and fourth digit different of 01, 02, 03 e 99"""

    invalid_number = '06087879999'
    assert to.start(invalid_number) == False


def test_to_validation_invalid_digit_verification():
    """Test if digit verification is invalid"""

    invalid_number = '29010227833'
    assert to.start(invalid_number) == False


def test_to_validation_valid_number_is_really_valid():
    """Test if a valid number is really valid"""

    valid_number = '29010227836'
    assert to.start(valid_number)
