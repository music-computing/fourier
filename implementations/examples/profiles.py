# coding: utf-8
"""
A small selection of patterns that are referenced in the paper and may be useful for testing.
Source: [redacted]
"""

from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

__author__ = "Anonymous for blind submission"


# ------------------------------------------------------------------------

scales = {
    "major": (1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1)
}

chords = {
    "major": (1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0)
}

rhythms = {
    "bossa_nova_5_in_16": (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0),
    "cinquillo_augmented": (1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    "son_clave": (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    "tresillo": (1, 0, 0, 1, 0, 0, 1, 0)  # cf prototype_3_8_x3
}


prototypes = {
    "3_8_x1": (1, 0, 0, 0, 0, 0, 1, 1),
    "3_8_x2": (1, 0, 0, 1, 1, 0, 0, 0),
    "3_8_x3": (1, 0, 0, 1, 0, 0, 1, 0),  # cf tresillo
    "3_8_x4": (1, 0, 0, 0, 1, 0, 1, 0)
}


# ------------------------------------------------------------------------
