"""Tests for utils.py"""
# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long, redefined-outer-name, missing-function-docstring

import pytest
from santorini import utils


def test_is_adjacent():
    assert utils.is_adjacent((0,1), (1,1)) is True
    assert utils.is_adjacent((2,4), (1,3)) is True
    assert utils.is_adjacent((0,0), (0,1)) is True
    assert utils.is_adjacent((4,3), (4,3)) is False
    assert utils.is_adjacent((0,0), (1,2)) is False

def test_valid_algebraic_positions():
    assert utils.algebraic_position_to_indices("A1") == (0, 0)
    assert utils.algebraic_position_to_indices("B2") == (1, 1)
    assert utils.algebraic_position_to_indices("H8") == (7, 7)
    assert utils.algebraic_position_to_indices("A10") == (9, 0)

def test_invalid_algebraic_positions():
    with pytest.raises(ValueError):
        utils.algebraic_position_to_indices("1A")
    with pytest.raises(ValueError):
        utils.algebraic_position_to_indices("AA")
    with pytest.raises(ValueError):
        utils.algebraic_position_to_indices("")
    with pytest.raises(ValueError):
        utils.algebraic_position_to_indices("B")
