from requisicao_mixpanel import request_mixpanel
import json
from normalizacao_dados import normaliza_dados
from requisicao_metaAds import requisicao_metaAds, session_id

def executaPipeline():
    #Faz requisição para o Mixpanel
    dados_mix, total_usuarios = request_mixpanel()

    #Normaliza e criptografa dados
    dados_normalizados = normaliza_dados(dados_mix)  
            
    #Cria ID da sessão com base no dia e horário
    id_sessao = session_id()

    #Faz envio dados para Meta Ads
    resultado_meta = requisicao_metaAds(dados_normalizados,total_usuarios,id_sessao)

    return {
        "total_mixpanel": total_usuarios,
        "total_normalizados": len(dados_normalizados),
        "meta_result": resultado_meta
    }