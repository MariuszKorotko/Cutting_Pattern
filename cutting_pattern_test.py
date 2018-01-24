import unittest
from cutting_pattern import CuttingPattern


class TestCuttingPattern(unittest.TestCase):

    def setUp(self):
        self.pattern = CuttingPattern([1.0, 2, 1.23], [20, 13, 7], 2, 6)

    def test_pattern_has_attributes(self):
        assert self.pattern.size is not None
        assert self.pattern.quantity is not None
        assert self.pattern.cut_width is not None
        assert self.pattern.pieces is not None
        assert self.pattern.log_length is not None
        assert self.pattern.logs is not None
        assert self.pattern.remaining is not None
        assert self.pattern.final_pattern is not None

    def test_pattern_attributes_by_type(self):
        assert type(self.pattern.size) is list
        assert type(self.pattern.quantity) is list
        assert type(self.pattern.cut_width) is float
        assert type(self.pattern.pieces) is list
        assert type(self.pattern.log_length) is float
        assert type(self.pattern.logs) is int
        assert type(self.pattern.remaining) is list
        assert type(self.pattern.final_pattern) is list

    def test_pattern_has_methods(self):
        assert self.pattern.prepare_pieces is not None
        assert self.pattern.prepare_pattern is not None
        assert self.pattern.print_pattern is not None

    def test_prepare_pieces_method_returns_correct_result(self):
        self.assertEqual(self.pattern.prepare_pieces(),
                         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                          1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0,
                          2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
                          1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23])

    def test_prepare_pattern_method_returns_correct_result(self):
        pieces = self.pattern.prepare_pieces()
        self.assertEqual(self.pattern.prepare_pattern(pieces),
                         [[2.0, 2.0, 1.23], [2.0, 2.0, 1.23], [2.0, 2.0, 1.23],
                          [2.0, 2.0, 1.23], [2.0, 2.0, 1.23], [2.0, 2.0, 1.23],
                          [2.0, 1.23, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
