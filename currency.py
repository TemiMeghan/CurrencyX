# imports modules
import requests
import nasdaqdatalink

nasdaqdatalink.ApiConfig.api_key = 'bmNyFL8dH_srfWkPmnc6'# nasdaq key

nations = ['HRV','ARE','CHE'] # selected nations

def get_nation():    
    nation_list = [] # empty list
    for nation_code in nations: # loops nations
        if nation_code == 'HRV':# checks for equality
            nation_name = 'Croatia' 
        elif nation_code == 'ARE':# checks for equality
            nation_name = 'UAE'
        elif nation_code == 'CHE':# checks for equality
            nation_name = 'Switzerland'
        else:
            nation_name = None# checks for equality
          
        if nation_name:
            data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{nation_code}', start_date='2021-01-31', end_date='2021-01-31') # assigns nasdaq api to data

            nation_demo = requests.get(f"https://restcountries.com/v3.1/name/{nation_name}")# gets data
            nation_info = nation_demo.json()[0]
            flag = nation_info.get("flags")
            svg = flag['svg']

            nation = {  
                "country": nation_name,
                "local_price": data.iloc[0, 0],# selects index0
                "dollar_ex": data.iloc[0, 1],# selects index1
                "dollar_price": data.iloc[0, 2],# selects index2
                "dollar_ppp": data.iloc[0, 3],# selects index3
                "dollar_valuation": data.iloc[0, 4],# selects index4
                "dollar_adj_valuation": data.iloc[0, 5],# selects index5
                "flag": svg,
                "geolocation": nation_info.get("region"),#gets region
                "population": nation_info.get("population"),#gets population
            }

            nation_list.append(nation)# appends data to nation_list

    return nation_list# returns nation_list
