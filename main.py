from libs.complete_list_solution.glass_triangle import GlassTriangle

def main():

    #Define maximum capacity of each glass in the triangle
    glass_maximum_capacity = 5

    #Create a Glass triangle object
    glass_tree = GlassTriangle(glass_maximum_capacity)

    #fill the triangle with some volume of liquid
    glass_tree.fill_triangle(60)

    #print the triangle as a list of list.
    # First list is the first row, and the so on.
    print (glass_tree.get_as_list())

    #Print the triangle on the console as a triangle
    print (glass_tree)

    # Export the traingle as graph data. Can be plugged into
    # https://dreampuf.github.io/GraphvizOnline to see the graph
    print (glass_tree.export_as_graph_data())

    # Export the graph as an image.
    # Needs pydot. See README.md (I tried it on Linux. Not sure about windows)
    glass_tree.export_as_graph_image()

    #Get a glass at a particular location
    print(glass_tree.get_glass_at_i_and_j(5,5))


if __name__ == "__main__":
    main()