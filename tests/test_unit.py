"""
Unit tests for the calculator functions.
"""
import pytest
from myapp import add, subtract, multiply, divide, Calculator


class TestBasicFunctions:
    """Test basic arithmetic functions."""
    
    def test_add(self):
        """Test addition."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(100, 200) == 300
    
    def test_subtract(self):
        """Test subtraction."""
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
        assert subtract(0, 0) == 0
    
    def test_multiply(self):
        """Test multiplication."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0
    
    def test_divide(self):
        """Test division."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)


class TestCalculatorClass:
    """Test Calculator class."""
    
    def test_calculator_initialization(self):
        """Test calculator initialization."""
        calc = Calculator()
        assert calc.get_history() == []
    
    def test_calculate_add(self):
        """Test calculator addition."""
        calc = Calculator()
        result = calc.calculate('add', 5, 3)
        assert result == 8
        assert len(calc.get_history()) == 1
    
    def test_calculate_subtract(self):
        """Test calculator subtraction."""
        calc = Calculator()
        result = calc.calculate('subtract', 10, 4)
        assert result == 6
    
    def test_calculate_multiply(self):
        """Test calculator multiplication."""
        calc = Calculator()
        result = calc.calculate('multiply', 6, 7)
        assert result == 42
    
    def test_calculate_divide(self):
        """Test calculator division."""
        calc = Calculator()
        result = calc.calculate('divide', 20, 4)
        assert result == 5
    
    def test_calculate_unknown_operation(self):
        """Test calculator with unknown operation raises error."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Unknown operation"):
            calc.calculate('power', 2, 3)
    
    def test_history_management(self):
        """Test history management."""
        calc = Calculator()
        
        # Perform calculations
        calc.calculate('add', 1, 2)
        calc.calculate('subtract', 5, 3)
        
        history = calc.get_history()
        assert len(history) == 2
        assert history[0]['operation'] == 'add'
        assert history[1]['operation'] == 'subtract'
        
        # Clear history
        calc.clear_history()
        assert calc.get_history() == []
