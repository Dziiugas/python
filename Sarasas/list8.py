cmugis = [186, 205, 193, 201, 178, 221, 211, 217, 168, 158, 205, 165]
coliugis = [round(cm / 2.54, 2) for cm in cmugis]
print(coliugis)
txtugis = ['Aukstas' if i>= 180 else 'vidutinis'if i>=160 else 'zemas' for i in cmugis]
print(txtugis)