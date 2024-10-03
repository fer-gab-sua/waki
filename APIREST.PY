import http.client
import json

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "7e8d395c32f0b3a14d452f48e293b275"
    }

conn.request("GET", "/fixtures/rounds?season=2022&league=61", headers=headers)

res = conn.getresponse()
data = res.read()


# Convierte los datos a formato JSON
json_data = json.loads(data)

# Imprime los datos en formato JSON
print(json.dumps(json_data, indent=4))  # Usa indent=4 para una mejor legibilidad