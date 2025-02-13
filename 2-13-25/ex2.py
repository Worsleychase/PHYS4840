# ex2.py
# 2-13-25

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl
from myFuncLib import np
from myFuncLib import plt
blue, green, red, probability = np.loadtxt('NGC6341.dat', usecols=(8, 14, 26, 32), unpack=True)

magnitude = blue
color     = blue - red

quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))

mod = mfl.distMod(8.63*10**3)
magnitude -= mod

load_file = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)

age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9
age_Gyr = age_Gyr_1e9

age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]

Teff = 10.0**logTeff
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

phases_for_desired_age = phase[age_selection]
desired_phases = np.where(phases_for_desired_age <= 3)

## now, we can restrict our equal-sized arrays by phase
cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

fig, ax = plt.subplots(figsize=(8,16))

ax.scatter(color[quality_cut], magnitude[quality_cut], c="k", s = 4, alpha = 0.8)
ax.plot(cleaned_color, cleaned_magnitude, c='g', linewidth = 3)
fig.gca().invert_yaxis()
ax.set_xlabel("Color: B-R", fontsize=20)
ax.set_ylabel("Magnitude: B", fontsize=20)
ax.set_title('Isochrone Model vs. NGC Data', fontsize=22)
ax.set_xlim(-.2, 2)
ax.set_ylim(8,0)
plt.show()
plt.close()
plt.savefig('ex2.png')