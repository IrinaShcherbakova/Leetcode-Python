class Term:
    
    def __init__(self, value: int, op: str):
        self.val = value
        self.op = op
        
    def get_value(self) -> int:
        return self.val
    
    def set_value(self, new_val: int) -> None:
        self.val = new_val

    def get_op(self) -> str:
        return self.op
    
    
    
class Solution:
    def calculate(self, s: str) -> int:
        processing, result = None, 0
        sequence = self.parse_expression(s)
        for i,term in enumerate(sequence):
            print("term: %s, sign: %s" %(term.get_value(),term.get_op()))
            next_term = (sequence[i+1] if i+1 < len(sequence) else None)
            processing = self.collapse_term(processing, term)
            
            if not next_term or next_term.get_op() == '+' or next_term.get_op() == '-':
                result = self.apply_op(result, processing.get_op(), processing.get_value())
                processing = None
        
        return result

    
    def collapse_term(self, primary: Term, secondary: Term) -> Term:
        if not primary or not secondary:
            return (primary if not secondary else secondary)
        value = self.apply_op(primary.get_value(), secondary.get_op(), secondary.get_value())
        primary.set_value(value)
        return primary
        
 
    def apply_op(self, left: int, op: str, right: int) -> int:
        if op == '+':
            return left + right
        if op == '-':
            return left - right
        if op == '*':
            return left * right
        return left // right
    
    
    def parse_expression(self, s: str) -> List[Term]:
        sequence = []
        first_num, index = self.read_number(s, 0)
        sequence.append(Term(first_num, "+"))
        while index < len(s) and index > 0:
            op, index = self.read_op(s, index)
            if not op:
                break
            num, index = self.read_number(s, index)
            sequence.append(Term(num, op))            
        return sequence
    
    
    # returns number and next index
    def read_number(self, s: str, index: int) -> tuple:
        index = self.skip_whitespaces(s, index)
        if index < 0:
            return None, index
        number = ""
        while index < len(s) and s[index].isdigit():
            number += s[index]
            index += 1
        return int(number), index
    
    
    # returns operator and next index
    def read_op(self, s: str, index: int) -> tuple:
        index = self.skip_whitespaces(s, index)
        if index < 0:
            return None, index
        op = s[index]
        return op, index+1
    
    
    # skip whitespaces in the input strings and returns next non empty index
    def skip_whitespaces(self, s: str, index: int) -> int:
        if index >= len(s):
            return -1
        while index < len(s) and s[index] == " ":
            index += 1
        return (index if index < len(s) else -1)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
