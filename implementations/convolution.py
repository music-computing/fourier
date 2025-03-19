# coding: utf-8
"""
Demonstrate convolution, interval vector, and interval function
as they pertain to Fourier methods.

Source: [redacted]
"""

from __future__ import annotations

__author__ = "Anonymous for blind submission"


# ------------------------------------------------------------------------

def convolve(
        vector_1: list | tuple,
        vector_2: list | tuple,
        eliminate_doubling: bool = False
) -> tuple:
    """
    Convolution combines two vectors,
    with a scalar product of corresponding entries
    where they are rotated relative to one another by k steps.
    If the `eliminate_doubling` is True, return only 1s and 0s.

    >>> c_major_triad = (1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0)
    >>> min_7_dyad = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
    >>> convolve(c_major_triad, min_7_dyad)
    (1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0)

    """
    number_elements = len(vector_1)
    if len(vector_2) != number_elements:
        raise ValueError("The lengths of and b must match.")

    combined_list = []
    for k in range(number_elements):
        combined_list.append(
            sum(
                [vector_1[i] * vector_2[k - i % number_elements] for i in range(number_elements)]
            )
        )

    if eliminate_doubling:
        combined_list = [1 if x > 0 else 0 for x in combined_list]
    return tuple(combined_list)


def get_interval_vector(
        vector: list | tuple,
        return_counts: bool = True
) -> tuple:
    """
    Generates the interval vector within a single set:
    the complete set of intervals between items within that set.

    Args:
    vector (list): A list of integers.
    return_counts (bool): If True, returns a tuple with the counts for each integer from 0 to 6.
        (This corresponds to the standard representation in music theory.)
        Otherwise, returns a list of integers.

    Returns:
        tuple: A tuple with the counts for the number of times the interval of that index position occurs.

    >>> test_list = [1, 3, 4, 6]
    >>> get_interval_vector(test_list, return_counts=False)
    (2, 3, 5, 1, 3, 2)

    >>> get_interval_vector(test_list, return_counts=True)  # default
    (0, 1, 2, 2, 0, 1, 0)

    """
    differences = []

    for i in range(len(vector)):
        for j in range(i + 1, len(vector)):
            diff = abs(vector[j] - vector[i])
            differences.append(diff)

    if return_counts:
        differences = values_to_counts(differences)

    return tuple(differences)


def interval_function(
        vector_1: list | tuple,
        vector_2: list | tuple,
        return_counts: bool = True
) -> tuple:
    """
    All intervals between two vectors.
    The interval _function_ was introduced to music theory by Lewin, 2001

    Args:
        vector_1 (list): A vector that may represent a starting condition.
        vector_2 (list): A vector that may represent a following condition.
        return_counts (bool). Re-organise the list of intervals as described for the interval vector.

    Returns:
        tuple

    >>> start_set = [1, 2, 3]
    >>> end_set = [3, 4, 5]
    >>> interval_function(start_set, end_set, return_counts=False)
    (2, 3, 4, 1, 2, 3, 0, 1, 2)

    >>> interval_function(start_set, end_set, return_counts=True)  # default
    (1, 2, 3, 2, 1, 0, 0)

    """
    differences = []
    for start in vector_1:
        for end in vector_2:
            if start <= end:  # Ensure start is less than or equal to end
                differences.append(end - start)

    if return_counts:
        differences = values_to_counts(differences)

    return tuple(differences)


def values_to_counts(
        vector: list | tuple,
        max_val: int | None = 6
) -> tuple:
    """
    Converts any list of integers into a count by index.
    Similar to collections.Counter, but returning an ordered list.

    >>> start_set = [1, 2, 3]
    >>> values_to_counts(start_set)
    (0, 1, 1, 1, 0, 0, 0)

    >>> values_to_counts(start_set, max_val=None)
    (0, 1, 1, 1)

    """
    if not max_val:
        max_val = max(vector)
    counts = [0] * (max_val + 1)
    for difference in vector:
        counts[difference] += 1
    return tuple(counts)


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest

    doctest.testmod()
