from flask import Flask

app = Flask(__name__)

#Rotas endpoints
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/mas')
def hello_mas():
    return 'Hello Mas'

if __name__ == "__main__":
    app.run(debug=True)