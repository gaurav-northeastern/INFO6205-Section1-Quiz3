def evaluate_expression(expression: str) -> int:
    """
    Evaluate an arithmetic expression using Dijkstra’s Two-Stack Algorithm.

    :param expression: str - The arithmetic expression in infix notation.
    :return: int - The result of evaluating the expression.
    """
    operators = []
    operands = []
    
    def push_operator(op: str):
        """Push an operator onto the operator stack."""
        operators.append(op)
    
    def push_operand(val: int):
        """Push an operand onto the operand stack."""
        operands.append(val)
    
    def pop_operator() -> str:
        """Pop and return the top operator from the operator stack."""
        return operators.pop()
    
    def pop_operand() -> int:
        """Pop and return the top operand from the operand stack."""
        return operands.pop()
    
    def apply_operator(op: str, val1: int, val2: int) -> int:
        """Applies an operator to two operands and returns the result."""
        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2
        elif op == '/':
            return val1 // val2  # Integer division
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        if char == ' ':
            i += 1
            continue
        
        if char == '(':
            pass  # Ignore left parenthesis
        elif char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            push_operand(num)
            i -= 1
        elif char in ['+', '-', '*', '/']:
            push_operator(char)
        elif char == ')':
            op = pop_operator()
            val2 = pop_operand()
            val1 = pop_operand()
            result = apply_operator(op, val1, val2)
            push_operand(result)
        
        i += 1
    
    return pop_operand()

# Example usage
expr = "((3 + 2) * 5)"
print(evaluate_expression(expr))  # Output: 25



