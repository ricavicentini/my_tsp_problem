"""
Tests for the main module functionality.
"""

import pytest
from main import main


def test_main_function_output(capsys, expected_welcome_message):
    """Test that the main function prints the expected welcome message."""
    # Call the main function
    main()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that the expected message is in the output
    assert expected_welcome_message in captured.out
    assert captured.err == ""  # No error output expected


def test_main_function_callable():
    """Test that the main function can be called without raising exceptions."""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")


class TestMainModule:
    """Test class for main module functionality."""
    
    def test_main_function_exists(self):
        """Test that the main function exists and is callable."""
        assert callable(main)
    
    def test_main_function_returns_none(self):
        """Test that the main function returns None (as expected for a main function)."""
        result = main()
        assert result is None 