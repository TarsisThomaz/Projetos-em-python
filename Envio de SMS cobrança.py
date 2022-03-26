import json
import requests

def vigencia_boleto(sql_nome, sql_numero, sql_id, sql_boleto):
    url = "URL TELEFONIA"    payload = json.dumps({
        "expiraLista": 240,
        "cancelarPendentes": False,
        "contatos": [
            {
            "contato": sql_numero,
            "cliente": sql_nome,
            "idExterno": sql_id,
            "notificacao": "Olá"+" "+sql_nome+ ", aqui é a *!\nTudo bem? Não identificamos o pagamento de sua mensalidade, isso pode te impossibilitar de utilizar seus benefícios. Estamos preocupados com sua saúde e à disposição para te ajudar.\n\nEnviamos também o link do boleto para pagamento!\n"+""+sql_boleto+"\n\n\nÉ importante para você manter os seus acompanhamentos médicos?"
           }
        ]
        })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'AUTORIZAÇÃO AQUI'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if connection.is_connected():
    txt = open('query.sql')
    cursor.execute(txt.read())
    records = cursor.fetchall()
    cont = 0
    for i in records:
        sql_id, sql_plano, sql_status, sql_vencimento, sql_valor_mensal, sql_nome, sql_numero, sql_tipo_pagamento, sql_boleto, sql_codigo_barras, sql_dia_pagamento, sql_qtd_faturas_pagar, sql_dias_atraso, sql_mes_cobranca, dia_cobranca = i
        if (sql_tipo_pagamento == 'TICKET' or sql_tipo_pagamento == 'TICKETS'):
            # vai cobrar no dia seguinte do vencimento da fatura do titular
            if (dia_cobranca == 5 and sql_qtd_faturas_pagar == 1 and sql_dias_atraso >= 2):
                for sql_numero_formatado in sql_numero:
                    sql_numero_formatado = str(0) + sql_numero
                    v_sql_numero_formatado = remover_caracteres(sql_numero_formatado, "-()")
                cont = cont + 1
                pp.pprint(sql_id)
                pp.pprint(sql_plano)
                pp.pprint(sql_status)
                pp.pprint(sql_vencimento)
                pp.pprint(sql_valor_mensal)
                pp.pprint(sql_qtd_faturas_pagar)
                pp.pprint(sql_dias_atraso)
                pp.pprint(sql_tipo_pagamento)
                pp.pprint(sql_codigo_barras)
                pp.pprint(sql_boleto)
                pp.pprint(sql_dia_pagamento)
                pp.pprint(sql_mes_cobranca)
                pp.pprint(sql_nome)
                pp.pprint(v_sql_numero_formatado)
                pp.pprint(30 * '-=')
                vigencia_boleto(sql_nome,v_sql_numero_formatado,sql_id,sql_boleto)