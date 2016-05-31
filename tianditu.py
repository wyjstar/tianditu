#coding: utf-8
import os
import urllib2
import PIL.Image as Image

def geturl_ditu(y, x):
    url_ditu = 'http://www.csmap.gov.cn/wmts/kvp/services/yingxiangditu/MapServer/TDTWMTSServer?' + \
    'SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&FORMAT=tiles&TILEMATRIXSET=c&STYLE=default&' + \
    'LAYER=vec&TILEMATRIX=18&TILEROW=' + str(y) + '&TILECOL=' + str(x)
    return url_ditu

def geturl_dituzhuji(y, x):
    url_dituzhuji = 'http://www.csmap.gov.cn/wmts/kvp/services/yingxiangdituzhuji/MapServer/TDTWMTSServer?' + \
    'SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&FORMAT=tiles&TILEMATRIXSET=c&STYLE=default&' + \
    'LAYER=vec&TILEMATRIX=18&TILEROW=' + str(y) + '&TILECOL=' + str(x)
    return url_dituzhuji

#Capture Parameter
tilesize = 256
tiletop = 45004
tileheight = 5
tileleft = 213315
tilewidth = 6

ditu_bigimg = Image.new('RGBA',(tilesize * tilewidth, tilesize * tileheight))
dituzhuji_bigimg = Image.new('RGBA',(tilesize * tilewidth, tilesize * tileheight))
for y in range(0, tileheight):
    for x in range(0, tilewidth):
        #Download Ditu
        ditu_imgurl = geturl_ditu(tiletop + y, tileleft + x)
        ditu_img = urllib2.urlopen(ditu_imgurl)
        ditu_file = open('ditu-' + str(y) + '_' + str(x) +'.png', "wb")
        ditu_file.write(ditu_img.read())
        ditu_file.close()
        print('ditu-' + str(y) + '_' + str(x) +'.png' + '  Saved!')
        ditu_bigimg.paste(Image.open('ditu-' + str(y) + '_' + str(x) +'.png'), (x * tilesize, y * tilesize))
        #Download DituZhuji
        dituzhuji_imgurl = geturl_dituzhuji(tiletop + y, tileleft + x)
        dituzhuji_img = urllib2.urlopen(dituzhuji_imgurl)
        dituzhuji_file = open('dituzhuji-' + str(y) + '_' + str(x) +'.png', "wb")        
        dituzhuji_file.write(dituzhuji_img.read())
        dituzhuji_file.close()
        print('dituzhuji-' + str(y) + '_' + str(x) +'.png' + '  Saved!')
        dituzhuji_bigimg.paste(Image.open('dituzhuji-' + str(y) + '_' + str(x) +'.png'), (x * tilesize, y * tilesize))

ditu_bigimg.save('ditu.png')
print('ditu.png  Saved!')
dituzhuji_bigimg.save('dituzhuji.png')
print('dituzhuji.png  Saved!')
dituall = Image.new('RGBA',(tilesize * tilewidth, tilesize * tileheight))
dituall.paste(Image.open('ditu.png'), (0, 0))
dituall.paste(Image.open('dituzhuji.png'), (0, 0), Image.open('dituzhuji.png'))
dituall.save('dituall.png')
print('dituall.png  Saved!')
