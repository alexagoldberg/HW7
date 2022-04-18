import numpy as np
import matplotlib.pyplot as plt

data=open("sed.txt", "r")

lines= data.readlines()
for i in range(0,3):
    lines.pop(0)

wavelength = [float(x.split(",")[0]) for x in lines]
luminosity = [float(x.split(",")[1]) for x in lines]

fig, axs = plt.subplots()
axs.plot(wavelength, luminosity)
axs.set_title('Plot 1')
axs.set_yscale('log')
axs.set_xscale('log')
plt.savefig('Goldberg_hw7.png', dpi=300)

xarray = np.array(wavelength)
yarray = np.array(luminosity)

import pandas as pd
import astropy.units as u

data = np.column_stack([xarray, yarray])
df = pd.DataFrame(data=data)


wavmicros= (df[0] > 10) & (df[0] < 1000)

dfcorrect=df[wavmicros]

integral=np.trapz(dfcorrect[0], dfcorrect[1])*u.Lsun
print(integral.to(u.erg/u.s))
