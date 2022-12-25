import numpy as np

from scipy import stats


def calculate_mean_loss(arr: np.array) -> int:
    """ calculates average loss in the loss landscape

    Args:
        arr (np.array): loss values

    Returns:
        int: mean loss over entire loss landscape
    """
    return np.round(
        np.mean(arr),
        4
    )


def calculate_mean_sharpness(loss_arr: np.array, center_percent: int):
    """ calculates mean gradient of diagonals from a center matrix of 3x3

    Args:
        loss_arr (np.array): loss values 
        center_percent (int)
    Returns:
        int: mean sharpness
    """
    steps = [(0, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
             (1, -1), (0, -1), (-1, -1), (-1, 0)]
    cx = loss_arr.shape[0]//2
    cy = loss_arr.shape[1]//2
    total_grad = 0
    for step in steps:
        total_grad += mean_grad_diagonals_from_center(
            arr=loss_arr,
            min_arr=0,
            max_arr=loss_arr.shape[0],
            cx=cx+step[0],
            cy=cy+step[1],
            center_percent=center_percent
        )
    return np.round(total_grad / len(steps), 3)


def generate_points_on_line(min_arr: int, max_arr: int, x: int, y: int, step_x: int, step_y: int):
    """ generates list of points on a line from start point with step size given for both x and y coordinate

    Args:
        min_arr (int): minimum boundary val of arr
        max_arr (int): maximum boundary val of arr
        x (int): x cordinate of start point
        y (int): y cordinate of start point
        step_x (int): step size of x cordinate
        step_y (int): step size of y cordinate

    Returns:
        tuple: x (list) and y (list) points on line
    """
    x_p, y_p = [], []
    while x >= min_arr and y >= min_arr and x < max_arr and y < max_arr:
        x_p.append(x)
        y_p.append(y)
        x += step_x
        y += step_y
    return x_p, y_p


def mean_grad_diagonals_from_center(arr: np.array, min_arr: int, max_arr: int, cx: int, cy: int, center_percent: int):
    """ returns mean gradient of all diagnols from center point

    Args:
        arr (np.array): loss values 
        min_arr (int): minimum boundary val of arr
        max_arr (int): maximum boundary val of arr
        cx (int): x cordinate of center point
        cy (int): y cordinate of center point
        center_percent (int)
    Returns:
        int: mean slope/gradient of all diagonals lines
    """
    steps = [(-1, 1), (0, 1), (1, 1), (1, 0),
             (1, -1), (0, -1), (-1, -1), (-1, 0)]
    grad = 0
    assert arr.shape[0] == arr.shape[1]
    total_steps = int((center_percent * arr.shape[0] / 100) // 2)
    for i in range(total_steps):
        for step in steps:
            step = ((i+1)*step[0], (i+1)*step[1])
            x_p, y_p = generate_points_on_line(
                min_arr=min_arr,
                max_arr=max_arr,
                x=cx,
                y=cy,
                step_x=step[0],
                step_y=step[1]
            )
            z = [arr[x_p[i]][y_p[i]] for i in range(len(x_p))]
            x = np.arange(0, len(x_p))
            slope = stats.linregress(x, np.array(z))[0]
            grad += abs(slope)
    return grad / len(steps)

