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


def get_coord_of_pharmacy(pos):
    geocoder_api_server = "https://search-maps.yandex.ru/v1/"

    geocoder_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "text": "аптека",
        "type": "biz",
        "lang": "ru_RU",
        'll': pos
    }

    json_response = get_response(geocoder_api_server, geocoder_params)

    snippet['Название аптеки:'] = json_response["features"][0]["properties"]["CompanyMetaData"]["name"]
    snippet['Адрес аптеки:'] = json_response["features"][0]["properties"]["CompanyMetaData"]["address"]
    snippet['Часы работы:'] = json_response["features"][0]["properties"]["CompanyMetaData"]["Hours"]["text"]

    toponym_coord = json_response["features"][0]['geometry']["coordinates"]
    return toponym_coord


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12

toponym_to_find = " ".join(sys.argv[1:])

snippet = dict()

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

json_response = get_response(geocoder_api_server, geocoder_params)

toponym_object = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
map_params = scale_map.scale_map(toponym_object)

coord_pharmacy = get_coord_of_pharmacy(map_params["ll"])

snippet['Расстояние между точками:'] = ((float(map_params["ll"][0]) - coord_pharmacy[0]) ** 2 +
                                        (float(map_params["ll"][1]) - coord_pharmacy[1]) ** 2) ** 0.5

map_params['pt'] = f'{map_params["ll"]},pmrdm99~{",".join(map(str, coord_pharmacy))},pmgnm1'
map_params.pop('ll')
map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

for key, value in snippet.items():  # Не совсем понял на какой экран надо вывести
    print(key, value)
Image.open(BytesIO(response.content)).show()
