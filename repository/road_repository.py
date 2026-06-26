class RoadRepository:

    def get_graph(self):

        return {

            "Home": {

                "Mall": 2,

                "School": 5

            },

            "Mall": {

                "Home": 2,

                "Office": 4,

                "Hospital": 3

            },

            "School": {

                "Home": 5,

                "Hospital": 2

            },

            "Hospital": {

                "School": 2,

                "Mall": 3,

                "Office": 2

            },

            "Office": {

                "Mall": 4,

                "Hospital": 2

            }

        }