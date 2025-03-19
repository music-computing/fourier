# coding: utf-8
"""
Demonstrate Fourier equivalences.
Source: [redacted]
"""

__author__ = "Anonymous for blind submission"

import numpy as np
from implementations.utils import fourier_magnitudes

operations = ["rotate", "mirror", "multiply", "complement"]  # NB: not repeat.


def equivalence_comparison(
        input_list: list,
        operation: str = "rotation"
) -> np.array:
    """
    Creates a modified form of a set and checks equivalence.

    Check this (from scratch) against built in `np.eye`.

    >>> c_maj_profile = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    >>> equivalence_comparison(c_maj_profile, operation = "rotate")
    True

    >>> equivalence_comparison(c_maj_profile, operation = "mirror")
    True

    :param input_list: the set to test.
    :param operation: the change to make. Chose from
        "rotate" (transpose),
        "mirror",
        "multiply" (amplitudes),
        "complement".
        Note that repeat is handled separately.

    return: bool
    """

    before = fourier_magnitudes(input_list)

    if operation == "rotate":
        after = rotate(input_list)
    elif operation == "mirror":
        after = mirror(input_list)
    elif operation == "multiply":
        after = multiply(input_list)
    elif operation == "complement":
        after = complement(input_list)
    else:
        raise ValueError(f"Invalid operation: must be one of {operations}")

    after = fourier_magnitudes(after)
    if np.allclose(before, after):
        return True
    else:
        return False


def rotate(
        input_list: list,
        n: int | None = None
) -> list:
    """
    Rotate a list by N steps.

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
    return [x * factor for x in input_list]  # TODO np better here.


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


def demonstrate_repeat_mapping(
        input_list: list,
        num_repeats: int = 4
) -> bool:
    """
    Handles the slightly different case of repetition.

    >>> c_maj_profile = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    >>> demonstrate_repeat_mapping(c_maj_profile)
    True

    """
    before = fourier_magnitudes(input_list)
    after = fourier_magnitudes(input_list * num_repeats)
    assert np.allclose(before, after[::num_repeats] / num_repeats)
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
