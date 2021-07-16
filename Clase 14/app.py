from flask import Flask, json, request
from pymongo import MongoClient
from urllib.parse import urlencode
import settings
from os import environ


USER = environ["DB_USER"]
PASS = environ["DB_PASS"]
HOST = environ["DB_HOST"]
BASE = environ["DB_NAME"]
PORT = environ["PORT"]
FLASK_ENV = environ["FLASK_ENV"]

app = Flask(__name__)

###### MongoDB ######
params = {
    "retryWrites" : "true",
    "w" : "majority",
    "ssl" : "true",
    "ssl_cert_reqs" : "CERT_NONE"
}
client = MongoClient("mongodb+srv://" + USER + ":" + PASS + "@" + HOST + "/" + BASE + "?" + urlencode(params) )      
db = client
#####################

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

@app.route("/users/<path>")
def searchUsers(path):
    
    '''
    if path == "people":
        return "ACA VA UN JSON DE PERSONAS"
    elif path == "company":
        return "ACA VA UN JSON DE EMPRESAS"
    else:
        return "UPPS... NO PUEDO BUSCAR LO QUE ESTAS PIDIENDO :("
    '''
    
    if path not in ["people", "company", "all"]:
        return "UPPS... NO PUEDO BUSCAR LO QUE ESTAS PIDIENDO :("
    
    data = db["PDD-MJ-N-287"]
    test = data["twitter"]
    
    if path == "all":
        users = test.find({}).limit(10)
    else:
        users = test.find({ "type" : path }).limit(10)
    
    result = []

    for user in users:
        item = {
            'usuario' : user['name']
        }
        result.append(item)

    return app.response_class(response = json.dumps(result), status = 200, mimetype = "application/json" )

@app.route("/test")
def test():
    data = db["PDD-MJ-N-287"]
    test = data["twitter"]
    
    
    users = test.find()
    
    for user in users:
        print(user)
    
    return "Mira la consola..."
    
@app.route("/tweets/<user>/<limit>")
def filterUsers(user, limit):
    data = db["PDD-MJ-N-287"]
    twitter = data["twitter"]
    
    if limit != None and limit.isnumeric():
        limit = int(limit)
    else:
        response = {
            "ok" : False,
            "msg" : "ERROR: No puede realizarse la busqueda :("
        }
        return app.response_class(response = json.dumps(response), status = 404, mimetype = "application/json")
        
    tweets = twitter.find({ "in_reply_to_screen_name" : user }).limit(limit)

    response = []
    
    for tweet in tweets:
        item = {
            "id" : tweet['id_str'],
            "user" : tweet['in_reply_to_screen_name'],
            "tweet" : tweet['full_text']
        }
        response.append(item)

    return app.response_class(response = json.dumps(response), status = 200, mimetype = "application/json")

@app.route("/tweets", methods = ["POST"])
def postearTweets():

    data = db["PDD-MJ-N-287"]
    twitter = data["twitter"]
    
    el_tweet = {
        "id_str" : request.form["id"],
        "in_reply_to_screen_name" : request.form["user"],
        "full_text" : request.form["tweet"]
    }
    
    result = twitter.insert_one( el_tweet )

    '''   
    if result.acknowledged == True:
        
        response = {
            "ok" : True,
            "msg" : "Tweet guardado correctamente :D"
        }
    
    else:

        response = {
            "ok" : False,
            "msg" : "Error al guardar el Tweet :C"
        }
    '''
    
    # variable = valor_verdaro CONDICION valor_falso
    
    response = { "ok" : True, "msg" : "Tweet guardado correctamente :D" } if result.acknowledged == True else { "ok" : False, "msg" : "Error al guardar el Tweet :C" }
    
    # response = result.acknowledged == true ? { ok : true } : { ok : false }
    
    return app.response_class(response = json.dumps(response), status = 200, mimetype = "application/json")





if __name__ == "__main__":
    if FLASK_ENV == "development":
        app.run( port = PORT, host = '0.0.0.0' )
    else:
        app.run( port = PORT )