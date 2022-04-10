# -*- coding: utf-8 -*-


def count_and_say(n):
    last = []
    cur = []
    for i in range(n):
        cur = []
        if i == 0:
            cur.append(1)
            last = cur[:]
        else:
            count = 0
            tmp_num = None
            for item in last:
                if tmp_num != None and item != tmp_num:
                    cur.append(count)
                    cur.append(tmp_num)
                    tmp_num = item
                    count = 1
                else:
                    tmp_num = item
                    count += 1
            cur.append(count)
            cur.append(tmp_num)
            last = cur[:]
        print(cur)


if __name__ == "__main__":
    count_and_say(50)

