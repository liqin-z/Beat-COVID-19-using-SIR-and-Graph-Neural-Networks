import numpy as np
import matplotlib.pyplot as plt
import requests,datetime,os
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from osgeo import ogr

plt.style.use('ggplot')

def basemapper():
    fig,ax = plt.subplots(figsize=(14,10))
    m = Basemap(llcrnrlon=bbox[0],llcrnrlat=bbox[1],urcrnrlon=bbox[2],
               urcrnrlat=bbox[3],resolution='h', projection='cyl')
    shpe = m.readshapefile(shapefile.replace('.shp',''),'curr_shapefile')
    m.drawmapboundary(fill_color='#bdd5d5')
    m.fillcontinents(color=plt.cm.tab20c(19))
    m.drawcounties(color='k',zorder=999)
    parallels = np.linspace(bbox[1],bbox[3],5)
    m.drawparallels(parallels,labels=[True,False,False,False],fontsize=12,linewidth=0.25)
    meridians = np.linspace(bbox[0],bbox[2],5)
    m.drawmeridians(meridians,labels=[False,False,False,True],fontsize=12,linewidth=0.25)
    return fig,ax,m

zip_data = './coronavirus-data-master/archive/tests-by-zcta.csv'
txt = []

shapefile_folder = './ZIP_CODE_040114/'
shapefile = shapefile_folder+os.listdir(shapefile_folder)[0].split('_correct_CRS')[0]+'_correct_CRS.shp'
drv    = ogr.GetDriverByName('ESRI Shapefile')
ds_in  = drv.Open(shapefile,0)
lyr_in = ds_in.GetLayer()
shp = lyr_in.GetExtent()
zoom = 0.01
bbox = [shp[0]-zoom,shp[2]-zoom,shp[1]+zoom,shp[3]+zoom]
fig,ax,m = basemapper()

fig.canvas.draw()
transf = ax.transData.inverted()
shape_areas = [ii['AREA'] for ii in m.curr_shapefile_info]

header = txt[0]

zipcodes = [data_row[0] for data_row in txt[3:]]
zipcode_pos = [float(data_row[1]) for data_row in txt[3:]]
zipcode_tot = [float(data_row[2]) for data_row in txt[3:]]
zipcode_perc = [float(data_row[3]) for data_row in txt[3:]]

data_array = [zipcode_pos,zipcode_tot,zipcode_perc]
data_titles = ['Positive Cases','Total Tested','Percent Testing Positive']
data_indx = 2
data_range = [np.min(data_array[data_indx]),np.max(data_array[data_indx])]

cmap_sel = plt.cm.BuPu
txt_color = 'w'
shape_edge_colors = 'k'
NA_color = 'w'

