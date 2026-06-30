class MapService:

    def build_city_map(self, locations, graph):

        positions = self.build_positions(locations)

        return {
            "locations": self.build_location_points(locations.keys(), positions),
            "roads": self.build_road_lines(graph, positions)
        }

    def build_route_map(self, locations, path):

        route_locations = {
            location: locations[location]
            for location in path
        }
        positions = self.build_positions(route_locations)

        return {
            "locations": self.build_location_points(path, positions),
            "roads": self.build_path_lines(path, positions),
            "points": [
                {
                    "name": location,
                    "x": positions[location]["x"],
                    "y": positions[location]["y"]
                }
                for location in path
            ]
        }

    def build_positions(self, locations):

        latitudes = [location[0] for location in locations.values()]
        longitudes = [location[1] for location in locations.values()]
        min_latitude = min(latitudes)
        max_latitude = max(latitudes)
        min_longitude = min(longitudes)
        max_longitude = max(longitudes)

        latitude_range = max(max_latitude - min_latitude, 0.01)
        longitude_range = max(max_longitude - min_longitude, 0.01)

        positions = {}

        for name, coordinates in locations.items():
            latitude, longitude = coordinates
            x = 8 + ((longitude - min_longitude) / longitude_range) * 84
            y = 92 - ((latitude - min_latitude) / latitude_range) * 84
            positions[name] = {
                "x": round(x, 2),
                "y": round(y, 2)
            }

        return positions

    def build_location_points(self, location_names, positions):

        return [
            {
                "name": name,
                "x": positions[name]["x"],
                "y": positions[name]["y"]
            }
            for name in location_names
        ]

    def build_road_lines(self, graph, positions):

        roads = []
        seen_roads = set()

        for start, neighbors in graph.items():
            for end in neighbors:
                road_key = tuple(sorted([start, end]))

                if road_key in seen_roads:
                    continue

                seen_roads.add(road_key)
                roads.append(self.build_line(start, end, positions))

        return roads

    def build_path_lines(self, path, positions):

        roads = []

        for index in range(len(path) - 1):
            roads.append(
                self.build_line(
                    path[index],
                    path[index + 1],
                    positions,
                    is_active=True
                )
            )

        return roads

    def build_line(self, start, end, positions, is_active=False):

        start_position = positions[start]
        end_position = positions[end]

        return {
            "start": start,
            "end": end,
            "x1": start_position["x"],
            "y1": start_position["y"],
            "x2": end_position["x"],
            "y2": end_position["y"],
            "is_active": is_active
        }
