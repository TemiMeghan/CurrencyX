# imports modules
from flask import Flask, render_template
from currency import get_nation
import requests

app = Flask('app')


@app.route('/')
def index():
  data = get_nation()  # assigns function to data
  for nation in data:  # loops data
    nation_url = f"https://restcountries.com/v3.1/name/{nation['country']}"# nation url
    response = requests.get(nation_url) #gets data
    nation_info = response.json()[0]
    nation['population'] = nation_info['population']
  
  return render_template("/index.html", data=data)




app.run(host='0.0.0.0', port=8080)


