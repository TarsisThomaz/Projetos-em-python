from datetime import datetime

ano_nasc = int(input('ano nasceu?'))
mes_nasc = int(input('mes nasceu?'))
dia_nasc = int(input('dia nasceu'))

data nasc = datetime(ano_nasc, mes_nasc, dia_nasc)
data_atual = datetime.now()

diff = data_atual - data_nasc

dias = diff.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

print(f'Você tem{anos}, anos')