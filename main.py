# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

with open(r'C:\Users\xyz\Desktop\新建文件1.csv', 'r', encoding='utf-8') as f:
    raw_data = np.loadtxt(f, delimiter=',', skiprows=2, dtype=str)
    str_data = np.transpose(raw_data)[:2]
    data = str_data.astype(float)
    # data = np.asarray(str_data, dtype=float)
    # for i in range(len(str_data)):
    #     for j in range(len(str_data[i])):
    # float(str_data[:, :])
    # print(str_data)
    X = data[0]
    Y = data[1]
    plt.plot(X, Y)
    plt.show()
