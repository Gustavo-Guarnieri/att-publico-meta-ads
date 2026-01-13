import requests
import json
from dotenv import load_dotenv
import os

#Carrega dados do .env
load_dotenv()

def request_mixpanel():
    #Declara variáveis que serão usadas no loop de paginação
    all_results_list = []
    page = 0
    session_id = None
    total = None

    #Dados para requisição
    url = f"https://mixpanel.com/api/query/engage?project_id={os.getenv('PROJECT_ID')}"
    payload = {
    "output_properties": ["Name", "Phone", "Email","$country_code","$region","$city", "Pais"],
    "filter_by_cohort": {"id": 5945342}, #Cohort company: [RMKT] Ativos desengajados total (pag e iniciante)
    "data_group_id": '8453995111420155989'
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "authorization": os.getenv('BASIC_TOKEN')
    }

    #Inicio da requisição com loop de paginação
    while True:
        params = {
            "page": page
        }

        if session_id:
            params["session_id"] = session_id

        response = requests.post(url, data=json.dumps(payload), headers=headers, params=params)
        data = response.json()

        # guarda o session_id e outros dados retornado na primeira chamada
        session_id = data["session_id"]
        results = data["results"]
        if total is None:
            total = data["total"]

        all_results_list.extend(results)

        # CONDIÇÃO DE PARADA
        if total is not None and len(all_results_list) >= total:
            break

        page += 1

    print('Dados mixpanel pegos')
    return all_results_list, total


