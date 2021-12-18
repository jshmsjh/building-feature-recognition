# building-feature-recognition

In this repository, we accomplished building feature recognition using traditional/dl-assisted computer vision method. The Chinese version of the README is here. And the report of our project(in Chinese) is in the  `report` folder.

## Results

**number of floors**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 5               | 6     | 6                |
| net  | 5               | 6     | 6                |

**number of windows**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 60              | 87    | 44               |
| net  | 60              | 100   | 44               |

**size of windows**

|      | Business school | dorm5       | network building |
| ---- | --------------- | ----------- | ---------------- |
| ours | L6.0m-W1.9m     | L3.2m-W1.9m | L2.6m-W1.9m      |
| net  | L4.7m-W2.1m     | L3.4m-W1.7m | L2.6m-W2.3m      |

**area of windows($m^2$)**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 12              | 6     | 5                |
| net  | 9.9             | 5.9   | 5.9              |

**max length($m$)**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 120             | 35    | 40               |
| net  | 126             | 36.7  | 45.7             |

**max width($m$)**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 60              | 15    | 18               |
| net  | 69.7            | 16.3  | 17.9             |

**max height($m$)**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 31              | 22    | 19               |
| net  | 26.2            | 21.1  | 24               |

Floor area($m^2$)

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 7600            | 1800  | 700              |
| net  | 7630            | 1599  | 743              |

**volume($m^3$)**

|      | Business school | dorm5 | network building |
| ---- | --------------- | ----- | ---------------- |
| ours | 23.6            | 3.96  | 1.47             |
| net  | 19.9            | 3.37  | 1.78             |

## Using the code

To use our code, please first clone this repository and install the `cv2`, `numpy`, `matplotlib` package.

### Reproduction

`side_main.py` process pictures taken horizontally and count floor numbers as well as their relative proportion.

`top_main.py` process pictures taken by a drone from the top of the building.

`window_main.py` process pictures taken horizontally and count window numbers as well as their relative proportion.

Simply click the 'run' icon when opening the three files and you will see the results. Note that threshold tuning might be needed, please refer to our report for more details.

The demo pictures and the results are in the `demo` folder.

### Test your own picture

Please note that the computer vision methods are sensitive to the quality of the picture.

To test your own picture, you may simply replace the picture name in the code. If the default thresholds don't work well, just replace it with a few tests.

