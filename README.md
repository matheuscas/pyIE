Validation of Brazilian States Registrations
=====================

Consistency validation of brazilian state registration numbers.

**Current release: 1.0.1**

[![Build Status](https://travis-ci.org/matheuscas/br-state_registration.png?branch=master)](https://travis-ci.org/matheuscas/br-state_registration)

How to use it:
--------------

``` python
>>>>> from st_reg import consistency
>>>>> acre_state_registration_number = '0172030964575'
>>>>> acre_index_number = 1
>>>>> result = consistency.check(acre_state_registration_number, acre_index_number)
>>>>> print result
>>>>> True
```

That's it! You just have to pass the number that has to be checked and pass an integer that represents the state. Below you can see the entire index table of the states from Brazil.

``` python
1 => AC (Acre)
2 => AL (Alagoas)
3 => AM (Amazonas)
4 => AP (Amapa)
5 => BA (Bahia)
6 => CE (Ceara)
7 => DF (Distrito Federal)
8 => ES (Espirito Santo)
9 => GO (Goias)
10 => MA (Maranhao)
11 => MG (Minas Gerais)
12 => MS (Mato Grosso do Sul)
13 => MT (Mato Grosso)
14 => PA (Para)
15 => PB (Paraiba)
16 => PE (Pernambuco)
17 => PI (Piaui)
18 => PR (Parana)
19 => RJ (Rio de Janeiro)
20 => RN (Rio Grande do Norte)
21 => RO (Rondonia)
22 => RR (Roraima)
23 => RS (Rio Grande do Sul)
24 => SC (Santa Catarina)
25 => SE (Sergipe)
26 => SP (Sao Paulo)
27 => TO (Tocantins)  
```

Portuguese
--------------

Validação da consistência dos números das inscrições estaduais brasileiras

Como utilizar:

**Versão atual: 1.0.1**

``` python
>>>>> from st_reg import consistency
>>>>> alagoas_state_registration_number = '1720309645'
>>>>> alagoas_index_number = 2
>>>>> result = consistency.check(alagoas_state_registration_number, alagoas_index_number)
>>>>> print result
>>>>> False
```
É isso! Você apenas tem que passar o número que tem que ser verificado e passar um inteiro que representa o Estado. Acima você pode ver a tabela de índice inteiro dos estados do Brasil.


