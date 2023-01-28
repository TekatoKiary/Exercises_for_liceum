import sys
from io import BytesIO
import requests
from PIL import Image
import scale_map


def get_response(geocoder_server, geocoder_params):
    _response = requests.get(geocoder_server, params=geocoder_params)
    if not _response:
        print("Ошибка выполнения запроса")
        print("Http статус:", _response.status_code, "(", _response.reason, ")")
        sys.exit()
    _json_response = _response.json()
    return _json_response


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

json_response = get_response(geocoder_api_server, geocoder_params)

toponym_object = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
map_params = scale_map.scale_map(toponym_object)

geocoder_api_server = "https://search-maps.yandex.ru/v1/"

geocoder_params = {
    "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
    "text": "аптека",
    "type": "biz",
    "lang": "ru_RU",
    'll': map_params["ll"]
}
json_response_pharmacy = get_response(geocoder_api_server, geocoder_params)

map_params['pt'] = [f"{map_params['ll']},pmrdm99"]
map_params.pop('ll')
map_params.pop('spn')
for i in range(10):
    coord = json_response_pharmacy["features"][i]['geometry']["coordinates"]
    hours = json_response_pharmacy["features"][i]["properties"]["CompanyMetaData"]["Hours"]['Availabilities'][0]
    color = 'gr'
    if hours.get("TwentyFourHours"):  # Именно круглосуточные, то есть работа в 24 часа в сутки
        color = 'gn'
    elif len(hours.keys()):
        color = 'bl'
    map_params['pt'] += [f'{",".join(map(str, coord))},pm{color}m{1 + i}']

map_params['pt'] = '~'.join(map_params['pt'])

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
