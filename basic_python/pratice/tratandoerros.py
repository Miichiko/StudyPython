try:
    # resultado = 10 / 0
    # import ios
    # print(variavel)
    int('adg')

# aki consigo ver os tipos de erros e processar cada um deles.


# aki esto tratando de cada error.
except ZeroDivisionError:
    print('error: divisão por 0 não permitida.')
except ModuleNotFoundError:
    print('nenhum módulo encontrado.')
except NameError:
    print('Variável não definida.')
except ValueError:
    print('Valor inapropriado.')
except Exception as error:
    print('Deu um erro')
    print('MSG:', error)
    print("nome:", error.__class__.__name__)
