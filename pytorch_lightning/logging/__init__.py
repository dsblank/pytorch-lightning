"""
.. warning:: `logging` package has been renamed to `loggers` since v0.6.1 and will be removed in v0.8.0
"""

import warnings

warnings.warn("`logging` package has been renamed to `loggers` since v0.6.1"
              " and will be removed in v0.8.0", DeprecationWarning)

from pytorch_lightning.loggers import *  # noqa: F403
