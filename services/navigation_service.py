import heapq

class NavigationService:

    def find_shortest_path(self, graph, start, destination):

        distances = {node: float("inf") for node in graph}
        distances[start] = 0

        previous = {node: None for node in graph}

        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_node = heapq.heappop(priority_queue)

            for neighbor, weight in graph[current_node].items():

                distance = current_distance + weight

                if distance < distances[neighbor]:

                    distances[neighbor] = distance

                    previous[neighbor] = current_node

                    heapq.heappush(
                        priority_queue,
                        (distance, neighbor)
                    )

        path = []

        current = destination

        while current is not None:

            path.append(current)

            current = previous[current]

        path.reverse()

        return distances[destination], path