from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # TODO: Implement bracket matching functionality
    # as required by bracket_checker.py and by
    # bracket_match_test.py

    def brackets_match(self, line):
        """Check if a given string is brackets match

        Args:
            line: input string

        Returns:
            True: if the string is brackets match
            False: if the string is not brackets match
        """
        bracket_stack = Stack()
        for ch in line:
            if (ch == '[' or ch == '(' or ch == '{'):
                bracket_stack.push(ch)
            elif (ch == ']'):
                if bracket_stack.peek() == '[':
                    bracket_stack.pop()
                else:
                    return False
            elif (ch == ')'):
                if bracket_stack.peek() == '(':
                    bracket_stack.pop()
                else:
                    return False
            elif (ch == '}'):
                if bracket_stack.peek() == '{':
                    bracket_stack.pop()
                else:
                    return False
        if (len(bracket_stack.items) == 0):
            return True
        else:
            return False
