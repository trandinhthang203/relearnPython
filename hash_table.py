class hash_table:
    def romanToInt(self, s = 'MCMXCIV'):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        left = 0
        list_input = []
        seen = ()

        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in s:
            if i in dict:
                list_input.append(dict[i])
        
        for index, right in enumerate(list_input, start=1):
            while list_input[left] < right:
                result += right - list_input[left]
                del list_input[left:left+1]
                left += 1
                 
            left += 1
        result += sum(list_input)
        return result


h = hash_table()
print(h.romanToInt())