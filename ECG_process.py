# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk
import intan_rhd_format.load_intan_rhd_format


print(read_data(r'D:\ECG\ECG002_221109_172137\info.rhd'))
# with open(r'D:\ECG\ECG002_221109_172137\amplifier.dat', 'rb') as f:
#     ECGfileData = np.fromfile(f, dtype=np.int16)
# ECGfileData = ECGfileData * 0.195
# nkECGdataPeaks = nk.signal_findpeaks(ECGfileData, height_min=600)
# nkHRV = nk.hrv(nkECGdataPeaks, sampling_rate=20000)
# nkHR = nk.ecg_rate(nkECGdataPeaks, sampling_rate=20000)
# print(nkHRV, '\n', nkHR)
