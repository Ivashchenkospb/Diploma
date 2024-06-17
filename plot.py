import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import time


mpl.rc('font', size=18) #controls default text size
mpl.rc('axes', titlesize=30) #fontsize of the title
mpl.rc('axes', labelsize=26) #fontsize of the x and y labels
mpl.rc('xtick', labelsize=26) #fontsize of the x tick labels
mpl.rc('ytick', labelsize=26) #fontsize of the y tick labels
mpl.rc('legend', fontsize=24) #fontsize of the legend


class DynamicPlot():

    def __init__(self):
        self.filePath = "./Results1/"
        self.lw = 2      # linewidth
        self.lw_tip = 3  # dotted line thickness
        self.alpha = 0.5 # transparency for productive layers
        self.hex_code = "#308014"
        self.redd = int(self.hex_code[1:3], 16)/255
        self.greenn = int(self.hex_code[3:5], 16)/255
        self.bluee = int(self.hex_code[5:7], 16)/255

        self.onLaunch

    
    def onLaunch(self):
        cols = 3
        self.fig, self.ax = plt.subplots(nrows=1, ncols=cols, figsize=(15, 12))
        self.ax[0].set_xlabel('Раскрытие, [мм]')
        self.ax[0].set_ylabel('Глубина [м]')
        self.ax[0].invert_yaxis()

        self.ax[1].set_xlabel('Поровое давление [МПа]')
        self.ax[1].set_ylabel('Глубина [м]')
        self.ax[1].invert_yaxis()

        self.ax[2].set_xlabel('МПа')
        self.ax[2].set_ylabel('Глубина [м]')
        self.ax[2].invert_yaxis()

        depthlim = [2640.0, 2685.0]
        vlim = [-0.1, 2]
        presLim = [24.0, 35.0]
        sMinlim = [35.0, 45.0]
        borders = [2.350000e+03, 2.650000e+03, 2.660000e+03, 2.665000e+03, 2.675000e+03, 
		           2.950000e+03]
        prodlayers = [0, 1, 0, 1, 0]

        self.ax[0].set_xlim(vlim)
        self.ax[0].set_ylim(depthlim)

        self.ax[1].set_xlim(presLim)
        self.ax[1].set_ylim(depthlim)

        self.ax[2].set_xlim(sMinlim)
        self.ax[2].set_ylim(depthlim)

        [self.ax[0].plot(vlim, [brd, brd], \
            color='grey', lw=self.lw_tip, ls='--') for brd in borders]
        [self.ax[0].fill_between(vlim, borders[i], borders[i + 1], color='yellow', \
            hatch='///', edgecolor='black',alpha=self.alpha) for i, k in enumerate(prodlayers) if k == 1]
        [self.ax[0].fill_between(vlim, borders[i], borders[i + 1], color=(self.redd,self.greenn,self.bluee), \
            hatch='\\/...', alpha=self.alpha) for i, k in enumerate(prodlayers) if k != 1]
        
        [self.ax[1].plot(presLim, [brd, brd], \
            color='grey', lw=self.lw_tip, ls='--') for brd in borders]
        [self.ax[1].fill_between(presLim, borders[i], borders[i + 1], color='yellow', \
            hatch='///', edgecolor='black',alpha=self.alpha) for i, k in enumerate(prodlayers) if k == 1]
        [self.ax[1].fill_between(presLim, borders[i], borders[i + 1], color=(self.redd,self.greenn,self.bluee), \
            hatch='\\/...', alpha=self.alpha) for i, k in enumerate(prodlayers) if k != 1]
        
        [self.ax[2].plot(sMinlim, [brd, brd], \
            color='grey', lw=self.lw_tip, ls='--') for brd in borders]
        [self.ax[2].fill_between(sMinlim, borders[i], borders[i + 1], color='yellow', \
            hatch='///', edgecolor='black',alpha=self.alpha) for i, k in enumerate(prodlayers) if k == 1]
        [self.ax[2].fill_between(sMinlim, borders[i], borders[i + 1], color=(self.redd,self.greenn,self.bluee), \
            hatch='\\/...', alpha=self.alpha) for i, k in enumerate(prodlayers) if k != 1]

        self.line0, = self.ax[0].plot([], [], 'o')
        self.line1, = self.ax[1].plot([], [], 'o')
        self.line2, = self.ax[2].plot([], [], 'o')

        [self.ax[i].grid() for i in range(cols)]

    def onRunning(self, )


d = DynamicPlot()