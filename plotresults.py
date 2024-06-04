import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json

filePath = "./"
fileName = "result.json"

with open(filePath + fileName) as f:
    res = json.load(f)

borders = np.array(res["Borders"])
prodlayers = np.array(res["ProdLayers"])
y_axis = np.array(res['depth'])
halfwidth = np.array(res['halfwidth'])
sigma_min = np.array(res['sMin'])
sigma_min_back = np.array(res['sMinBack'])

mpl.rc('font', size=18) #controls default text size
mpl.rc('axes', titlesize=30) #fontsize of the title
mpl.rc('axes', labelsize=26) #fontsize of the x and y labels
mpl.rc('xtick', labelsize=26) #fontsize of the x tick labels
mpl.rc('ytick', labelsize=26) #fontsize of the y tick labels
mpl.rc('legend', fontsize=24) #fontsize of the legend

lw = 2      # linewidth
lw_tip = 3  # dotted line thickness
alpha = 0.5 # transparency for productive layers

depthlim = [borders[1] - 10.0, borders[4] + 10.0]
vlim = [-0.1, 1.1*max(halfwidth)]
sMin_min = min(sigma_min)
sMin_max = max(sigma_min)
sMinBack_min = min(sigma_min_back)
sMinBack_max = max(sigma_min_back)
sMinlim = [1.1*min(sMin_min, sMinBack_min), 0.9*max(sMin_max, sMinBack_max)]

cols = 2
fig, ax = plt.subplots(nrows=1, ncols=cols, figsize=(15, 12))

ax[0].set_xlabel('Полураскрытие [мм]')
ax[0].set_ylabel('Глубина [м]')
ax[0].set_xlim(vlim)
ax[0].set_ylim(depthlim)
ax[0].invert_yaxis()

ax[1].set_xlabel('Напряжение [МПа]')
ax[1].set_ylabel('Глубина [м]')
ax[1].set_xlim(sMinlim)
ax[1].set_ylim(depthlim)
ax[1].invert_yaxis()

hex_code = "#308014"

redd = int(hex_code[1:3], 16)/255
greenn = int(hex_code[3:5], 16)/255
bluee = int(hex_code[5:7], 16)/255

[ax[0].plot(vlim, [brd, brd], \
    color='grey', lw=lw_tip, ls='--') for brd in borders]
[ax[0].fill_between(vlim, borders[i], borders[i + 1], color='yellow', \
    hatch='///', edgecolor='black',alpha=alpha) for i, k in enumerate(prodlayers) if k == 1]
[ax[0].fill_between(vlim, borders[i], borders[i + 1], color=(redd,greenn,bluee), \
    hatch='\\/...', alpha=alpha) for i, k in enumerate(prodlayers) if k != 1]
ax[0].plot(halfwidth, y_axis, color='b', lw=lw, label='Полураскрытие')

[ax[1].plot(sMinlim, [brd, brd], \
    color='grey', lw=lw_tip, ls='--') for brd in borders]
[ax[1].fill_between(sMinlim, borders[i], borders[i + 1], color='yellow', \
    hatch='///', edgecolor='black',alpha=alpha) for i, k in enumerate(prodlayers) if k == 1]
[ax[1].fill_between(sMinlim, borders[i], borders[i + 1], color=(redd,greenn,bluee), \
    hatch='\\/...', alpha=alpha) for i, k in enumerate(prodlayers) if k != 1]
ax[1].plot(sigma_min_back, y_axis, color='red', lw=lw, label='sMin + sBack')
ax[1].plot(sigma_min, y_axis, color='orange', lw=lw, label='sMin', ls='--')


[ax[i].grid() for i in range(cols)]
[ax[i].legend() for i in range(cols)]
fig.tight_layout()
plt.show()