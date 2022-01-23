import numpy as np

from .mymodel import Model
from .weights.linearModelWeights import linearModelWeights

linearModel = Model(np.array(linearModelWeights))
