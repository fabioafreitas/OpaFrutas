from geopy.geocoders import Nominatim
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS


geolocator = Nominatim(user_agent="teste")
google_api_key = "[KEY API GOOGLE MAPS]"

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=['POST'])
def teste():
    httpBody = request.get_json()
    address1 = httpBody['address1']
    address2 = httpBody['address2']

    coord1 = [] # latitude, longitude
    coord2 = [] # latitude, longitude

    location = geolocator.geocode(address1)
    # print("\nEndereço 1:")
    # print(location.address)
    coord1.append(location.latitude)
    coord1.append(location.longitude)

    location = geolocator.geocode(address2)
    # print("\nEndereço 2:")
    # print(location.address)
    coord2.append(location.latitude)
    coord2.append(location.longitude)

    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+str(coord1[0])+","+str(coord1[1])+"&destinations="+str(coord2[0])+"%2C"+str(coord2[1])+"&key="+google_api_key)
    dados = response.json()
    distancia = dados['rows'][0]['elements'][0]['distance']
    tempo = dados['rows'][0]['elements'][0]['duration']
    # print("\n")
    # print(distancia)
    # print(tempo)
    print('{},{}'.format(address1, address2))
    return jsonify({'distancia':distancia, 'tempo':tempo})

if __name__ == '__main__':
    app.run()
