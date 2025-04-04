# coding: utf-8
"""
Demonstrate Fourier equivalences.

Basic, shared functionality.
Arguments are typically named simple `input_list`.
We typically use this for lists of integers,
 but these function does not require this and will accept any list,
 in many cases accepting even any objects.
 Typing hints indicate any constraints.

Source: [redacted]
"""

from __future__ import annotations

__author__ = "Anonymous for blind submission"

import numpy as np


def fourier_magnitudes(input_list: list) -> list:
    """Convenience function to ensure consistent handling of Fourier magnitude."""
    return np.absolute(np.fft.fft(input_list))


def rotate(
        input_list: list[int],
        n: int | None = None
) -> list:
    """
    Rotate a list by N steps.

    :param input_list: Any list.
    :param n: how many steps to rotate.
        Or, equivalently, the nth index of the input list becomes the 0th index of the new.
        If unspecified, use the half cycle: int(<cycle lenth>/2).

    >>> rotate([0, 1, 2, 3])
    [2, 3, 0, 1]

    """
    if not n:
        n = int(len(input_list) / 2)
        assert n > 1

    return input_list[n:] + input_list[:n]


def mirror(
        input_list: list | tuple,
        index_of_symmetry: int | None = None
) -> list:
    """
    Reverse a list.

    Args:
    input_list: Any list.
    index_of_symmetry: Defaults to None, in which case, standard refelction [::-1].
        Alternatively, specify an index to rotate about, e.g., for the reverse function in convolution use 0.
        This is equivalent to mirror and rotation.
        See notes at `rotate`.

    >>> test_case = [0, 1, 2, 3, 4, 5]
    >>> mirror(test_case)
    [5, 4, 3, 2, 1, 0]

    >>> mirror(test_case, index_of_symmetry=0)
    [0, 5, 4, 3, 2, 1]

    >>> mirror(test_case, index_of_symmetry=1)
    [1, 0, 5, 4, 3, 2]
    """
    if index_of_symmetry is not None:
        return input_list[index_of_symmetry::-1] + input_list[-1:index_of_symmetry:-1]
    else:
        return input_list[::-1]


def multiply(
        input_list: list,
        scale_factor: int = 2
) -> list:
    """
    Multiply all values of a list.

    Args:
    input_list: Any list.
    scale_factor: The "scale factor" aka "multiplicative operand". Multiply all terms by this amount. Defaults to 2.

    >>> multiply([0, 1, 2])
    [0, 2, 4]

    """
    return [x * scale_factor for x in input_list]  # TODO np would be better here.


def is_indicator_vector(indicator_vector: list | tuple) -> bool:
    """Check that a list or tuple is an indicator vector, featuring only 0s and 1s."""
    if all(x in (0, 1) for x in indicator_vector):
        return True


def complement(indicator_vector: list) -> list:
    """
    Provide the complement of an indicator vector.
    >>> complement([1, 0, 1, 0])
    [0, 1, 0, 1]
    """
    if not is_indicator_vector(indicator_vector):
        raise ValueError("This is to be called only on binary lists (indicator vectors).")
    return [1 - x for x in indicator_vector]


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


def set_to_vector(
        input_set: list[int] | tuple[int],
        min_index: int | None = 0,
        max_index: int | None = 6
) -> tuple:
    """
    Converts any "set" (list of integers) into a "vector" (count of integers organised by index).
    See the paper for full definitions.
    This is similar to the collections.Counter function, simply returning an ordered list instead of a dict.

    Args:
        input_set: The input integers.
        min_index: The minimum index to use. Defaults to 0. Use 1 for interval vectors, to exlcude 0.
        max_index: The maximum index to use. Defaults to 6 for interval vectors.

    >>> test_set = [1, 2, 3]
    >>> set_to_vector(test_set, min_index=0, max_index=6)
    (0, 1, 1, 1, 0, 0, 0)

    >>> set_to_vector(test_set, min_index=1, max_index=6)
    (1, 1, 1, 0, 0, 0)

    >>> set_to_vector(test_set, max_index=None)
    (0, 1, 1, 1)

    """
    if not max_index:
        max_index = max(input_set)
    counts = [0] * (max_index + 1)
    for item in input_set:
        counts[item] += 1

    if min_index > 0:
        counts = counts[min_index:]

    return tuple(counts)


def vector_to_set(
        vector: list[int] | tuple[int]
) -> tuple:
    """
    Converts any "vector" (count of integers organised by index)
    to a corresponding "set" (unordered list of integers).
    See the paper for full definitions.

   Args:
       vector: The input vector.

   Returns:
       A tuple representing the set.

    Examples:
    >>> test_vector = (0, 3, 2, 1, 0, 0, 0)
    >>> resulting_set = vector_to_set(test_vector)
    >>> resulting_set
    (1, 1, 1, 2, 2, 3)

    >>> roundtrip = set_to_vector(resulting_set, max_index=6)
    >>> roundtrip
    (0, 3, 2, 1, 0, 0, 0)

    >>> roundtrip == test_vector
    True

    """
    return tuple(i for i in range(len(vector)) for _ in range(vector[i]))


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()