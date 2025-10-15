class Solution:
    def reverseVowels(self, s: str) -> str:
        left_pointer = 0
        right_pointer = len(s) - 1
        array = list(s)
        vowelset = set('aeiouAEIOU')

        while left_pointer < right_pointer:
            if array[left_pointer] in vowelset and array[right_pointer] in vowelset:
                array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
                left_pointer += 1
                right_pointer -= 1
            elif array[left_pointer] not in vowelset:
                left_pointer += 1
            elif array[right_pointer] not in vowelset:
                right_pointer -= 1

        return "".join(array)