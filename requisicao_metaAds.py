import requests
from dotenv import load_dotenv
import os
import datetime as d

def session_id():
    data = d.datetime.now()
    session_id = d.date.strftime(data,"%d%m%Y%H%M")
    return session_id

def requisicao_metaAds(dados_usuarios,total_lista, id_sessao):
    url = f'https://graph.facebook.com/v24.0/{os.getenv('AUDIENCE_ID')}/usersreplace'
    params = {'access_token':os.getenv('ACCESS_TOKEN')}
    payload = {
        "session": {
        "session_id":id_sessao, 
        "batch_seq":1,
        "last_batch_flag":True, 
        "estimated_num_total":total_lista 
        },
        "payload": {
        "schema": ["FN","EMAIL","PHONE","COUNTRY"],
        "data": dados_usuarios
        },
    }
    headers = {"Content-Type": "application/json"}


    response = requests.post(
        url,
        params=params,
        json=payload,
        headers=headers
    )

    print(response.status_code)
    print(response.json())

#{'error': {'message': '(#100) Data is missing or does not match schema', 
# 'type': 'OAuthException', 'code': 100, 'fbtrace_id': 'AkVBHUBSX9W0B9k3P_8WIgT'}}