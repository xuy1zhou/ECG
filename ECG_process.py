# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk
import load_intan_rhd_format
import pandas as pd


DataInfo = load_intan_rhd_format.read_data(r'D:\ECG\ECG002_221109_210522\info.rhd')
SampleRate = DataInfo['frequency_parameters']['amplifier_sample_rate']
StartPoint = int(0 * 60 * SampleRate)
EndPoint = int(4 * 60 * SampleRate)

with open(r'D:\ECG\ECG002_221109_210522\amplifier.dat', 'rb') as f:
    ECGfileData = np.fromfile(f, dtype=np.int16)
ECGfileData = ECGfileData[StartPoint:EndPoint] * 0.195
nkECGdataPeaks = nk.signal_findpeaks(ECGfileData, height_min=1000)
nkFixedPeaks = nk.signal_fixpeaks(peaks=nkECGdataPeaks, sampling_rate=SampleRate, relative_interval_min=-0.2,
                                  relative_interval_max=0.2, method='neurokit')
nkHRV = nk.hrv_time(nkFixedPeaks, sampling_rate=SampleRate)
nkHR = np.asarray(nk.ecg_rate(nkFixedPeaks, sampling_rate=SampleRate), dtype=np.int16)
pdHRV = pd.DataFrame(nkHRV)
pdHR = pd.DataFrame(nkHR)
pdHRV.to_csv('HRV.csv', index=False)
pdHR.to_csv('HR.csv', index=False, header=False)
