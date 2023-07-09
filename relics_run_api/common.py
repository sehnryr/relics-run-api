from fractions import Fraction
from typing import Dict, Final


"""Relic rarity data.

This is a dictionary of dictionaries. The first key is the relic refinement
level. The second key is the relic drop chance for that refinement level.
The value is the chance of getting a common, uncommon, or rare reward from
that relic refinement level.
"""
RELIC_RARITY = {
    "intact": {
        1: Fraction(76, 100 * 3),
        2: Fraction(22, 100 * 2),
        3: Fraction(2, 100),
    },
    "exceptional": {
        1: Fraction(70, 100 * 3),
        2: Fraction(26, 100 * 2),
        3: Fraction(4, 100),
    },
    "flawless": {
        1: Fraction(60, 100 * 3),
        2: Fraction(34, 100 * 2),
        3: Fraction(6, 100),
    },
    "radiant": {
        1: Fraction(50, 100 * 3),
        2: Fraction(40, 100 * 2),
        3: Fraction(10, 100),
    },
}
