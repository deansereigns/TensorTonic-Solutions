import numpy as np
import math
def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation)."""
    # YOUR CODE HERE
    # print(image.shape)
    n = image.shape[0]
    shape=(n,55,55,96)
    result = np.zeros(shape)
    return result
    pass