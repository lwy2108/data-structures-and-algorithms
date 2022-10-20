"""
Given an integer, return it as a roman numeral.
"""


def array_map_int_to_rom(num):
    ints = [
        1000,
        900,
        500,
        400,
        100,
        90,
        50,
        40,
        10,
        9,
        5,
        4,
        1
    ]

    roms = [
        'M',
        'CM',
        'D',
        'CD',
        'C',
        'XC',
        'L',
        'XL',
        'X',
        'IX',
        'V',
        'IV',
        'I'
    ]

    res = ""

    for i in range(len(ints)):
        count = num // ints[i]
        num -= count * ints[i]
        res += count * roms[i]

    return res
  
  
# test cases
print(3, "Pass" if array_map_int_to_rom(3) == "III" else "Fail")
print(58, "Pass" if array_map_int_to_rom(58) == "LVIII" else "Fail")
print(1994, "Pass" if array_map_int_to_rom(1994) == "MCMXCIV" else "Fail")
