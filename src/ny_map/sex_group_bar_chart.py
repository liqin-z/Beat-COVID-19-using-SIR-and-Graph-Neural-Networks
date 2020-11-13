import csv
import matplotlib.pyplot as plt
import datetime
import numpy as np

plt.style.use('ggplot')

age_data = './coronavirus-data-master/archive/boroughs-by-sex.csv'
txt = []

with open(age_data, 'r', newline='') as file:
    reader = csv.reader(file)
    for line in reader:
        txt.append(line)

header = txt[0]

fig,ax = plt.subplots(figsize=(12.5,7))
spacer = -0.25
cii = 0
for plot_indx in range(4,7):
    data_to_plot,x_range = [],[]
    for jj in range(1,len(txt)-1):
        x_range.append(txt[jj][0])
        data_to_plot.append(float(txt[jj][plot_indx]))
    x_plot = np.arange(0,len(x_range))+spacer
    hist = ax.bar(x_plot,data_to_plot,label=header[plot_indx].replace('_',' ').title(),width=0.15,color=plt.cm.Set2(cii))
    spacer+=0.25
    cii+=1

ax.set_xticks(np.arange(0,len(x_range)))
ax.set_xticklabels(x_range)
ax.legend(fontsize=16)
ax.tick_params('both',labelsize=16)
# textbox showing the date the data was processed
txtbox = ax.text(0.0, 0.975, 'Data updated at '+datetime.datetime.now().strftime('%b %d, %Y %H:%M'), transform=ax.transAxes, fontsize=14,
        verticalalignment='center', bbox=dict(boxstyle='round', facecolor='w',alpha=0.5)) 
txtbox.set_x(0.36-(txtbox.figure.bbox.bounds[2]-(txtbox.clipbox.bounds[2]-txtbox.clipbox.bounds[0]))/txtbox.figure.bbox.bounds[2])
fig.savefig(header[0]+'_in_nyc.png',dpi=300,facecolor='#FCFCFC',bbox_inches = 'tight')
plt.show()
