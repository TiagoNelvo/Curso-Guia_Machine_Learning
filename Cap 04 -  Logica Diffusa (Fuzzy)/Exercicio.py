import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import Fuzzy
from Fuzzy import * 







gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)
gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10, 3)
gorjeta['alta'] = fuzz.pimf(gorjeta.universe, 10, 20, 20, 21)
gorjeta.view()