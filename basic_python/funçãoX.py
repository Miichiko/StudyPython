def multiplicação(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado


def checando_par_impar(*args):
    resultado = multiplicação(*args)
    if resultado % 2 == 0:
        return (f"seu resultado {resultado} é par.")
    else:
        return (f"seu resultado {resultado} é impar.")


print(checando_par_impar(7, 1))
