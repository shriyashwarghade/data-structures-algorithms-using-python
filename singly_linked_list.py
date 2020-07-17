__author__ = 'Shriyash Warghade'
__version__ = '1.0.0'
__maintainer__ = 'Shriyash Warghade'
__email__ = 'warghade.shriyash@gmail.com'
__status__ = 'Development'


class Node:
    def __init__(self, data):
        self.link = None
        self.data = data


root = None


class SingleLinkedList:

    @staticmethod
    def get_data_from_user():
        while True:
            try:
                data = int(input("Enter Value (In Integer): "))
                break
            except:
                print("Invalid Data")
        return Node(data)

    def append(self):
        global root
        temp = self.get_data_from_user()
        if root is None:
            root = temp
        else:
            t = root
            while t.link is not None:
                t = t.link
            t.link = temp
        print("Node Appended Successfully.")

    def add_at_begin(self):
        global root
        temp = self.get_data_from_user()
        if root is None:
            root = temp
        else:
            t = root
            temp.link = t
            root = temp
        print("Node Appended At Begin Successfully.")

    def add_at_end(self):
        global root
        temp = self.get_data_from_user()
        if root is None:
            root = temp
        else:
            t = root
            while t.link is not None:
                t = t.link
            t.link = temp
        print("Node Appended At End Successfully.")

    def add_after(self):
        global root
        if root is None:
            print("Linked List Is Empty.")
            return
        while True:
            try:
                position = int(input("Enter Position To Insert Element:"))
                break
            except:
                print("Invalid Input")
        if position < 0:
            print("Position Cannot Be Negative Value.")
            return
        elif position > self.length():
            print("Invalid Position.")
            return
        temp = self.get_data_from_user()
        t, i = root, 1
        while i < position - 1:
            i += 1
            t = t.link
        p = t.link
        temp.link = p
        t.link = temp
        print("Node Appended At {} Position Successfully.".format(position))

    @staticmethod
    def delete_first_node():
        global root
        if root is None:
            print("Linked List Is Empty.")
            return
        else:
            if root.link is None:
                root = None
            else:
                root = root.link
            print("First Node Deleted Successfully.")

    def delete_specified_node(self):
        global root
        if root is None:
            print("Linked List Is Empty.")
            return
        while True:
            try:
                position = int(input("Enter Position Of Node To Delete:"))
                break
            except:
                print("Invalid Input")
        if position < 0:
            print("Position Cannot Be Negative Value.")
            return
        elif position > self.length():
            print("Invalid Position.")
            return
        t, i = root, 1
        if position == 1:
            root = None if root.link is None else root.link
        else:
            while i < position - 1:
                i += 1
                t = t.link
            p = t.link
            t.link = None if p.link is None else p.link
        print("Node Deleted At {} Position Successfully.".format(position))

    @staticmethod
    def display():
        global root
        if root is None:
            print("Linked List In Empty.")
        else:
            t = root
            data = []
            while t is not None:
                data.append(str("{}--> ".format(t.data)))
                t = t.link
            print("".join(data))

    @staticmethod
    def length():
        global root
        count = 0
        t = root
        while t is not None:
            count += 1
            t = t.link
        return count

    def reverse_list(self):
        global root
        if root is None:
            print("Linked List Is Empty.")
            return
        elif self.length() == 1:
            print("Linked List Has Only 1 Node.")
            return
        t = root
        nodes = []
        while t is not None:
            nodes.append(t)
            t = t.link
        temp = None
        for i in range(len(nodes) - 1, -1, -1):
            nodes[i].link = None
            if temp is None:
                temp = nodes[i]
            else:
                temp1 = temp
                while temp1.link is not None:
                    temp1 = temp1.link
                temp1.link = nodes[i]
        root = temp
        print("Linked List Reversed.")

    def swap(self):
        global root
        if root is None:
            print("Linked List Is Empty.")
            return
        elif self.length() == 1:
            print("Linked List Has Only 1 Node.")
            return
        while True:
            try:
                position1 = int(input("Enter 1st Position Of Node To Swap:"))
                position2 = int(input("Enter 2nd Position Of Node To Swap:"))
                break
            except:
                print("Invalid Input")
        if position1 < 0 or position2 < 0:
            print("Position Cannot Be Negative Value.")
            return
        elif position1 > self.length() or position2 > self.length():
            print("Invalid Position.")
            return
        elif position1 == position2:
            print("Both Positions Can Not Be Same")
            return
        if position1 < position2:
            position1, position2 = position1, position2
        else:
            position1, position2 = position2, position1
        temp2 = temp1 = root
        i = 1
        while i < position1:
            i += 1
            temp1 = temp1.link
        i = 1
        while i < position2:
            i += 1
            temp2 = temp2.link
        temp = temp1.data
        temp1.data = temp2.data
        temp2.data = temp
        print("Node {} Swaped With {}.".format(position1, position2))

    def sort(self):
        global root
        if root is None:
            print("Linked List Is Empty.")
            return
        elif self.length() == 1:
            print("Linked List Has Only 1 Node.")
            return
        t = root
        values = {}
        while t is not None:
            values.update({t.data: t})
            t = t.link
        from collections import OrderedDict
        ordered_dict = OrderedDict(sorted(values.items()))
        temp = None
        for i in ordered_dict.items():
            if temp is None:
                temp = i[1]
                temp.link = None
            else:
                temp1 = temp
                while temp1.link is not None:
                    temp1 = temp1.link
                temp1.link = i[1]
                temp1 = temp1.link
                temp1.link = None
        root = temp
        print("Linked List Sorted Successfully.")


def main():
    single_linked_list = SingleLinkedList()
    print("-" * 20, "SINGLE LINKED LIST", "-" * 20)
    while True:
        print(
            "1.Append\n2.Add At Begin\n3.Add At End\n4.Add After\n5.Delete First Node\n6.Delete Specified Node"
            "\n7.Display\n8.Length\n9.Reverse List\n10.Swap 2 Nodes\n11.Sort\n12.Exit")
        choice = input("Enter Your Choice: ")
        try:
            if int(choice) == 1:
                single_linked_list.append()
            elif int(choice) == 2:
                single_linked_list.add_at_begin()
            elif int(choice) == 3:
                single_linked_list.add_at_end()
            elif int(choice) == 4:
                single_linked_list.add_after()
            elif int(choice) == 5:
                single_linked_list.delete_first_node()
            elif int(choice) == 6:
                single_linked_list.delete_specified_node()
            elif int(choice) == 7:
                single_linked_list.display()
            elif int(choice) == 8:
                print("Length Of Linked List: {}".format(single_linked_list.length()))
            elif int(choice) == 9:
                single_linked_list.reverse_list()
            elif int(choice) == 10:
                single_linked_list.swap()
            elif int(choice) == 11:
                single_linked_list.sort()
            elif int(choice) == 12:
                return
            else:
                print("Invalid Choice")
        except:
            print("Invalid Choice")
        print("-" * 60)


if __name__ == '__main__':
    main()
