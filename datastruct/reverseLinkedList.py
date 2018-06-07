# -*- coding: utf-8 -*-


class Struct:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        s = str(self.value)
        n = self
        while n.next:
            s += str(n.next.value)
            n = n.next
            print(n.value)
        return s



def reverse_linklist(first):
    last = first
    next = first.next
    while next:
        cur = next
        next = next.next
        cur.next = last
        last = cur


def reverse(link_list):
    cur = link_list
    next = cur.next
    cur.next = None
    while next:
        tmp = next.next
        next.next = cur
        cur = next
        next = tmp
        # print(next)
        if next is None:
            break

    return cur


if __name__ == "__main__":

    struct = Struct(-1, None)
    tmp = struct
    for i in range(10):
        struct.next = Struct(i, None)
        struct = struct.next
    struct = tmp
    # print(struct)

    struct = reverse_linklist(struct)
    print(struct)

