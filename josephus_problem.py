# coding=utf-8
__author__ = 'Saqib Razaq'


'''
Josephus problem is a math puzzle with a grim description: n prisoners are standing on a circle, sequentially numbered
from 0 to n − 1. An executioner walks along the circle, starting from prisoner 0, removing every k-th prisoner and
killing him. As the process goes on, the circle becomes smaller and smaller, until only one prisoner remains, who is
then freed.
'''


class Node:

    def __init__(self, id, next=None):
        self.id = id
        self.next = next


def create_list(n):
    node = None
    for i in xrange(n):
        node = Node(i, node)
    head = node
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    return head


def remove_item(n, head):
    while head is not head.next:
        for i in xrange(n):
            head = head.next
        print "Deleted Item with id: {}".format(head.id)
        head.id = head.next.id
        head.next = head.next.next
    print "Winner is item with id: {}".format(head.id)


def main(number_of_items_in_list=57, n=7):
    head = create_list(number_of_items_in_list)
    remove_item(n, head)


if __name__ == '__main__':
    number_of_items_in_list = int(raw_input("How many items should be in the list? "))
    n = int(raw_input("Interval in which items should be removed? "))
    main(number_of_items_in_list, n)