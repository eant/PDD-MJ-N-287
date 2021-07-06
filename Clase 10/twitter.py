import tweepy
from pprint import pprint

claves = open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves_twitter.txt')
keys = [clave.strip('\n') for clave in claves]

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#%%
#Mi perfil
usuario = api.me()
pprint(usuario._json)
#%%
#Otro usuario
otro_usuario = api.get_user('DrBrianMay')
pprint(otro_usuario._json)
#%%
#Seguidores (te devuelve 20 porque es el resultado paginado)
seguidores = api.followers(screen_name = 'DrBrianMay')
for seguidor in seguidores:
   print(seguidor._json['screen_name'])
#%%
#Si quiero más de 20 resultados, por ejemplo a quién sigue alguien
for amigo in tweepy.Cursor(api.friends, screen_name = 'DrBrianMay').items(80):
   nombre = amigo._json['screen_name']
   print(nombre)
#%%
#Los twits que posteó un usuario
contador = 1
for tweet in tweepy.Cursor(api.user_timeline, screen_name = 'alferdez', tweet_mode = 'extended').items(10):
   try:
      print(contador, "Este es un retweet:")
      pprint(tweet._json['retweeted_status']['full_text'])
   except:
      print(contador)
      pprint(tweet._json['user']['created_at'])
   contador += 1
#%%
for tweet in tweepy.Cursor(api.search, q = 'music', tweet_mode = 'extended').items(10):
   print(tweet._json['full_text'])



