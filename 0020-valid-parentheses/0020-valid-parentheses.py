from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack : list = []
        Hashmap : dict = defaultdict(int)
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                Hashmap[ch] += 1
                stack.append(ch)
            else:
                if ch == ']':
                    if '[' not in Hashmap or Hashmap['['] == 0:
                        return False
                    elif stack[-1] != '[':
                        return False
                    stack.pop()
                    Hashmap['['] -= 1
                elif ch == '}':
                    if '{' not in Hashmap or Hashmap['{'] == 0:
                        return False
                    elif stack[-1] != '{':
                        return False
                    stack.pop()
                    Hashmap['{'] -= 1
                else:
                    if '(' not in Hashmap or Hashmap['('] == 0:
                        return False
                    elif stack[-1] != '(':
                        return False
                    stack.pop()
                    Hashmap['('] -= 1
        return len(stack) == 0