#!/usr/bin/env python
# -*- coding: utf-8 -*-

def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
    roman = ''
    romanmappings = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                     40: "XL", 50: "L", 90: "XC", 100: "C",
                     400: "CD", 500: "D", 900: "CM", 1000: "M" }
    for intVal in sorted(romanmappings.keys(), reverse=True):
        while number >= intVal:
            roman += romanmappings[intVal]
            number -= intVal
    return roman


if __name__ == '__main__':
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    print 'All ok'
