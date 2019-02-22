""" Abstract class for Link List Node

"""
class Node:
    def __init__(self, value: "int"):
        self.value = value
        self.next = None


if __name__ == "__main__":
    # initial node 
    node1 = Node(11)
    node2 = Node(4)

    # set next node
    node1.next = node2

    # total value from link list
    total_value = 0.0

    # Code here


    