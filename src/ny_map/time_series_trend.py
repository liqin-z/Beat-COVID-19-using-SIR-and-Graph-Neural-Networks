import csv
import matplotlib.pyplot as plt
import datetime
import numpy as np

plt.style.use('ggplot')

age_data = './coronavirus-data-master/archive/case-hosp-death.csv'
txt = []

with open(age_data, 'r', newline='') as file:
    reader = csv.reader(file)
    for line in reader:
        txt.append(line)

header = txt[0]
dates = []
for i in txt[1::]:
    dates.append(i[0])

fig,axs = plt.subplots(2,1,figsize=(12,9))
cii = 0
for jj in range(1,len(txt[0])):
    vals = []
    for ii in range(0,len(txt[1:])):
        val = (txt[1:])[ii][jj]
        if val=='':
            val = np.nan
        else:
            val = float(val)
        vals.append(val)
        
    axs[0].scatter(dates,vals,label=txt[0][jj].replace('_',' '),color=plt.cm.tab10(cii),linewidth=3.0)
    axs[1].plot(dates,np.nancumsum(vals),label=(txt[0][jj]).replace('_',' ').replace('NEW','TOTAL'),
                                                                linewidth=6.0,color=plt.cm.tab10(cii),linestyle=':')
    cii+=1
    
axs[0].legend(title='New Case Counts')
axs[0].tick_params(axis='x', rotation=15)
axs[0].set_ylabel('New Count',fontsize=16)
axs[0].set_yscale('log')
axs[0].tick_params('both',labelsize=16)
axs[0].set_xticklabels([])
axs[1].legend(title='Total Case Counts')
axs[1].set_yscale('log')
axs[1].tick_params(axis='x', rotation=15)
axs[1].set_xlabel('Date [Year-Month-Day]',fontsize=18,labelpad=10)
axs[1].set_ylabel('Total Count',fontsize=18)
axs[1].tick_params('both',labelsize=16)
fig.subplots_adjust(hspace=0.1)
fig.savefig(header[0]+'_in_NYC_COVID19.png',dpi=300,facecolor='#FCFCFC')
plt.show()
