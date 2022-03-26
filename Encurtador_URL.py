from too_short_url import too_st
from lista_nomes import lista_links

lista = lista_links()

val = 0
while val < 483:
    for valor in lista:
        print(too_st(valor))
        val += 1


