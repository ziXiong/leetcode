"""
Count And Say
created: 2014/10/25
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
class Solution:
    # @return a string
    def countAndSay(self, n):
        input_ = str(n)
        output = ''
        for _ in range(n):
            last = input_[0]
            count = 0
            for i in range(1, len(input_)):
                if input_[i] == last:
                    count += 1
                else:
                    output = count + last
                    last = input_[i+1]
                    count = 0
        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution(8)
