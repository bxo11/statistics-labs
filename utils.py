def calculate_avg(sequence):
    suma = 0
    for x in sequence:
        suma += x
    return suma / len(sequence)


def calculate_variance(sequence):
    average = calculate_avg(sequence)
    suma_kwadratow_odchylen = 0
    for element in sequence:
        suma_kwadratow_odchylen += (element - average) ** 2
    return suma_kwadratow_odchylen / len(sequence)

def calculate_sum(sequence):
    result = 0
    for a in sequence:
        result+=a
    return result