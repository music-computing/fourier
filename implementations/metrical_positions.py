# coding: utf-8
"""
Working with an example data.
Implementation for Fourier exercises.
Source: [redacted]
"""

from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pandas as pd


__author__ = "Anonymous for blind submission"


# ------------------------------------------------------------------------


THIS_DIR = Path(__file__).parent


def get_beethoven_example(file_name: str = 'Beethoven_Op057-01_FG58.csv'):
    """
    This repo provides a single file from the BPSD dataset
    This function retrieves that data
    and returns a list of start times.
    """

    notes = pd.read_csv(THIS_DIR / "example_data" / file_name, sep=";")
    return [row.start_meas for _, row in notes.iterrows()]


def events_by_position_to_onsets(
        pattern: list = [4, 1, 2, 1, 3, 1, 2, 1]
) -> list:
    """
    Convert a position-oriented list to one of onset times.

    :param pattern: The pattern of event uses, each measure, with equal spacing.

    >>> events_by_position_to_onsets()
    [0.0, 0.0, 0.0, 0.0, 0.125, 0.25, 0.25, 0.375, 0.5, 0.5, 0.5, 0.625, 0.75, 0.75, 0.875]

    """
    pattern_fractions = []
    for index in range(len(pattern)):
        num = pattern[index]
        for n in range(num):
            pattern_fractions.append(index  / len(pattern))

    return pattern_fractions


def make_fake_starts(
        measures: int = 40,
        pattern: list = [4, 1, 2, 1, 3, 1, 2, 1]
) -> np.array:
    """
    Complementing the real example, this fuctions serves to
    create a simple, synthetic example of start time data for experimentation.

    :param measures: The number of measures (repetitions)
    :param pattern: The patter of event uses, each measure. See `events_by_position_to_onsets`.

    The defaults set up a [4, 1, 2, 1, 3, 1, 2, 1] pattern 40 times starting at a measure numbered 1.
    With 15 events per measure for 40 measures, this makes for 60 event positions in total
    of which the first four events are at measure 1, the 5th is at 1.125, ..., and the last is 40.875.
    (so finishing at the end of measure 41).

    >>> fs = make_fake_starts()
    >>> len(fs)
    600

    >>> fs[:5]
    array([1.   , 1.   , 1.   , 1.   , 1.125])

    >>> fs[-1]
    40.875

    """

    onsets_by_bar = np.array(events_by_position_to_onsets(pattern))
    all_onsets = np.array([])

    for n in range(measures):
        onsets_by_bar += 1  # count from 1
        all_onsets = np.append(all_onsets, onsets_by_bar)

    return all_onsets


class MetricalData:
    """
    Create and store metrical information from start times in one place.
    :param start_times: All note start times in the data.
    :param bins_per_measure: The number of bins per measure.
        E.g., 1 for a coarse look at density, 24 for every 5th in 12/8 etc.
    """
    def __init__(
            self,
            start_times: list | np.array,
            bins_per_measure: int | None = 24
    ):
        self.start_times = start_times
        if bins_per_measure:
            self.bins_per_measure = bins_per_measure
        # else:
        #     self.bins_per_measure = # TODO import `metrical_LCM` algo. from utils etc.
        self.measure_floor = None
        self.measure_ceiling = None
        self.num_measures = None
        self.num_increments = None
        self.bins_whole_piece = None
        self.measure_positions = [round(x - int(x), 5) for x in start_times]
        self.bins_one_measure = np.arange(0, 1, 1/bins_per_measure)
        self.get_bins()

    def get_bins(self):
        """
        Create equal sized bins for any piece.
        Take the min/max values as the start/end of the bars at the extreme of the piece,
        to make sure every event is counted (with at most a small buffer).
        """
        self.measure_floor = int(np.floor(min(self.start_times)))
        self.measure_ceiling = int(np.ceil(max(self.start_times)))
        self.num_measures = self.measure_ceiling - self.measure_floor
        self.num_increments = self.num_measures * self.bins_per_measure
        self.bins_whole_piece = np.linspace(self.measure_floor, self.measure_ceiling, self.num_increments)

    def histogram_of_starts(
        self,
        measure_not_whole: bool = True,
        grid_lines: int | None = None,
        x_label: str | None = None,
        write_not_show: bool = True,
        write_path: str | Path = THIS_DIR / "histogram_of_starts.pdf"
    ) -> None:
        """
        Create a histogram, plotting the sheer number of events per time increment.

        :param measure_not_whole: If True, aggregate data into one abstract measure.
        :param grid_lines: The number of vertical lines, e.g., to highlight macro-beats.
        :param x_label: Optionally specify an annotation for the x-axis.
        :param write_not_show: Chose between saving and showing.
        :param write_path: If writing/saving, chose a file location and name.
        :return: None (plot)
        """
        if measure_not_whole:
            data = self.measure_positions
            bins_to_use = self.bins_one_measure
            if not x_label:
                x_label = "Fraction of Measure"
        else:
            data = self.start_times
            bins_to_use = self.bins_whole_piece
            if not x_label:
                x_label = "Measure"

        freqs, bins, _ = plt.hist(
            data,
            bins=bins_to_use,
            rwidth=0.9,
            edgecolor='black'
        )
        plt.title(f'Histogram of Note Events, with {self.bins_per_measure} division/s per measure')
        plt.xlabel(x_label)
        plt.ylabel('Frequency')

        if grid_lines:
            x_lin = list(np.linspace(0, 1, grid_lines + 1))
            plt.xticks(x_lin, minor=False, rotation=45)
            plt.grid()

        plt.tight_layout()

        if write_not_show:
            plt.savefig(write_path)
        else:
            plt.show()


def demo_hist(
    real_not_fake: bool = True,
    measure_not_whole: bool = True,
) -> None:

    grid_lines = None

    if real_not_fake:
        data = MetricalData(
            get_beethoven_example(),
            bins_per_measure=24
        )
    else:
        data = MetricalData(
            make_fake_starts(),
            bins_per_measure=8
        )

    if measure_not_whole:
        grid_lines = 4
        x_label = "measure position"
    else:
        x_label = "measure"
    data.histogram_of_starts(
        measure_not_whole = measure_not_whole,
        grid_lines=grid_lines,
        x_label=x_label,
        write_not_show=True,
        write_path= THIS_DIR / "plots" /  f'demo_hist_{x_label.replace(" ", "_")}.pdf'
    )


# ------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()


