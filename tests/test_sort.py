import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from main import sort
from enums import Stack


class TestSort(unittest.TestCase):
    """Unit tests for the sort function that classifies packages."""

    def test_standard_small_package(self):
        """Small and light package should go to STANDARD."""
        result = sort(10, 10, 10, 5)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_standard_edge_dimensions(self):
        """Package with large dimensions but exceeds volume limit."""
        result = sort(149, 149, 149, 19)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_standard_edge_mass(self):
        """Package with mass at edge (19kg) should go to STANDARD."""
        result = sort(10, 10, 10, 19)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_standard_edge_volume(self):
        """Package with volume at edge should go to STANDARD."""
        result = sort(99, 100, 100.999, 15)
        self.assertEqual(result, Stack.STANDARD.value)
    
    def test_standard_edge_dimensions_separate(self):
        """Package with one dimension at 149 but small volume."""
        result = sort(149, 10, 10, 15)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_standard_minimum_values(self):
        """Package with minimum values should go to STANDARD."""
        result = sort(1, 1, 1, 1)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_special_bulky_by_width(self):
        """Package with width >= 150 should go to SPECIAL."""
        result = sort(150, 10, 10, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_bulky_by_height(self):
        """Package with height >= 150 should go to SPECIAL."""
        result = sort(10, 150, 10, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_bulky_by_length(self):
        """Package with length >= 150 should go to SPECIAL."""
        result = sort(10, 10, 150, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_bulky_by_volume(self):
        """Package with volume >= 1000000 should go to SPECIAL."""
        result = sort(100, 100, 100, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_bulky_multiple_dimensions(self):
        """Package with multiple dimensions >= 150 should go to SPECIAL."""
        result = sort(150, 150, 10, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_bulky_all_dimensions(self):
        """Package with all dimensions >= 150 should go to SPECIAL."""
        result = sort(150, 150, 150, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_heavy_only(self):
        """Heavy package (>= 20kg) but not bulky should go to SPECIAL."""
        result = sort(10, 10, 10, 20)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_heavy_edge(self):
        """Package with mass exactly 20kg should go to SPECIAL."""
        result = sort(50, 50, 50, 20)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_special_very_heavy(self):
        """Very heavy but small package should go to SPECIAL."""
        result = sort(10, 10, 10, 100)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_rejected_bulky_and_heavy_by_width(self):
        """Bulky by width and heavy should be REJECTED."""
        result = sort(150, 10, 10, 20)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_rejected_bulky_and_heavy_by_height(self):
        """Bulky by height and heavy should be REJECTED."""
        result = sort(10, 150, 10, 20)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_rejected_bulky_and_heavy_by_length(self):
        """Bulky by length and heavy should be REJECTED."""
        result = sort(10, 10, 150, 21)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_rejected_bulky_and_heavy_by_volume(self):
        """Bulky by volume and heavy should be REJECTED."""
        result = sort(100, 100, 100, 25)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_rejected_all_dimensions_and_heavy(self):
        """Package with large dimensions and heavy should be REJECTED."""
        result = sort(200, 200, 200, 50)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_rejected_edge_cases(self):
        """Package at bulky and heavy thresholds should be REJECTED."""
        result = sort(150, 150, 150, 20)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_rejected_volume_threshold_and_heavy(self):
        """Package at volume threshold and heavy should be REJECTED."""
        result = sort(100, 100, 100, 20)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_decimal_dimensions_standard(self):
        """Package with decimal dimensions."""
        result = sort(10.5, 10.5, 10.5, 5.5)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_decimal_dimensions_bulky(self):
        """Package with decimal dimensions exceeding volume threshold."""
        result = sort(149.9, 149.9, 149.9, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_decimal_dimensions_over_limit(self):
        """Package with decimal dimension over limit."""
        result = sort(150.1, 10, 10, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_decimal_mass_under_limit(self):
        """Package with decimal mass below limit."""
        result = sort(10, 10, 10, 19.9)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_decimal_mass_at_limit(self):
        """Package with decimal mass at limit."""
        result = sort(10, 10, 10, 20.0)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_decimal_volume_at_threshold(self):
        """Package with decimal volume at threshold."""
        result = sort(100, 100, 99.999, 10)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_decimal_volume_over_threshold(self):
        """Package with decimal volume over threshold."""
        result = sort(100, 100, 100.1, 10)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_zero_dimensions(self):
        """Package with zero dimensions."""
        result = sort(0, 0, 0, 0)
        self.assertEqual(result, Stack.STANDARD.value)

    def test_very_large_dimensions(self):
        """Package with very large dimensions."""
        result = sort(1000, 1000, 1000, 5)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_very_large_mass(self):
        """Package with very large mass."""
        result = sort(10, 10, 10, 1000)
        self.assertEqual(result, Stack.SPECIAL.value)

    def test_very_large_both(self):
        """Package with very large dimensions and mass."""
        result = sort(1000, 1000, 1000, 1000)
        self.assertEqual(result, Stack.REJECTED.value)

    def test_main_example_case(self):
        """Test the example from main: (10, 150, 10, 21)."""
        result = sort(10, 150, 10, 21)
        self.assertEqual(result, Stack.REJECTED.value)


if __name__ == '__main__':
    unittest.main()
