# duotos dvi duomenu eilutes. rasti mediana

sar1 = [4,8,9,7,9]
sar2 = [5,8,9,-1,25,8,7,9]

def surastimediana(sar):
    sar.sort()
    ilgis = len(sar)
    if ilgis % 2 != 0:
        m0 = sar[ilgis//2]
    else:
        m0 = (sar[ilgis//2]+sar[ilgis//2-1])/2
    return m0

sar1.sort()
sar2.sort()
print(f'{sar1} mediana = {surastimediana(sar1)}')
print(f'{sar2} mediana = {surastimediana(sar2)}')