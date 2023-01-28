def scale_map(toponym_object):
    # Координаты центра топонима:
    toponym_coodrinates = toponym_object["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    lower_corner = toponym_object['boundedBy']['Envelope']['lowerCorner'].split()
    upper_corner = toponym_object['boundedBy']['Envelope']['upperCorner'].split()

    delta_x = abs(float(upper_corner[0]) - float(lower_corner[0]))
    delta_y = abs(float(upper_corner[1]) - float(lower_corner[1]))

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": f'{delta_x},{delta_y}',
        "l": "map"
    }
    return map_params