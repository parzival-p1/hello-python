
###*** ***  L  A  M  B  D  A  S *** ***###

"""_definicion_
lambdas: funciones anonimas void que puedo 
almacenar en una variable
"""

#^ *** definiendo lambdas *** ^#
sum_two_vals = lambda fst_value, snd_value: fst_value + snd_value
print(sum_two_vals(2, 4))   # 6

mult_values = lambda fst_value, snd_value: fst_value * snd_value - 3
print(mult_values(2, 4))    # 5

#^ *** lambdas dentro de una func() *** ^#
def sum_three_vals(value):
    return lambda fst_value, snd_value: fst_value + snd_value + value

print(sum_three_vals(5)(2, 4))  # 11
