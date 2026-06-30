from repository.location_repository import LocationRepository


class RoadRepository:

    def get_graph(self):

        locations = LocationRepository().get_all_locations()
        connections = {

            "Home": [

                "Mall",

                "School",

                "Airport",

                "City Park"

            ],

            "Mall": [

                "Home",

                "Office",

                "Hospital",

                "Railway Station",

                "City Park"

            ],

            "School": [

                "Home",

                "Hospital",

                "City Park"

            ],

            "Hospital": [

                "School",

                "Mall",

                "Office",

                "Tech Park"

            ],

            "Office": [

                "Mall",

                "Hospital",

                "Tech Park"

            ],

            "Airport": [

                "Home",

                "Beach",

                "Railway Station"

            ],

            "Railway Station": [

                "Mall",

                "Airport",

                "Beach"

            ],

            "Beach": [

                "Airport",

                "Railway Station",

                "City Park"

            ],

            "Tech Park": [

                "Office",

                "Hospital"

            ],

            "City Park": [

                "Home",

                "Mall",

                "School",

                "Beach"

            ]

        }

        graph = {}

        for start, neighbors in connections.items():
            graph[start] = {}

            for end in neighbors:
                graph[start][end] = self.calculate_distance(
                    locations[start],
                    locations[end]
                )

        return graph

    def calculate_distance(self, start, end):

        latitude_difference = start[0] - end[0]
        longitude_difference = start[1] - end[1]
        distance = (
            (latitude_difference ** 2) +
            (longitude_difference ** 2)
        ) ** 0.5

        return round(max(distance * 55, 1), 2)
