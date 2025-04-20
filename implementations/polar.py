# coding: utf-8
"""
Implementation of polar coordinates for Fourier exercises.
Source: [redacted]
"""

from __future__ import annotations

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

import cmath


__author__ = "Anonymous for blind submission"

THIS_DIR = Path(__file__).parent


# ------------------------------------------------------------------------

def dft_to_polar_with_cmath(X: np.array):
    """
    Convert the DFT (`X`) of a signal to polar coords using the `cmath` module,
    which takes a complex number as input and returns a tuple of the magnitude and phase.
    I.e., take a signal, compute the DFT, and run this ;)

    >>> signal = np.array([1, 2, 3, 4])
    >>> X = np.fft.fft(signal)
    >>> X[0]
    np.complex128(10+0j)

    >>> dft_to_polar_with_cmath(X)[0]
    (10.0, 0.0)

    """
    return [cmath.polar(x) for x in X]


def dft_to_polar_with_numpy(X: np.array):
    """
    Convert a DFT to polar coordinates using np functionality for calculating the
    magnitudes (with `np.abs`) and phase (`np.angle`).
    """
    magnitudes = np.abs(X)
    phases = np.angle(X)
    return list(zip(magnitudes, phases))


def one_cartesian_to_polar(real_part, imaginary_part):
    """
    Converts the real and imaginary parts of a complex number in _Cartesian form_
    to a tuple containing the magnitude and phase of the complex number in _Polar form_
    from scratch.

    In this first demonstration, we take values that make for an integer magnitude (3-4-5 triangle).
    >>> one_cartesian_to_polar(3, 4)
    (5.0, 0.9272952180016122)

    The next demonstration shows a simple phase value due to the 0-values for the complex parts.

    >>> magnitude, phase = one_cartesian_to_polar(3, 0)
    >>> (magnitude, phase)
    (3.0, 0.0)

    """
    magnitude = (real_part**2 + imaginary_part**2)**0.5
    phase = cmath.phase(complex(real_part, imaginary_part))
    return magnitude, phase


def plot_demo(
        complex_num = 3 + 4j,
        write_not_show: bool = False,
        axes_degrees_not_radians: bool = False,
):
    """
    Polar plot of a single complex number on the complex plane.
    Label the axes with either degrees (`axes_degrees_not_radians`=True) or radians.
    """
    magnitude = np.abs(complex_num)
    phase = np.angle(complex_num)

    plt.figure(figsize=(6, 6))
    plt.polar([0, phase], [0, magnitude], marker='o')
    plt.xlim(-np.pi, np.pi)
    plt.ylim(0, max(magnitude * 1.2, 5))
    plt.title(f"Complex Number: {complex_num}")
    plt.grid(True)

    if axes_degrees_not_radians:
        pass
    else:  # Add axis labels (in radians)
        plt.xticks([-np.pi / 2, 0, np.pi / 2, np.pi],
                   ['$-\pi/2$', '0', '$\pi/2$', '+/-$\pi$'])
    if write_not_show:
        plt.savefig(THIS_DIR / "plots" / "polar_demo.pdf")
    else:
        plt.show()


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()
