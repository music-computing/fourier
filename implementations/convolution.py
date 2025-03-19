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
        list_1: list | tuple,
        list_2: list | tuple,
        eliminate_doubling: bool = False
) -> list:
    """
    Convolution combines two vectors,
    with a scalar product of corresponding entries
    where they are rotated relative to one another by k steps.

    >>> c_major_triad = (1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0)
    >>> min_7_dyad = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
    >>> convolve(c_major_triad, min_7_dyad)
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

    """
    number_elements = len(list_1)
    if len(list_2) != number_elements:
        raise ValueError("The lengths of and b must match.")

    combined_list = []
    for k in range(number_elements):
        combined_list.append(
            sum(
                [list_1[i] * list_2[k - i % number_elements] for i in range(number_elements)]
            )
        )

    if eliminate_doubling:
        combined_list = [1 if x > 0 else 0 for x in combined_list]
    return combined_list


def get_interval_vector(
        set_of_integers: list,
        return_counts: bool = True
) -> tuple:
    """
    Generates the interval vector within a single set:
    the complete set of intervals between items within that set.

    Args:
    set_of_integers (list): A list of integers.
    return_counts (bool): If True, returns a tuple with the counts for each integer from 0 to 6.
        (This corresponds to the standard representation in music theory.)
        Otherwise, returns a list of integers.

    Returns:
    list or tuple: A list of integers or a tuple with the counts for each integer.

    >>> test_list = [1, 3, 4, 6]
    >>> get_interval_vector(test_list, return_counts=False)
    (2, 3, 5, 1, 3, 2)

    >>> get_interval_vector(test_list, return_counts=True)  # default
    (0, 1, 2, 2, 0, 1, 0)

    """
    differences = []

    for i in range(len(set_of_integers)):
        for j in range(i + 1, len(set_of_integers)):
            diff = abs(set_of_integers[j] - set_of_integers[i])
            differences.append(diff)

    if return_counts:
        differences = values_to_counts(differences)

    return tuple(differences)


def interval_function(
        start_set: list,
        end_set: list,
        return_counts: bool = True
) -> tuple:
    """
    Generates all intervals between two sets of integers and returns the difference between the two values.
    The interval _function_ was introduced to music theory by Lewin, 2001


    Args:
        start_set (list): A list of integers representing the start of the intervals.
        end_set (list): A list of integers representing the end of the intervals.
        return_counts (bool). Re-organise the list as in the interval vector.

    Returns:
    list: A list of integers, where each integer represents the difference between the start and end of an interval.

    >>> start_set = [1, 2, 3]
    >>> end_set = [3, 4, 5]
    >>> interval_function(start_set, end_set, return_counts=False)
    (2, 3, 4, 1, 2, 3, 0, 1, 2)

    >>> interval_function(start_set, end_set, return_counts=True)  # default
    (1, 2, 3, 2, 1, 0, 0)

    """
    differences = []
    for start in start_set:
        for end in end_set:
            if start <= end:  # Ensure start is less than or equal to end
                differences.append(end - start)

    if return_counts:
        differences = values_to_counts(differences)

    return tuple(differences)


def values_to_counts(
        set_of_integers: list | tuple,
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
        max_val = max(set_of_integers)
    counts = [0] * (max_val + 1)
    for difference in set_of_integers:
        counts[difference] += 1
    return tuple(counts)


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest

    doctest.testmod()
