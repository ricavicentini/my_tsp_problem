"""
Unit tests for the cities logic module.
"""

import pytest
import math
from logic.cities import calculate_distance, calculate_total_distance, routes_to_cities


class TestCalculateDistance:
    """Test cases for the calculate_distance function."""
    
    def test_calculate_distance_positive_coordinates(self):
        """Test distance calculation with positive coordinates."""
        city1 = (0, 0)
        city2 = (3, 4)
        expected_distance = 5.0  # 3-4-5 triangle
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
        assert isinstance(result, float)
    
    def test_calculate_distance_zero_distance(self):
        """Test distance calculation when both cities are at the same location."""
        city1 = (10, 20)
        city2 = (10, 20)
        expected_distance = 0.0
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
        assert isinstance(result, float)
    
    def test_calculate_distance_negative_coordinates(self):
        """Test distance calculation with negative coordinates."""
        city1 = (-3, -4)
        city2 = (0, 0)
        expected_distance = 5.0  # 3-4-5 triangle
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
    
    def test_calculate_distance_mixed_coordinates(self):
        """Test distance calculation with mixed positive and negative coordinates."""
        city1 = (-2, 3)
        city2 = (1, -1)
        # Distance = sqrt((1-(-2))^2 + (-1-3)^2) = sqrt(9 + 16) = sqrt(25) = 5
        expected_distance = 5.0
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
    
    def test_calculate_distance_large_coordinates(self):
        """Test distance calculation with large coordinates."""
        city1 = (1000, 2000)
        city2 = (1300, 2400)
        # Distance = sqrt((1300-1000)^2 + (2400-2000)^2) = sqrt(300^2 + 400^2) = sqrt(90000 + 160000) = sqrt(250000) = 500
        expected_distance = 500.0
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
    
    def test_calculate_distance_floating_point_precision(self):
        """Test distance calculation with floating point precision."""
        city1 = (1, 1)
        city2 = (2, 2)
        expected_distance = math.sqrt(2)  # approximately 1.414
        
        result = calculate_distance(city1, city2)
        
        assert abs(result - expected_distance) < 1e-10
    
    def test_calculate_distance_horizontal_line(self):
        """Test distance calculation for cities on a horizontal line."""
        city1 = (0, 5)
        city2 = (10, 5)
        expected_distance = 10.0
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
    
    def test_calculate_distance_vertical_line(self):
        """Test distance calculation for cities on a vertical line."""
        city1 = (5, 0)
        city2 = (5, 8)
        expected_distance = 8.0
        
        result = calculate_distance(city1, city2)
        
        assert result == expected_distance
    
    def test_calculate_distance_symmetry(self):
        """Test that distance calculation is symmetric (distance(A,B) == distance(B,A))."""
        city1 = (10, 20)
        city2 = (30, 40)
        
        distance_ab = calculate_distance(city1, city2)
        distance_ba = calculate_distance(city2, city1)
        
        assert distance_ab == distance_ba
    
    def test_calculate_distance_real_world_coordinates(self):
        """Test distance calculation with real-world-like coordinates."""
        # Using coordinates from the cities_locations data
        city1 = (533, 251)
        city2 = (506, 87)
        # Distance = sqrt((506-533)^2 + (87-251)^2) = sqrt(729 + 26896) = sqrt(27625) ≈ 166.24
        expected_distance = math.sqrt(27625)
        
        result = calculate_distance(city1, city2)
        
        assert abs(result - expected_distance) < 1e-10
    
    @pytest.mark.parametrize("city1,city2,expected", [
        ((0, 0), (0, 1), 1.0),
        ((0, 0), (1, 0), 1.0),
        ((0, 0), (1, 1), math.sqrt(2)),
        ((2, 2), (5, 6), 5.0),
        ((-1, -1), (2, 3), 5.0),
    ])
    def test_calculate_distance_parametrized(self, city1, city2, expected):
        """Parametrized test for various distance calculations."""
        result = calculate_distance(city1, city2)
        assert abs(result - expected) < 1e-10
    
    def test_calculate_distance_type_checking(self):
        """Test that the function handles correct input types."""
        city1 = (10, 20)
        city2 = (30, 40)
        
        result = calculate_distance(city1, city2)
        
        assert isinstance(result, float)
        assert result > 0