match_array,patches,patches_NA,color_array,txt_array = [],[],[],[],[]
for info,shape in zip(m.curr_shapefile_info,m.curr_shapefile):
    if info['POPULATION']==0.0:
        patches_NA.append(Polygon(np.array(shape), True, color=NA_color,label=''))
        continue
    if info['ZIPCODE'] in zipcodes:
        zip_indx = [ii for ii in range(0,len(zipcodes)) if info['ZIPCODE']==zipcodes[ii]][0]
        zip_data = data_array[data_indx][zip_indx]
        color_val = np.interp(zip_data,data_range,[0.0,1.0])
        c_map = cmap_sel(color_val)
        
        if info['ZIPCODE'] in match_array:
            patches.append(Polygon(np.array(shape), True, color=c_map)) 
        else:
            match_array.append(info['ZIPCODE'])
            patches.append(Polygon(np.array(shape), True, color=c_map))
            
            x_pts = [ii[0] for ii in shape]
            y_pts = [ii[1] for ii in shape]

            x_pts_centroid = [np.min(x_pts),np.min(x_pts),np.max(x_pts),np.max(x_pts)]
            y_pts_centroid = [np.min(y_pts),np.max(y_pts),np.min(y_pts),np.max(y_pts)]
            evals,evecs = np.linalg.eigh(np.cov(x_pts,y_pts))
            rot_vec = np.matmul(evecs.T,[x_pts,y_pts])
            angle = (np.arctan(evecs[0][1]/evecs[0][0])*180.0)/np.pi
            angle-=90.0
            if angle<-90.0:
                angle+=180.0
            elif angle>90.0:
                angle-=180.0
            
            if angle<-45.0:
                angle+=90.0
            elif angle>45.0:
                angle-=90.0

            txtbox = ax.text(np.mean(x_pts_centroid),np.mean(y_pts_centroid), info['ZIPCODE'], ha='center',
                              va = 'center',fontsize=np.interp(info['AREA'],np.sort(shape_areas)[::int(len(np.sort(shape_areas))/4.0)],
                                                               [1.0,2.0,4.0,5.0]),
                             rotation=angle, rotation_mode='anchor',color=txt_color,bbox=dict(boxstyle="round",ec=c_map,fc=c_map))

            trans_bounds = (txtbox.get_window_extent(renderer = fig.canvas.renderer)).transformed(transf)
            for tbox in txt_array:
                tbounds = (tbox.get_window_extent(renderer = fig.canvas.renderer)).transformed(transf)
                loops = 0
                while trans_bounds.contains(tbounds.x0,tbounds.y0) or trans_bounds.contains(tbounds.x1,tbounds.y1) or\
                        tbounds.contains(trans_bounds.x0,trans_bounds.y0) or tbounds.contains(trans_bounds.x1,trans_bounds.y1) or\
                trans_bounds.contains(tbounds.x0+((tbounds.x0+tbounds.x1)/2.0),tbounds.y0+((tbounds.y0+tbounds.y1)/2.0)) or \
                trans_bounds.contains(tbounds.x0-((tbounds.x0+tbounds.x1)/2.0),tbounds.y0-((tbounds.y0+tbounds.y1)/2.0)) or \
                trans_bounds.contains(tbounds.x0+((tbounds.x0+tbounds.x1)/2.0),tbounds.y0-((tbounds.y0+tbounds.y1)/2.0)) or\
                trans_bounds.contains(tbounds.x0-((tbounds.x0+tbounds.x1)/2.0),tbounds.y0+((tbounds.y0+tbounds.y1)/2.0)):
                    txtbox.set_size(txtbox.get_size()-1.0)
                    tbox.set_size(tbox.get_size()-1.0)
                    trans_bounds = (txtbox.get_window_extent(renderer = fig.canvas.renderer)).transformed(transf)
                    tbounds = (tbox.get_window_extent(renderer = fig.canvas.renderer)).transformed(transf)
                    loops+=1
                    if loops>10:
                        break
            
            txt_array.append(txtbox)
            if len(txt_array) % 10 == 0:
                print('{0:2.0f} % Finished'.format(100.0*(len(txt_array)/len(zipcodes))))
            
    else:
        patches_NA.append(Polygon(np.array(shape), True, color=NA_color,label=''))

pc = PatchCollection(patches, match_original=True, edgecolor=shape_edge_colors, linewidths=1., zorder=2,cmap=cmap_sel)
pc_NA = PatchCollection(patches_NA, match_original=True, edgecolor=shape_edge_colors, linewidths=1., zorder=2)
ax.add_collection(pc)
ax.add_collection(pc_NA)
    
pc.set_clim(data_range)
cb = plt.colorbar(pc,shrink=0.75)
cb.set_label(data_titles[data_indx],fontsize=18,labelpad=10)

leg1 = ax.legend(handles=[patches_NA[-1]],title='No Data',
                 fontsize=16,framealpha=0.95,loc='upper left')

txtbox = ax.text(0.0, 0.025, 'Computed on '+datetime.datetime.now().strftime('%b %d, %Y %H:%M'), transform=ax.transAxes, fontsize=14,
        verticalalignment='center', bbox=dict(boxstyle='round', facecolor='w',alpha=0.5)) 
txtbox.set_x(1.1-(txtbox.figure.bbox.bounds[2]-(txtbox.clipbox.bounds[2]-txtbox.clipbox.bounds[0]))/txtbox.figure.bbox.bounds[2])
plt.show()
