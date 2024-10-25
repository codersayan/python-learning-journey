import re
import math

class AdvancedCalculator:
    def evaluate_expression(self, expression):
        """Evaluate a mathematical expression and return the result."""
        expression = self.preprocess_expression(expression)
        try:
            result = self.calculate(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def preprocess_expression(self, expression):
        """Preprocess the expression to handle special cases."""
        # Replace square root function
        expression = re.sub(r'sqrt\(([^)]+)\)', r'sqrt(\1)', expression)
        return expression

    def calculate(self, expression):
        """Calculate the value of the expression."""
        # Evaluate square root
        if 'sqrt' in expression:
            return self.handle_sqrt(expression)

        # Handle parentheses
        while '(' in expression:
            expression = self.handle_parentheses(expression)

        # Handle basic arithmetic operations
        return eval(expression)

    def handle_sqrt(self, expression):
        """Handle square root calculations."""
        matches = re.findall(r'sqrt\(([^)]+)\)', expression)
        for match in matches:
            value = eval(match)
            expression = expression.replace(f'sqrt({match})', str(math.sqrt(value)))
        return self.calculate(expression)

    def handle_parentheses(self, expression):
        """Handle expressions inside parentheses."""
        # Find the last opening parenthesis
        open_index = expression.rfind('(')
        close_index = expression.find(')', open_index)
        inner_expression = expression[open_index + 1:close_index]
        # Evaluate the inner expression
        inner_result = self.calculate(inner_expression)
        # Replace the entire parentheses expression with its result
        return expression[:open_index] + str(inner_result) + expression[close_index + 1:]

# Example usage
if __name__ == "__main__":
    calculator = AdvancedCalculator()
    while True:
        user_input = input("Enter a mathematical expression (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        result = calculator.evaluate_expression(user_input)
        print(f"Result: {result}")
