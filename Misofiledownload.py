
"""
Created on Wed May 10 21:16:55 2017
@author: S.Kadamany
"""


import urllib 
import pandas as pd

date_start='1/3/2018'
date_end='1/4/2018'
extension='.xls'
url_head=  'https://docs.misoenergy.org/marketreports/'
url_tail='_da_pr'
downloadloc=r'\\ascendanalytics.com\users\sxk94\python'
date_list=pd.date_range(start=date_start, end=date_end, freq='D').strftime('%Y-%m-%d')
dates=[d.replace('-','',) for d in date_list]
for i in dates:
    fullurl=url_head+str(i)+url_tail+extension
    file= downloadloc+"\MiSO_DA_"+i+extension
    urllib.request.urlretrieve(fullurl,file)
