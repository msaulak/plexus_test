"""Module representing a Triangle of glasses
"""

import datetime
import os

from libs.complete_list_solution.glass import Glass


class GlassTriangle():
    """Class representing a glass triangle
    """

    def __init__(self, capacity_per_glass):
        """Initialize the triagle
        :param capacity_per_glass:
        """
        self.how_much_water_to_pour = None
        self.left_over_volume = None
        self.glasses_triangle = []
        self.capacity_per_glass = capacity_per_glass

    def _init_triangle(self):
        """Initalize the triangle and add the first glass if needed
        :return:
        """
        self.left_over_volume = None
        self.glasses_triangle = []

        self.glasses_triangle.append([Glass(0, 0, self.capacity_per_glass)])
        self.glasses_triangle[0][0].current_volume = self.how_much_water_to_pour
        self.left_over_volume = self.how_much_water_to_pour

        return True

    def add_row_of_glasses(self, level):
        """Adds a row of glasses to the bottom of the triangle.
        The number of glasses in the row = depth of the row
        For example, at depth 3 there are 3 glasses.
        :param level: depth of the row in the triangle
        :return:
        """
        glasses_created = 0
        glass_row = []
        while (glasses_created <= level):
            glass_row.append(Glass(level, glasses_created, self.capacity_per_glass))
            glasses_created += 1

        self.glasses_triangle.append(glass_row)

    def get_glass_at_i_and_j(self, i, j):
        """Gets the glass at location i,j. Raises IndexError if i or j
        is out of bounds.
        :return:
        """
        try:
            return self.glasses_triangle[i][j]
        except IndexError:
            raise IndexError(f'Could not find a glass in the triangle at co-ordinates {i}, {j}. '
                             f'Maximum values of i and j should be {len(self.glasses_triangle) - 1} where '
                             f'i <= j')

    def get_as_list(self):
        """Returns the glass triangle as a list of list
        :return:
        """
        return_list = []
        for glass_row in self.glasses_triangle:
            row_list = []
            for glass in glass_row:
                row_list.append(glass.current_volume)

            return_list.append(row_list)

        return return_list

    def fill_triangle(self, how_much_water_to_pour):
        """Method which begins distributing the value in how_much_water_to_pour
        to the glasses in the triangle.
        :param how_much_water_to_pour:
        :return:
        """

        self.how_much_water_to_pour = how_much_water_to_pour
        # Doing some sanity check
        if how_much_water_to_pour < 0:
            raise ValueError(f'Negative value {self.how_much_water_to_pour} can not be poured into the triangle. '
                             f'It must be a whole number.')

        # Perform 2 base cases here to avoid unnecessary computation below
        if how_much_water_to_pour == 0:
            self.glasses_triangle = []
            return

        if how_much_water_to_pour <= self.capacity_per_glass:
            self.glasses_triangle = [[Glass(0, 0, self.capacity_per_glass)]]
            self.glasses_triangle[0][0].current_volume = how_much_water_to_pour
            return

        if not self._init_triangle():  # If something went wrong in initializing the triangle, return
            return

        for vertical_position, glass_row in enumerate(self.glasses_triangle):

            # has_left_over = False
            for horizontal_position, glass in enumerate(glass_row):

                if self.left_over_volume <= 0:
                    break

                if glass.current_volume > glass.max_capacity:

                    self.left_over_water = glass.current_volume - glass.max_capacity

                    #Fill the current glass to max
                    self.glasses_triangle[vertical_position][horizontal_position].current_volume = glass.max_capacity

                    # add a row this is the last row and there is more water to distribute
                    if vertical_position + 1 >= len(self.glasses_triangle):
                        self.add_row_of_glasses(vertical_position + 1)

                    # left child
                    self.glasses_triangle[vertical_position + 1][
                        horizontal_position].current_volume += self.left_over_water / 2
                    # right child
                    self.glasses_triangle[vertical_position + 1][
                        horizontal_position + 1].current_volume += self.left_over_water / 2

            if self.left_over_volume <= 0:
                break

    def __str__(self):
        """String representation of the triangle
        :return:
        """
        return_str = ''
        max_tabs = len(self.glasses_triangle)
        for glass_row in self.glasses_triangle:
            return_str += ''.join(["\t\t\t"] * max_tabs)
            for glass in glass_row:
                return_str += str(glass) + "\t\t"
            return_str += '\n\n'
            max_tabs -= 1

        return return_str  # str(self.glasses_triangle)

    def __repr__(self):
        return self.__str__()

    def export_as_graph_data(self):
        """Safe version to export the triangle data as a graph data with edges.
        This data can be printed on the console, copied and pasted on
        https://dreampuf.github.io/GraphvizOnline to see a visual representation
        :return:
        """
        try:
            graph = self._get_graph()
            return graph
        except ImportError as e:
            print(
                "Failed to import graph modules. Please see the below error. "
                "You can print the object to get a string representation.")
            print(e)
        except Exception as e:
            print(
                "Failure to export glass triangle as a graph. Please see the below error. "
                "You can print the object to get a string representation.")
            print(e)

        return None

    def _get_graph(self):
        """Translates the glass triangle to a pydot graph object
        :return:
        """
        import pydot
        graph = pydot.Dot(graph_type='graph')

        for i in range(len(self.glasses_triangle)):
            edges = []
            for j in range(len(self.glasses_triangle[i])):

                graph.add_node(pydot.Node(self.glasses_triangle[i][j].get_graph_node_string(),
                                          shape='box', style='striped', fontcolor="green",
                                          gradientangle=15,
                                          fillcolor=self.glasses_triangle[i][j].get_node_fill_color()))
                try:
                    edges.append(pydot.Edge(self.glasses_triangle[i][j].get_graph_node_string(),
                                            self.glasses_triangle[i + 1][j].get_graph_node_string()))

                    edges.append(pydot.Edge(self.glasses_triangle[i][j].get_graph_node_string(),
                                            self.glasses_triangle[i + 1][j + 1].get_graph_node_string()))

                except IndexError as e:
                    continue

            for edge in edges:
                graph.add_edge(edge)
        return graph

    def export_as_graph_image(self):
        """Create a png image, representing the triangle as a graph, on the local machine.
        :return:
        """
        graph_data = self.export_as_graph_data()

        if graph_data:
            try:
                import pydot
                dot_file_name = f'glass_triangle_{datetime.datetime.utcnow()}.dot'
                graph_data.write(dot_file_name)
                from subprocess import check_call
                (graph,) = pydot.graph_from_dot_file(dot_file_name)

                image_file_name = (f'glass_triangle_holding_{self.how_much_water_to_pour}'
                                   f'_ml_with_{self.capacity_per_glass}_ml_per_glass.png')
                graph.write_png(image_file_name)
                print(f'See image file {image_file_name}')
                os.remove(dot_file_name)

            except ImportError as e:
                print(
                    "Failed to import graph modules. Please see the below error. "
                    "You can print the object to get a string representation.")
                print(e)
            except Exception as e:
                print(
                    "Failure to export glass triangle as a graph. Please see the below error. "
                    "You can print the object to get a string representation.")
                print(e)

            return None
