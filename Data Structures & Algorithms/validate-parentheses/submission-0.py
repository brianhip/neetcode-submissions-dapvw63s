
class Solution:
    def isValid(self, s: str) -> bool:
        # input: string with parenthesis
        # output: boolean saying if parenthesis were in the right order
        # idea: use a stack to keep track of the parenthesis order
        
        # use a map to map the close parenthesis to an open parenthesis
        close_to_open_map = {
            ')':'(', 
            '}':'{', 
            ']':'[' 
        }

        open_parenthesis = []
        for parenthesis in s:
            if parenthesis in close_to_open_map:
                if not open_parenthesis:
                    return False
                last_open_parenthesis = open_parenthesis.pop()
                if close_to_open_map[parenthesis] is not last_open_parenthesis:
                    return False
            else:
                open_parenthesis.append(parenthesis)
        return not open_parenthesis