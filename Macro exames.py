import time
import pyautogui as py
import pyperclip as clip
import collections
from lista import lista_valores

lista = lista_valores()

val = 0

while val < 8068:
    for valor in lista:
        time.sleep(1)
        py.moveTo(434, 50)
        py.click(button='left')
        py.click(button='left')
        time.sleep(2)
        # time.sleep(3)
        # py.keyDown('ctrl')
        # py.press('a')
        # py.keyUp('ctrl')
        py.typewrite(valor)
        py.press('enter')
        #filtrar
        # py.moveTo(1241, 303)
        # py.click(button='left')
        time.sleep(2)

    # #selecionar editar
    #     py.moveTo(1301, 460)
    #     py.click(button='left')
    #     time.sleep(2)
        #selecionar opcoes de agenda
        py.moveTo(124, 315)
        py.click(button='left')
        time.sleep(1)
        #selciononar exibição de agenda
        py.moveTo(284, 377)
        py.click(button='left')
        time.sleep(1)
        #selecionar salvar
        py.moveTo(1280, 192)
        py.click(button='left')
        time.sleep(1)
        # #voltar browser
        # py.moveTo(18, 52)
        # py.click(button='left')
        #rolar pra baixo e salvar
        # py.scroll(-5000)
        # py.moveTo(1277, 662)
        # py.click(button='left')
        # time.sleep(1)
        #salvar
        # py.moveTo(1277, 665)
        # py.click(button='left')
    val += 1

print("fim")
