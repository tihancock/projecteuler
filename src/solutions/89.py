from string import split, replace
from copy import copy

def minimalRomanNumeral(roman_num):
    roman_num=replace(roman_num,"DD","M")
    roman_num=replace(roman_num,"DCCCC","CM")
    roman_num=replace(roman_num,"CCCC","CD")
    roman_num=replace(roman_num,"LL","C")
    roman_num=replace(roman_num,"LXXXX","XC")
    roman_num=replace(roman_num,"XXXXX","L")
    roman_num=replace(roman_num,"XXXX","XL")
    roman_num=replace(roman_num,"VV","X")
    roman_num=replace(roman_num,"VIIII","IX")
    roman_num=replace(roman_num,"IIIII","V")
    roman_num=replace(roman_num,"IIII","IV")

    return roman_num

lines=split(open('files/roman.txt','r').read(),'\r\n')

print sum([len(l)-len(minimalRomanNumeral(l)) for l in lines])
