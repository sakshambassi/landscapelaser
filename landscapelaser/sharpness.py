"""
This module implements a sharpness measure of loss-landscapes

Author: Saksham Bassi
"""
import numpy as np

from landscapelaser.sharpness_util import (
    calculate_mean_loss,
    calculate_mean_sharpness
)

class LandscapeLaser:
    """
    Class of LandscapeLaser calculation
    """
    def __init__(self) -> None:
        pass

    def calculate(self, values = None, path = None, center_percent: int = 30):
        """returns (sharpness, mean) of loss landscape

        Args:
            values (np.array): array of loss values
            path (str): absolute path of loss values
            center_percent (int): dimension of array of centers considered in the form
            of percentage of dimension of total points in the loss_values array
        """
        if (values is None and path is None) or (values is not None and path is not None):
            raise ValueError('Can calculate sharpness only by array or path')
        if path:
            try:
                values = np.load(path)
            except FileNotFoundError:
                raise Exception("File not found.")
        return calculate_mean_sharpness(values, center_percent), calculate_mean_loss(values)