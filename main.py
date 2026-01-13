from requisicao_mixpanel import request_mixpanel
import json
from normalizacao_dados import normaliza_dados
from requisicao_metaAds import requisicao_metaAds, session_id

#Faz requisição para o Mixpanel
dados_mix, total_usuarios = request_mixpanel()


#Salva em um arquivo uma lista com todos usuários COLETADOS do cohort
with open('LOG_dados_mixpanel.json','w',encoding='utf-8') as f:
    json.dump(dados_mix, f, ensure_ascii=False, indent=4)

#Normaliza e criptografa dados
dados_normalizados = normaliza_dados(dados_mix)

#Salva em um arquivo uma lista com todos usuários NORMALIZADOS
with open('LOG_dados_normalizados.txt','w',encoding='utf-8') as f:
        for item in dados_normalizados:
            f.write(f"{str(item)}\n")    
        
#Cria ID da sessão com base no dia e horário
id_sessao = session_id()

#Faz envio dados para Meta Ads
requisicao_metaAds(dados_normalizados,total_usuarios,id_sessao)