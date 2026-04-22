import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is (n, m), weights is (m,) -> return (n,) predictions
        # Round to 5 decimal places
        pass

        res = [0.0] * len(X)
    
        for i, row in enumerate(X):
            for j, col in enumerate(row):
                res[i] += np.dot(X[i][j],weights[j])
            res[i] = np.round(res[i], 5)
        return res

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute mean squared error between predictions and ground truth
        # Round to 5 decimal places
        pass

        res = 0.0

        for i, row in enumerate(model_prediction):
            for j, col in enumerate(row):
                res += (model_prediction[i][j] - ground_truth[i][j]) ** 2

        res = np.round(res * (1/len(model_prediction)), 5)

        return res