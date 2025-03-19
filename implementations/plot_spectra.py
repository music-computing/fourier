# coding: utf-8
"""
Basic implementation for computing Fourier transform and plotting the result.
Source: [redacted]
"""

from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

__author__ = "Anonymous for blind submission"

from implementations.examples.profiles import scales

THIS_DIR = Path(__file__).parent


# ------------------------------------------------------------------------

def compute_and_plot(
    time_array: np.array,
    frequency_arrays: list[np.array],
    hide_symmetry: bool = True,
    write_not_show: bool = True,
    write_path: str | Path = THIS_DIR / "plots" / "dft_example.pdf",
    labels: list[str] = None,
    colors: list[str] = None
) -> None:
    """
    Calculate and plot the Fourier transform of multiple data sets.

    :param time_array: The time points (created outside this function).
    :param frequency_arrays: A list of 'signal' arrays which can be as simple as binary profiles.
    :param hide_symmetry: Return half the values from index 1 to N/2 (removing the symmetry).
    :param write_not_show: Chose between saving and showing.
    :param write_path: If writing/saving, chose a file location and name.
    :param labels: A list of labels for each data set.
    :param colors: A list of colors for each data set.
    :return: None (plot)
    """
    size = len(time_array)
    for frequency_array in frequency_arrays:
        if len(frequency_array)!= size:
            raise ValueError(
                f"The lengths of the `time_array` (currently {time_array})"
                f"and `frequency_array` (currently {frequency_array}) must match (same sample rate)."
            )

    plt.figure(figsize=(10, 6))
    for i, frequency_array in enumerate(frequency_arrays):
        magnitudes = np.absolute(np.fft.fft(frequency_array))

        if hide_symmetry:
            half_length = round(size / 2) + 1
            plot_time_array = time_array[1:half_length]
            plot_magnitudes = magnitudes[1:half_length]
        else:
            plot_time_array = time_array
            plot_magnitudes = magnitudes

        label = labels[i] if labels else f"Example {i+1}"
        color = colors[i] if colors else plt.cm.tab20(i)
        plt.plot(
            plot_time_array,
            plot_magnitudes,
            linestyle='-',
            marker='x',
            color=color,
            label=label
        )

    axis_label_size = 14
    plt.ylabel('FFT Amplitude $|X(freq)|$', fontsize=axis_label_size)
    plt.xlabel('Coefficient', fontsize=axis_label_size)

    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()

    if write_not_show:
        plt.savefig(write_path)
    else:
        plt.show()


def run_one(
        profile: list | None = None
) -> None:
    """
    Prepared and plot FT for any list.
    Defaults provide a demo of the `maj_scale` profile (examples.profiles.maj_scale)
    omitting symmetry.
    """
    if not profile:
        from examples.profiles import scales
        profile = scales["major"]
    frequency_array = np.array(profile)
    time_array = np.array(range(len(profile)))
    compute_and_plot(
        time_array,
        [frequency_array],
        hide_symmetry=False,
        labels=["major scale"],
        write_path= THIS_DIR / "plots" / "dft_example.pdf"
    )


def run_one_set(
        profiles: list | None = None
):
    """
    Prepared and plot FT for any combination of lists as long as they have the same length.
    Defaults provide a demo of examples.profiles.{cinquillo_augmented | son_clave | bossa_nova_5_in_16}
    """
    if not profiles:
        from examples.profiles import rhythms
        rhythm_names = ["cinquillo_augmented", "son_clave", "bossa_nova_5_in_16"]
        rhythm_labels = [x.replace("_", " ") for x in rhythm_names]
        profiles = [rhythms[label] for label in rhythm_names]

    shared_len = len(profiles[0])

    for profile in profiles[1:]:
        if len(profile) != shared_len:
            raise ValueError("The profiles must all be of the same length.")

    time_array = np.array(range(shared_len))

    compute_and_plot(
        time_array,
        profiles,
        hide_symmetry=True,
        labels=rhythm_labels,
        write_path=THIS_DIR / "plots" / "rhythm_comparison.pdf"
    )


# ------------------------------------------------------------------------

if __name__ == "__main__":
    run_one()
