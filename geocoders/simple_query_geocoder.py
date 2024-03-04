from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        aid = area_id
        response = API.get_area(area_id).name
        while API.get_area(area_id).parent_id:
            area_id = API.get_area(area_id).parent_id
            response = API.get_area(area_id).name + ', ' + response
        response = str(aid) + ',"' + response + '"'
        return response
