import numpy as np


class Model:

    def __init__(self, modelWeights: np.ndarray):
        self.weights = modelWeights

    def predict(self, data: np.ndarray) -> float:
        return np.dot(data, self.weights).sum()