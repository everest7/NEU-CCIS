from stack import Stack


class StringProcessor:
    """Class for processing strings"""

    def process_string(self, string):
        """Process the string to decode

        Args:
            String needs to be decoded

        Returns:
            A decoded string
        """
        stack = Stack()
        solution = ''
        for ch in string:
            if ch == '*':
                if len(stack.items) > 0:
                    char = stack.pop()
                    solution += char
            elif ch == '^':
                if len(stack.items) > 0:
                    char1 = stack.pop()
                    char2 = stack.pop()
                    solution += char1
                    solution += char2
            else:
                stack.push(ch)
        return solution
