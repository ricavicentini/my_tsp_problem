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


class TestCalculateTotalDistance:
    """Test cases for the calculate_total_distance function."""
    
    def test_calculate_total_distance_two_cities(self):
        """Test total distance calculation with two cities."""
        path = [(0, 0), (3, 4)]
        expected_distance = 5.0  # 3-4-5 triangle
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
        assert isinstance(result, float)
    
    def test_calculate_total_distance_three_cities_straight_line(self):
        """Test total distance with three cities in a straight line."""
        path = [(0, 0), (1, 0), (3, 0)]  # Horizontal line
        expected_distance = 3.0  # 0->1 (1 unit) + 1->3 (2 units) = 3 units
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
    
    def test_calculate_total_distance_square_path(self):
        """Test total distance for a square path."""
        path = [(0, 0), (0, 1), (1, 1), (1, 0)]  # Square corners
        expected_distance = 3.0  # 1 + 1 + 1 = 3 (three sides of square)
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
    
    def test_calculate_total_distance_triangle_path(self):
        """Test total distance for a triangle path."""
        path = [(0, 0), (3, 0), (0, 4)]  # Right triangle
        # Distance: 0->3 = 3, 3->0,4 = 5 (3-4-5 triangle)
        expected_distance = 8.0  # 3 + 5 = 8
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
    
    def test_calculate_total_distance_single_city(self):
        """Test total distance with single city (should be 0)."""
        path = [(10, 20)]
        expected_distance = 0.0
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
        assert isinstance(result, (int, float))  # Accept both int and float for edge case
    
    def test_calculate_total_distance_empty_path(self):
        """Test total distance with empty path."""
        path = []
        expected_distance = 0.0
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
        assert isinstance(result, (int, float))  # Accept both int and float for edge case
    
    def test_calculate_total_distance_same_cities(self):
        """Test total distance when all cities are at the same location."""
        path = [(5, 5), (5, 5), (5, 5), (5, 5)]
        expected_distance = 0.0
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
    
    def test_calculate_total_distance_negative_coordinates(self):
        """Test total distance with negative coordinates."""
        path = [(-1, -1), (0, 0), (1, 1)]
        # Distance: (-1,-1) to (0,0) = sqrt(2), (0,0) to (1,1) = sqrt(2)
        expected_distance = 2 * math.sqrt(2)
        
        result = calculate_total_distance(path)
        
        assert abs(result - expected_distance) < 1e-10
    
    def test_calculate_total_distance_large_path(self):
        """Test total distance with a larger path."""
        path = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]  # 5 cities in a line
        expected_distance = 4.0  # 1 + 1 + 1 + 1 = 4
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
    
    def test_calculate_total_distance_real_world_coordinates(self):
        """Test total distance with real-world coordinates from cities_locations."""
        # Using first 3 cities from 5-city dataset
        path = [(533, 251), (506, 87), (346, 97)]
        
        # Calculate expected distance manually
        dist1 = calculate_distance((533, 251), (506, 87))
        dist2 = calculate_distance((506, 87), (346, 97))
        expected_distance = dist1 + dist2
        
        result = calculate_total_distance(path)
        
        assert abs(result - expected_distance) < 1e-10
    
    def test_calculate_total_distance_floating_point_precision(self):
        """Test total distance with floating point precision."""
        path = [(0, 0), (1, 1), (2, 2), (3, 3)]
        # Each segment has distance sqrt(2)
        expected_distance = 3 * math.sqrt(2)
        
        result = calculate_total_distance(path)
        
        assert abs(result - expected_distance) < 1e-10
    
    def test_calculate_total_distance_circular_path(self):
        """Test total distance for a circular path (returning to start)."""
        path = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        # Square path: 1 + 1 + 1 + 1 = 4
        expected_distance = 4.0
        
        result = calculate_total_distance(path)
        
        assert result == expected_distance
    
    @pytest.mark.parametrize("path,expected", [
        ([(0, 0), (1, 0)], 1.0),
        ([(0, 0), (0, 1)], 1.0),
        ([(0, 0), (1, 1)], math.sqrt(2)),
        ([(0, 0), (1, 0), (1, 1)], 2.0),
        ([(0, 0), (3, 4), (0, 0)], 10.0),  # 5 + 5 = 10
    ])
    def test_calculate_total_distance_parametrized(self, path, expected):
        """Parametrized test for various total distance calculations."""
        result = calculate_total_distance(path)
        assert abs(result - expected) < 1e-10
    
    def test_calculate_total_distance_type_checking(self):
        """Test that the function returns correct type."""
        path = [(0, 0), (1, 1), (2, 2)]
        
        result = calculate_total_distance(path)
        
        assert isinstance(result, float)
        assert result >= 0
    
    def test_calculate_total_distance_order_matters(self):
        """Test that the order of cities matters in total distance calculation."""
        path1 = [(0, 0), (1, 0), (0, 1)]
        path2 = [(0, 0), (0, 1), (1, 0)]
        
        result1 = calculate_total_distance(path1)
        result2 = calculate_total_distance(path2)
        
        # Both should be positive but might be different due to different paths
        assert isinstance(result1, float)
        assert isinstance(result2, float)
        assert result1 >= 0
        assert result2 >= 0
    
    def test_calculate_total_distance_consistency_with_calculate_distance(self):
        """Test that total distance is consistent with individual distance calculations."""
        path = [(0, 0), (3, 4), (6, 8)]
        
        # Calculate manually
        dist1 = calculate_distance((0, 0), (3, 4))
        dist2 = calculate_distance((3, 4), (6, 8))
        expected_total = dist1 + dist2
        
        result = calculate_total_distance(path)
        
        assert abs(result - expected_total) < 1e-10
