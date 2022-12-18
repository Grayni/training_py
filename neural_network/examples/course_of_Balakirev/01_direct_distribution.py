import numpy as np


def act(val):
    return 0 if val < 0.5 else 1


def go(house, rock, attr):
    # Input layer(signal) vector
    x = np.array([house, rock, attr])  # 3x1

    wj1 = [0.3, 0.3, 0]
    wj2 = [0.4, -0.5, 1]

    weight1 = np.array([wj1,
                        wj2])  # array 2x3
    weight2 = np.array([-1, 1])  # array 2x1

    sum_hidden = np.dot(weight1, x)  # Σ(w*x)
    print('The values of the sums on the neurons of the hidden layer:', sum_hidden)

    out_hidden = np.array([act(x) for x in sum_hidden])
    print('The values on outputs the neurons of the hidden layer:', out_hidden)

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print('Outputs values of neurons:', y)

    return y


house = 0.3
rock = 0.4
attr = 0.6

result = go(house, rock, attr)

if result:
    print('Successful')
else:
    print('Denied')
