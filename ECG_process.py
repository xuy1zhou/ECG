# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk
import load_intan_rhd_format


DataInfo = load_intan_rhd_format.read_data(r'D:\ECG\ECG002_221109_172137\info.rhd')
SampleRate = DataInfo['frequency_parameters']['amplifier_sample_rate']
StartPoint = int(1 * 60 * SampleRate)
EndPoint = int(4 * 60 * SampleRate)

with open(r'D:\ECG\ECG002_221109_172137\amplifier.dat', 'rb') as f:
    ECGfileData = np.fromfile(f, dtype=np.int16)
ECGfileData = ECGfileData[StartPoint:EndPoint] * 0.195
nkECGdataPeaks = nk.signal_findpeaks(ECGfileData, height_min=600)
nkFixedPeaks = nk.signal_fixpeaks(nkECGdataPeaks, sampling_rate=SampleRate)
nkHRV = nk.hrv_time(nkFixedPeaks[1], sampling_rate=SampleRate)
nkHR = np.asarray(nk.ecg_rate(nkFixedPeaks[1], sampling_rate=SampleRate), dtype=np.int16)
