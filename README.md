# landscapelaser


### Implementation of the [landscapelaser](https://pypi.org/project/landscapelaser/) PyPi package.


Calculates sharpness of the loss landscape of a model. 

## Use
To use the package, do:

```python
from landscapelaser import LandscapeLaser
ll = LandscapeLaser()

import numpy as np
arr = np.random.random((20,20))

sharpness, mean_loss = ll.calculate(values=arr)
print(
    f'The sharpness measure of the loss landscape is `{sharpness}`'
    f' with mean loss over the landscape equal to `{mean_loss}`'
)
```

Here, arr is a 2d numpy array containing the loss values in the landscape. To calculate this, refer to [loss-landscapes package](https://pypi.org/project/loss-landscapes/0.1.1/).


## Installation
The package is available on PyPI. Install using:

`pip install landscapelaser`
