import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

G = 6.67384e-11
SOLAR_RADIUS = 6.963e8
SOLAR_MASS = 1.989e30
SOLAR_TEMP = 5778

data = pd.read_csv('koi_original.csv')

#0. Skim over a few columns of the csv data.

#1. Remove the header content from the top of the csv file, this was done by opening the csv file in excel.

#2. filter out data points without 'candidate' status from "Dispositions using Kepler Data - koipdisposition"
planet_candidates = data[data['koi_pdisposition'] == "CANDIDATE"]





# # Task 2.4.1a - Habitable Zone Calculation
# task241a = planet_candidates[['kepoi_name', 'koi_slogg', 'koi_slogg_err1', 'koi_slogg_err2', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'koi_smass', 'koi_smass_err1', 'koi_smass_err2']]

# #convert surface gravity (log(cm/s^2)) to si units by raising to the power of 10 (cm/s^2) and divide by 100 (m/s^2)
# task241a['koi_sg'] = np.power(10, task241a['koi_slogg']) / 100
# task241a['koi_sg_err1'] = np.power(10, task241a['koi_slogg_err1']) / 100
# task241a['koi_sg_err2'] = np.power(10, task241a['koi_slogg_err2']) / 100

# #convert from solar radii to m
# task241a['koi_rad'] = task241a['koi_srad'] * SOLAR_RADIUS
# task241a['koi_rad_err1'] = task241a['koi_srad_err1'] * SOLAR_RADIUS
# task241a['koi_rad_err2'] = task241a['koi_srad_err2'] * SOLAR_RADIUS

# # M = gr^2/G (solar masses)
# task241a['mass_calculated'] = (task241a['koi_sg'] * task241a['koi_rad']**2) / G / SOLAR_MASS

# #include uncertainties in calculation
# task241a['perc_unc_sgravity'] = (task241a['koi_sg_err1'] - task241a['koi_sg_err2']) / 2 / task241a['koi_sg'] * 100
# task241a['perc_unc_radius'] = (task241a['koi_rad_err1'] - task241a['koi_rad_err2']) / 2 / task241a['koi_rad'] * 100
# task241a['perc_unc_mass'] = task241a['perc_unc_sgravity'] + task241a['perc_unc_radius']
# task241a['abs_unc_mass'] = task241a['perc_unc_mass'] / 100 * task241a['mass_calculated']

# #final submission - kepoi, surface gravity (log(cm/s^2)), radius (solar radii), mass (solar masses), 
# task241a_final = task241a[['kepoi_name', 'koi_slogg', 'koi_slogg_err1', 'koi_slogg_err2', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'koi_smass', 'koi_smass_err1', 'koi_smass_err2', 'mass_calculated', 'abs_unc_mass']]
# task241a_final.to_csv('task241a_final.csv', index=False)
# # some datapoints appear to be duplicates because they are members of the same star system




# #Task 2.4.1b
# task241b = planet_candidates[['kepoi_name', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'koi_steff', 'koi_steff_err1', 'koi_steff_err2', 'koi_smass', 'koi_smass_err1', 'koi_smass_err2',]]

# #converting to dimensionless units - koi_srad already in desired units
# task241b['koi_ssteff'] = task241b['koi_steff'] / SOLAR_TEMP
# task241b['koi_ssteff_err1'] = task241b['koi_steff_err1'] / SOLAR_TEMP
# task241b['koi_ssteff_err2'] = task241b['koi_steff_err2'] / SOLAR_TEMP

# #given equation: l/lsun = (r/rsun)^2*(t/tsun)^4
# task241b['sluminosity'] = task241b['koi_srad']**2 * task241b['koi_ssteff']**4

# #error propagation
# task241b['frac_unc_sradius'] = (task241b['koi_srad_err1'] - task241b['koi_srad_err2']) / 2 / task241b['koi_srad']
# task241b['frac_unc_ssteff'] = (task241b['koi_ssteff_err1'] - task241b['koi_ssteff_err2']) / 2 / task241b['koi_ssteff']
# task241b['abs_unc_sluminosity'] = (2*task241b['frac_unc_sradius'] + 4*task241b['frac_unc_ssteff']) * task241b['sluminosity']

# #given equation
# task241b['radius_inner'] = np.sqrt((1/1.1) * task241b['sluminosity']) 
# task241b['radius_outer'] = np.sqrt((1/0.53) * task241b['sluminosity'])
# task241b['min_radius_inner'] = np.sqrt((1/1.1) * (task241b['sluminosity'] - task241b['abs_unc_sluminosity']))
# task241b['min_radius_outer'] = np.sqrt((1/0.53) * (task241b['sluminosity'] - task241b['abs_unc_sluminosity']))
# task241b['max_radius_inner'] = np.sqrt((1/1.1) * (task241b['sluminosity'] + task241b['abs_unc_sluminosity']))
# task241b['max_radius_outer'] = np.sqrt((1/0.53) * (task241b['sluminosity'] + task241b['abs_unc_sluminosity']))

# task241b_final = task241b[['kepoi_name', 'koi_smass', 'koi_smass_err1', 'koi_smass_err2', 'sluminosity', 'abs_unc_sluminosity', 'radius_inner', 'radius_outer', 'max_radius_inner', 'max_radius_outer', 'min_radius_inner', 'min_radius_outer']]
# task241b_final.to_csv('task241b_final.csv', index=False)




#Task 2.4.2c
tvr = planet_candidates[['koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'koi_steff', 'koi_steff_err1', 'koi_steff_err2']]

#convert all units to relative solar quantity for better visibility
tvr['koi_steff'] = tvr['koi_steff'] / SOLAR_TEMP
tvr['koi_steff_err1'] = tvr['koi_steff_err1'] / SOLAR_TEMP
tvr['koi_steff_err2'] = tvr['koi_steff_err2'] / SOLAR_TEMP * -1

tvr['koi_srad_err2'] = -1 * tvr['koi_srad_err2']

plt.errorbar(tvr['koi_srad'], tvr['koi_steff'], xerr=[tvr['koi_srad_err1'], tvr['koi_srad_err2']], yerr=[tvr['koi_steff_err1'], tvr['koi_steff_err2']], fmt='o', capsize=5)
plt.xlabel('Stellar Radius')
plt.ylabel('Stellar Temperature')
plt.title('Graph of Stellar Temperature against Stellar Radius')
plt.show()
