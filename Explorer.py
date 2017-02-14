class Journey:
    """
    This class manages journey over very difficult terrains.
    """

    def __init__(self, path):
        """
        Initiate table with difficult terrains.
        :param path: Path to the file with difficult terrains
        """
        self.tables = []
        self.graphs = None
        self.shortest_paths = None
        with open(path, "r") as file:
            lines = file.readlines()

        line_number = 0

        while line_number < len(lines):
            temp_table = []
            matrix_size = int(lines[line_number].strip())
            line_number += 1
            for index in range(line_number, line_number + matrix_size):
                row = lines[index].strip().split(',')
                int_row = map(int, row)
                temp_table.append(list(int_row))
            self.tables.append(temp_table)
            line_number += matrix_size

    def give_shortest_paths(self):
        """
        This  function load graphs symbolizing terrains into graph table,
        count shortest path through terrain and print it.
        """
        self.load_graphs()
        self.count_shortest_path()
        print(self, end="")

    def load_graphs(self):
        """
        Create table with graphs which can count shortest path in terrain.
        """
        self.graphs = [Graph(table) for table in self.tables]

    def count_shortest_path(self):
        """
        Count shortest path for each terrain.
        """
        self.shortest_paths = [graph.count_djikstra() for graph in self.graphs]

    def __str__(self):
        to_print = ""
        for cost in self.shortest_paths:
            to_print += str(cost) + "\n"
        return to_print


class Graph:
    def __init__(self, table):
        self.nodes = set(range(0, pow(len(table), 2) + 1))
        self.edges = None
        self.generate_edges(len(table))
        self.distance = [elem for row in table for elem in row]
        self.distance.insert(0, 0)

    def generate_edges(self, table_x_size):
        """
        Generate paths between nodes in self.edges . You can move only move to the right and down.
        :param table_x_size: Size of x or y wall in terrain array.
        """
        x_size = table_x_size
        self.edges = dict((node, []) for node in self.nodes)

        if x_size:
            self.edges[0].append(1)

        for from_node in range(1, len(self.nodes)):
            if from_node % x_size:  # There is area on the right side of from_node element
                self.edges[from_node].append(from_node + 1)

            if from_node / x_size <= x_size - 1:  # There is area below from_node element
                self.edges[from_node].append(from_node + x_size)

    def count_djikstra(self):
        """
        Count cost  between start point(with cost 0) and rest of the fields.
        Algorithm which was used: http://eduinf.waw.pl/inf/alg/001_search/0138.php
        :return: Table with travel cost to every area in terrain.
        """

        q = self.nodes.copy()
        s = set()
        cost = [float("inf") for i in range(0, len(self.nodes))]
        cost[0] = 0
        predecessor = dict((node, None) for node in self.nodes)

        while q:
            # Pick min_node from q with the smallest cost of travel.
            min_node = None
            for node in q:
                if min_node is None:
                    min_node = node
                elif cost[node] < cost[min_node]:
                    min_node = node

            # Delete picked node from q set and add it to s set.
            s.add(min_node)
            q.remove(min_node)

            # Check if you can from your min_node travel to min_node neighbours with smaller cost.
            for neighbour in self.edges[min_node]:
                if neighbour in q and cost[neighbour] > cost[min_node] + self.distance[neighbour]:
                    cost[neighbour] = cost[min_node] + self.distance[neighbour]
                    predecessor[neighbour] = min_node

        return cost[max(self.nodes)]


if __name__ == "__main__":
    my_journey = Journey("plik.txt")
    my_journey.give_shortest_paths()
