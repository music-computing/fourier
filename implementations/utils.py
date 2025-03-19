# coding: utf-8
"""
Demonstrate Fourier equivalences.
Source: [redacted]
"""

from __future__ import annotations

__author__ = "Anonymous for blind submission"

import numpy as np


def fourier_magnitudes(input_list: list) -> list:
    """Convenience function to ensure same handling of Fourier magnitude."""
    return np.absolute(np.fft.fft(input_list))


def rotate(
        input_list: list[int],
        n: int | None = None
) -> list:
    """
    Rotate a list by N steps.

    :param input_list: An list of integers.
    :param n: if unspecified, use the half cycle: int(n/2).

    >>> rotate([0, 1, 2, 3])
    [2, 3, 0, 1]

    """
    if not n:
        n = int(len(input_list) / 2)
        assert n > 1

    return input_list[n:] + input_list[:n]


def mirror(input_list: list) -> list:
    """
    Reverse a list

    >>> mirror([0, 1, 2])
    [2, 1, 0]

    """
    return input_list[::-1]


def multiply(
        input_list: list,
        factor: int = 2
) -> list:
    """
    Multiply all values of a set,.

    >>> multiply([0, 1, 2])
    [0, 2, 4]

    """
    return [x * factor for x in input_list]  # TODO np would be better here.


def complement(input_list: list) -> list:
    """
    Provide the complement of a list

    >>> mirror([1, 0, 1, 0])
    [0, 1, 0, 1]

    """
    out_list = []
    for x in input_list:
        if x == 0:
            out_list.append(1)
        elif x == 1:
            out_list.append(0)
        else:
            raise ValueError("This is to be called only on binary lists.")

    return out_list


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()