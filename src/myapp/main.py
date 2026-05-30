"""
Main module for the application.
"""
from . import Calculator


def main():
    """Main function demonstrating the calculator."""
    calc = Calculator()
    
    # Perform some calculations
    print("Calculator Demo")
    print("===============")
    
    result1 = calc.calculate('add', 10, 5)
    print(f"10 + 5 = {result1}")
    
    result2 = calc.calculate('subtract', 10, 5)
    print(f"10 - 5 = {result2}")
    
    result3 = calc.calculate('multiply', 10, 5)
    print(f"10 * 5 = {result3}")
    
    result4 = calc.calculate('divide', 10, 5)
    print(f"10 / 5 = {result4}")
    
    # Show history
    print("\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry['operation']}: {entry['a']} {entry['b']} = {entry['result']}")
    
    print(f"\nTotal calculations: {len(calc.get_history())}")


if __name__ == "__main__":
    main()
