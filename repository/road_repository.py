class RoadRepository:

    def get_graph(self):

        return {

            "Home": {

                "Mall": 2,

                "School": 5,

                "Airport": 3,

                "City Park": 4

            },

            "Mall": {

                "Home": 2,

                "Office": 4,

                "Hospital": 3,

                "Railway Station": 2,

                "City Park": 3

            },

            "School": {

                "Home": 5,

                "Hospital": 2,

                "City Park": 2

            },

            "Hospital": {

                "School": 2,

                "Mall": 3,

                "Office": 2,

                "Tech Park": 3

            },

            "Office": {

                "Mall": 4,

                "Hospital": 2,

                "Tech Park": 2

            },

            "Airport": {

                "Home": 3,

                "Beach": 4,

                "Railway Station": 5

            },

            "Railway Station": {

                "Mall": 2,

                "Airport": 5,

                "Beach": 2

            },

            "Beach": {

                "Airport": 4,

                "Railway Station": 2,

                "City Park": 5

            },

            "Tech Park": {

                "Office": 2,

                "Hospital": 3

            },

            "City Park": {

                "Home": 4,

                "Mall": 3,

                "School": 2,

                "Beach": 5

            }

        }
