import pyautogui as py
import time
import pyperclip as clip
import schedule as sch
from datetime import datetime
from datetime import date
from datetime import timedelta

#Lembrete - Mudar filiais ao enviar cada relatório

py.PAUSE = 1

def procedimentos():
    
    time.sleep(3)
    #Copiar email gerado
    py.moveTo(35,350)
    py.click(button='left')
    time.sleep(1)
    py.hotkey('Ctrl','t')
    py.hotkey('Ctrl','c')
    
    #Abrir novo email
    py.moveTo(203,744)
    py.click(button='left')
    py.write("Outlook")
    time.sleep(1)
    py.press('Enter')
    
    time.sleep(1)
    py.moveTo(35,89)
    py.click(button='left')

    #Colar conteúdo no novo email
    py.moveTo(26,354)
    py.click(button='left')
    py.hotkey('Ctrl','v')
    
    #Colocar os endereços de email
    emails = ""
    clip.copy(emails)
    
    py.moveTo(254,210)
    py.click(button='left')
    py.hotkey('Ctrl','v')
    
    #Colocar o título do email
    py.moveTo(1266,305)
    py.click(button='left')
    
    filial = ['Todas as Filiais','Nova Iguaçu','Miguel Couto', 'Nilópolis']
    
    #hoje = datetime.today().strftime('%d/%m/%Y')
    ontem = date.today() - timedelta(days=1)
    str_ontem = ontem.strftime('%d/%m/%Y')
    assunto = 'Controle de Procedimentos - ' + filial[3] + ' - ' + str_ontem
    clip.copy(assunto)
    py.hotkey('Ctrl','v')
    
    
    #Muda a assinatura
    # time.sleep(3)
    # py.moveTo(785,136)
    # py.click(button='left')

    # time.sleep(3)
    # py.moveTo(814,202)
    # py.click(button='left')

    #Clica em enviar e fecha o Outlook
    time.sleep(3)
    py.moveTo(58,237)
    py.click(button='left')

    #time.sleep(10)
    #py.moveTo(1342,13)
    #py.click(button='left')
    
    print("Terminou")
    
procedimentos()
