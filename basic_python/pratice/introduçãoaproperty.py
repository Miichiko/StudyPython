#  property é um método, mas se comporta como um atributo.
#  property funciona como um getter ele captura a info, mas sem quebra o códico


# neste caso estou privando o códico com o _cor
class Caneta:
    def __init__(self, cor):
        # self.cor_tinta = cor
        # _ ou __  eu estou dizendo que não deve ser usado fora da classe
        self._cor = cor

    # aki obtem uma cor
    @property
    def cor(self):
        return self._cor

    # aki está configurando uma nova cor
    @cor.setter
    def cor(self, valor):
        # aki posso restringir algumas ações
        # if valor == 'Rosa':
        #     raise ValueError('Não aceito essa cor')
        self._cor = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
# caneta._cor    _ ou __  eu estou dizendo que não deve ser usado fora da classe
