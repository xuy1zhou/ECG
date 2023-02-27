# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from nptdms import TdmsFile
import numpy as np
import pandas as pd
import neurokit2 as nk


def cut_minus(array):
    filter_arr = []
    for i in array:
        if i < 0:
            filter_arr.append(False)
        else:
            filter_arr.append(True)
    return array[filter_arr]


with TdmsFile.open(r'D:\ECG\221226\dobutamin.tdms') as tdms_file:
    for group in tdms_file.groups():
        group_name = group.name
    for channel in group.channels():
        channel_name = channel.name
    channel = tdms_file[group_name][channel_name]
    npECGdata = np.array(channel)
npECGdata = cut_minus(npECGdata)
SampleRate = 1 / channel.properties['wf_increment']
nkECGdataPeaks = nk.signal_findpeaks(npECGdata[30000:40000], height_min=0.06)
nkFixedPeaks = nk.signal_fixpeaks(peaks=nkECGdataPeaks, sampling_rate=SampleRate, relative_interval_min=-0.5,
                                  relative_interval_max=0.6, method='neurokit')
nkHRV = nk.hrv_time(nkECGdataPeaks, sampling_rate=SampleRate)
nkHR = np.asarray(nk.ecg_rate(nkECGdataPeaks, sampling_rate=SampleRate), dtype=np.int16)
# pdHRV = pd.DataFrame(nkHRV)
# pdHR = pd.DataFrame(nkHR)
# pdHRV.to_csv('neostigmine_HRV.csv', index=False)
# pdHR.to_csv('neostigmine_HR.csv', index=False, header=False)
# print(nkHR)
# print(nkHRV)

nk.events_plot([nkECGdataPeaks["Onsets"], nkECGdataPeaks["Peaks"]], npECGdata[30000:40000])
plt.show()

# signals = pd.DataFrame({"ECG_Raw" : npECGdata[0:3000],
#                         "ECG_NeuroKit" : nk.ecg_clean(npECGdata[0:3000], sampling_rate=500, method="neurokit"),
#                         "ECG_BioSPPy" : nk.ecg_clean(npECGdata, sampling_rate=500, method="biosppy"),
#                         "ECG_PanTompkins" : nk.ecg_clean(npECGdata, sampling_rate=500, method="pantompkins1985"),
#                         "ECG_Hamilton" : nk.ecg_clean(npECGdata, sampling_rate=500, method="hamilton2002"),
#                         "ECG_Elgendi" : nk.ecg_clean(npECGdata[0:3000], sampling_rate=500, method="elgendi2010"),
#                         "ECG_EngZeeMod" : nk.ecg_clean(npECGdata, sampling_rate=500, method="engzeemod2012")})



