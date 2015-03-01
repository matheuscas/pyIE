Validation of Brazilian States Registrations
=====================

Validation of brazilian state registration numbers.

**Current release: 1.0.8**

[![Build Status](https://travis-ci.org/matheuscas/pyIE.svg?branch=master)](https://travis-ci.org/matheuscas/pyIE)

How to install it:
--------------

``` python
pip install ie
```


How to use it:
--------------

``` python
>>>>> from ie import checking
>>>>> acre_state_registration_number = '0172030964575'
>>>>> acre_abbreviation = 'AC'
>>>>> result = checking.start(acre_state_registration_number, acre_abbreviation)
>>>>> print result
>>>>> True
```

That's it! You just have to pass the state abbreviation and the state number registration. Below you can see the entire states abbreviation table from Brazil.

``` python
AC (Acre)
AL (Alagoas)
AM (Amazonas)
AP (Amapa)
BA (Bahia)
CE (Ceara)
DF (Distrito Federal)
ES (Espirito Santo)
GO (Goias)
MA (Maranhao)
MG (Minas Gerais)
MS (Mato Grosso do Sul)
MT (Mato Grosso)
PA (Para)
PB (Paraiba)
PE (Pernambuco)
PI (Piaui)
PR (Parana)
RJ (Rio de Janeiro)
RN (Rio Grande do Norte)
RO (Rondonia)
RR (Roraima)
RS (Rio Grande do Sul)
SC (Santa Catarina)
SE (Sergipe)
SP (Sao Paulo)
TO (Tocantins)  
```

Portuguese
--------------

Validação das inscrições estaduais de todos os estados brasileiros.


Como installar:
--------------

``` python
pip install ie
```

Como utilizar:
--------------

**Versão atual: 1.0.8**

``` python
>>>>> from ie import checking
>>>>> alagoas_state_registration_number = '1720309645'
>>>>> alagoas_abbreviation = 'AL'
>>>>> result = checking.start(alagoas_state_registration_number, alagoas_abbreviation)
>>>>> print result
>>>>> False
```
É isso! Você apenas tem que passar o número que tem que ser verificado e a sigla do Estado. Acima você pode ver a tabela de siglas dos estados do Brasil.


