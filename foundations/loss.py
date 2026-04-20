import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass

        maximum = max(z)
        summation = 0.0

        for i in range(len(z)):
            z[i] = z[i] - maximum
            summation += math.e**(z[i])

        for i in range(len(z)):
            z[i] = np.round(math.e**(z[i]) / summation, 4)
        
        return z