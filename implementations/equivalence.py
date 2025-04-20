# coding: utf-8
"""
Demonstrate Fourier equivalences.
Source: [redacted]
"""

__author__ = "Anonymous for blind submission"

import numpy as np
from implementations.utils import fourier_magnitudes
from implementations.vectors_sets import complement, mirror, rotate, scalar_multiply

operations = ["rotate", "mirror", "multiply", "complement"]  # NB: not repeat.


def equivalence_comparison(
        vector: tuple[int, ...],
        operation: str = "rotation"
) -> bool:
    """
    Creates a modified form of a set and checks equivalence.

    Check this (from scratch) against built in `np.eye`.

    >>> c_maj_profile = (1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1)
    >>> equivalence_comparison(c_maj_profile, operation="rotate")
    True

    >>> equivalence_comparison(c_maj_profile, operation="mirror")
    True

    :param vector: the input data to test.
    :param operation: the change to make. Chose from
        "rotate" (e.g., pitch transpose),
        "mirror" (e.g., rhythm retrograde transpose for pitch),
        "multiply" (amplitudes),
        "complement".
        Note that repeat is handled separately.

    return: bool
    """

    before = fourier_magnitudes(vector)

    if operation == "rotate":
        after = rotate(vector)
    elif operation == "mirror":
        after = mirror(vector)
    elif operation == "multiply":
        after = scalar_multiply(vector, scale_factor=2)
    elif operation == "complement":
        after = complement(vector)
    else:
        raise ValueError(f"Invalid operation: must be one of {operations}")

    after = fourier_magnitudes(after)
    if np.allclose(before, after):
        return True
    else:
        return False



def demonstrate_repeat_mapping(
        vector: tuple,
        num_repeats: int = 4
) -> bool:
    """
    Demonstrates the slightly different case of repetition.

    >>> c_maj_profile = (1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1)
    >>> demonstrate_repeat_mapping(c_maj_profile)
    True

    """
    before = fourier_magnitudes(vector)
    after = fourier_magnitudes(vector * num_repeats)
    assert np.allclose(before, after[::num_repeats] / num_repeats)
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
