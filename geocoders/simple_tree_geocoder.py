from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        def dfs(start, visited=None):
            if visited is None:
                visited = set()
            visited.add(start.id)
            if int(start.id) == int(area_id):
                return start.name
            else:
                for next in start.areas:
                    if next.id not in visited:
                        s = dfs(next, visited)
                        if s:
                            return start.name + ', ' + s

        for i in self.__data:
            s = dfs(i)
            if s:
                return str(area_id) + '"' + s + '"'


