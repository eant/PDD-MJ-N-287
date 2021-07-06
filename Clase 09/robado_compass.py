from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={
    'dni': {
        '$gt': 30000000
    }
}
sort=list({
    'nombre': 1
}.items())

result = client['universidad']['alumnos'].find(
  filter=filter,
  sort=sort
)

for resultado in result:
   print(resultado)
