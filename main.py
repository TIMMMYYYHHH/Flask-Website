from flask import Flask, render_template
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
fox = response.json()

# print(fox)


app = Flask(__name__)



@app.route('/')
def index():
    
    

    return render_template('index.html')

@app.route('/about/<name>')
def about(name):
    print(name)
    return render_template('about.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

