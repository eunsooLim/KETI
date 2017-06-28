# -*- coding: utf-8 -*-

import saupjang_info_list
import urllib

for id in range(100,len(saupjang_info_list.saupjang_list)):
    saupjanID=str(saupjang_info_list.saupjang_list[id])
    url_query='http://125.140.110.217:4242/q?start=2016/11/01-00:00:00&end=2017/04/30-00:00:00&m=avg:origin_data_please%7BSaupjang='+saupjanID+'%7D&o=&m=sum:energy%7BSaupjang='+saupjanID+'%7D&o=axis%20x1y2&yrange=%5B0:%5D&y2range=%5B0:%5D&wxh=1178x931&style=linespoint&png'
    pngname='enegy_show_'+saupjanID+'.jpg'
    urllib.urlretrieve(url_query, pngname)
