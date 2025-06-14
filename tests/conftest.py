"""
Shared pytest fixtures and configuration for all tests.
"""

import pytest


@pytest.fixture
def expected_welcome_message():
    """Provide the expected welcome message for consistent testing."""
    return "Welcome to the TSP Problem Solver!"


@pytest.fixture
def sample_coordinates():
    """Provide sample TSP coordinates for testing."""
    return [
        (0, 0),    # City A
        (1, 0),    # City B
        (0, 1),    # City C
        (1, 1),    # City D
    ] 