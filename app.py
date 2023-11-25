from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/movie', methods= ["GET","POST"])
def getMovie():
    

    url = "https://moviesdatabase.p.rapidapi.com/titles/random"
    querystring = {"list":"most_pop_series"}
    headers = {
    'X-RapidAPI-Key':request.form.get("apiKey"),
	#"X-RapidAPI-Key": "74fe65ea69msh177d32e0dc593efp129997jsn2355f7fbcdce",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}
    print(headers)
    response=requests.get(url,headers=headers,params=querystring)
    data = response.json()
    movies=data.get('results', [])
    print(movies)
    
    
    return render_template('index.html', movies=movies)
    #return f"data : {data}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)