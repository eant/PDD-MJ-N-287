from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return '<h1>Hola mundo</h1>'

@app.route("/users")
def twitterUsers():
    users = [
        { 'name' : 'smessina_' },
        { 'name' : 'eantech' },
        { 'name' : 'TinchoLutter' },
        { 'name' : 'bitcoinArg' }
    ]
    response = app.response_class(response = json.dumps(users), status = 200, mimetype = "application/json"  )
    
    return response

app.run( port = 3030, host = '0.0.0.0' )