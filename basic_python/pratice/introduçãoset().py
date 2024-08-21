#  Métodos utéis em set().

#  Aqui tenho meu set() vázio.
s1 = set()

#  add
s1.add("Michiko")

#  update
# s1.update('Olá mundo')  "O,l,á, ,m,u,n,d,o"
s1.update(("Olá, mundo", 1, 2, 3, 4))

#  discard
s1.discard(4)

#  clear para limpar tudo
s1.clear()

# set() está novamente vázio.
print(s1)


# Operadores utéis:
# union | union - une as duas
# intersection & - itens presentes em ambas as duas
# difference - - itens presentes apenas no set da esquerda
# symmetrical difference ^ - itens que não estão presentes em ambas
