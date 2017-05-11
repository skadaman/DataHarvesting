# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:16:55 2017

@author: S.Kadamany
"""

import datetime
from urllib.request import urlretrieve
import pandas as pd
SPPLink= 'pubftp.spp.org'

date_list=pd.date_range(start='1/29/2014', periods=1185, freq='D').tolist()
for i in date_list:
    day=('0'+str(i.day))[1:]
    month=str(i.month)
    year=str(i.year)         
    post='/Markets/DA/LMP_By_BUS/'+year+'/'+day+'/By_Day/'
    filename='DA-LMP-B-'+year+month+day+'0100'
    path=r'C:\Users\sebastian\py\Py1\Incoming\SPP_Harvest'
    ext=".csv"
    downloadfolder=path+filename+ext
    url=SPPLink+post+filename+ext
# this uses urlretrieve(url,'download directory')
    urlretrieve(url,downloadfolder)