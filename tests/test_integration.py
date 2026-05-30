"""
Integration tests for the application.
"""
import pytest
from myapp import Calculator
from myapp.main import main


class TestIntegration:
    """Integration tests."""

    def test_calculator_workflow(self):
        """Test complete calculator workflow."""
        calc = Calculator()

        # Perform a series of calculations
        calc.calculate('add', 10, 5)
        calc.calculate('subtract', 20, 8)
        calc.calculate('multiply', 3, 7)
        calc.calculate('divide', 100, 10)

        # Verify history
        history = calc.get_history()
        assert len(history) == 4

        # Verify each calculation result
        assert history[0]['result'] == 15
        assert history[1]['result'] == 12
        assert history[2]['result'] == 21
        assert history[3]['result'] == 10

        # Test clearing and reusing calculator
        calc.clear_history()
        assert len(calc.get_history()) == 0

        # Perform new calculations after clearing
        result = calc.calculate('multiply', 6, 6)
        assert result == 36
        assert len(calc.get_history()) == 1

    def test_main_function_output(self, capsys):
        """Test main function produces expected output."""
        main()

        output = capsys.readouterr().out

        # Check that output contains expected elements
        assert "Calculator Demo" in output
        assert "10 + 5 = 15" in output
        assert "10 - 5 = 5" in output
        assert "10 * 5 = 50" in output
        assert "10 / 5 = 2" in output
        assert "Total calculations: 4" in output

    def test_error_handling_integration(self):
        """Test error handling in integrated workflow."""
        calc = Calculator()

        # Test division by zero in workflow
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.calculate('divide', 10, 0)

        # Ensure calculator still works after error
        result = calc.calculate('add', 1, 1)
        assert result == 2

        # Test invalid operation in workflow
        with pytest.raises(ValueError, match="Unknown operation"):
            calc.calculate('invalid', 1, 2)

        # Calculator should still be functional
        result = calc.calculate('subtract', 10, 5)
        assert result == 5
