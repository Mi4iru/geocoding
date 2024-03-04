from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.decoder = {}

        def dfs(start: TreeNode, visited=None):
            if visited is None:
                visited = set()
            visited.add(start.id)
            self.decoder[start.id] += [start.name]
            for next in start.areas:
                if next.id not in visited:
                    self.decoder[next.id] = self.decoder[start.id].copy()
                    dfs(next, visited)
        for i in self.__data:
            self.decoder[i.id] = []
            dfs(i)

    def _apply_geocoding(self, area_id: str) -> str:
        return str(area_id) + ',"' + ', '.join(self.decoder[str(area_id)]) + '"'
