def multiplicação(*args):
    resultado = 1
    for arg in args:
        resultado = resultado * arg
    return resultado


def checando_par_impar(*args):
    resultado = multiplicação(*args)
    print(f'seu resultado é {resultado}')
    if resultado % 2 == 0:
        return (f"seu resultado {resultado} é par.")
    else:
        return (f"seu resultado {resultado} é impar.")


print(checando_par_impar(2, 2, 2))
