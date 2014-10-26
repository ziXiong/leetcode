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
        input_str = str(n)
        output_str = ''
        for _ in range(n):
            output_str = self._everyCountAndSay(input_str)
            input_str = output_str
        return output_str

    def _everyCountAndSay(self, n):
        input_str = str(n)
        output_str = ''
        last_char = ''
        count = 0
        for i in range(len(input_str)):
            current_char = input_str[i]
            if current_char == last_char or last_char == '':
                count += 1
            else:
                output_str += str(count) + last_char
                count = 1
            last_char = current_char
        output_str += str(count) + last_char
        return output_str

     
if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(4))
