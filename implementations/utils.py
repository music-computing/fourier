# coding: utf-8
"""
Demonstrate Fourier equivalences.

Additional, basic, shared functionality beyond that provided in `vectors_sets`.

Source: [redacted]
"""

from __future__ import annotations
from typing import Iterable

__author__ = "Anonymous for blind submission"

import numpy as np


def fourier_magnitudes(input: Iterable) -> np.array:
    """Convenience function to ensure consistent handling of Fourier magnitude."""
    return np.absolute(np.fft.fft(input))


def items_to_differences(
        items: list | tuple,
        more_items: list | tuple | None = None,
        modulo: int | None = 12
):
    """
    Return the differences between integers.
    Among other application, this gives the intervals between pitch classes.

    Args:
         items: a list or tuple of integers.
            This may include duplicate entries (it may be a set or a multi-set), but see notes below.
         more_items: optionally specify a second set.
            If provided, calculate the differences between the two sets (as in the 'interval function').
            If None, this function creates a copy of the orignal set and
            calculates the differences between items of the same set (as in the 'interval vector').
         modulo: optionally specify a modulo value. Defaults to 12 for the case of 12-TET (-1 == 11).

    >>> test_items = [1, 2, 3, 9]
    >>> internal = items_to_differences(test_items, modulo=12)
    >>> internal
    (1, 2, 8, 1, 7, 6)

    Note that this internal-only version avoids duplicates.
    If you call it on the same set twice, you get everything twice (all intervals in both directions):

    >>> as_interval_function = items_to_differences(test_items, test_items, modulo=12)
    >>> as_interval_function
    (0, 1, 2, 8, 11, 0, 1, 7, 10, 11, 0, 6, 4, 5, 6, 0)
    """
    differences = []

    if more_items:
        for start in items:
            for end in more_items:
                differences.append((end - start) % modulo)
    else:
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                diff = (items[j] - items[i]) % modulo
                differences.append(diff)

    return tuple(differences)


def interval_to_interval_class(interval: int) -> int:
    """
    Map an integer to an interval class (integer in the range 0–6).

    >>> interval_to_interval_class(0)
    0

    >>> interval_to_interval_class(-1)
    1

    >>> interval_to_interval_class(-2)
    2

    >>> interval_to_interval_class(11)
    1

    >>> interval_to_interval_class(7)
    5
    """
    return (abs(interval) % 12) if (abs(interval) % 12) <= 6 else (12 - (abs(interval) % 12))


def interval_vector_to_interval_class_vector(interval_vector: tuple[int, ...]) -> tuple[int, ...]:
    """
    Map an interval vector (length 0-11) to an interval class vector (1-6).

    >>> interval_vector_to_interval_class_vector((1, 0, 5, 7, 2, 2, 0, 3, 5, 0, 8, 4))
    (4, 13, 7, 7, 5, 0)
    """
    interval_class_vector = [0] * 6
    for i in range(1, 6):
        interval_class_vector[i - 1] = interval_vector[i] + interval_vector[12 - i]

    interval_class_vector[5] = interval_vector[6]  # special case
    return tuple(interval_class_vector)


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()