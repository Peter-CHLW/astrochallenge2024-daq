import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

G = 6.67384e-11
SOLAR_RADIUS = 6.963e8
SOLAR_MASS = 1.989e30

data = pd.read_csv('koi_original.csv')

#0. Skim over a few columns of the csv data.

#1. Remove the header content from the top of the csv file, this was done by opening the csv file in excel.

#2. filter out data points without 'candidate' status from "Dispositions using Kepler Data - koipdisposition"
planet_candidates = data[data['koi_pdisposition'] == "CANDIDATE"]



# Task 2.4.1 - Habitable Zone Calculation
task241 = planet_candidates[['kepoi_name', 'koi_slogg', 'koi_slogg_err1', 'koi_slogg_err2', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'koi_smass', 'koi_smass_err1', 'koi_smass_err2']]

#convert surface gravity (log(cm/s^2)) to si units by raising to the power of 10 (cm/s^2) and divide by 100 (m/s^2)
task241['koi_sg'] = np.power(10, task241['koi_slogg']) / 100
task241['koi_sg_err1'] = np.power(10, task241['koi_slogg_err1']) / 100
task241['koi_sg_err2'] = np.power(10, task241['koi_slogg_err2']) / 100

#convert from solar radii to m
task241['koi_rad'] = task241['koi_srad'] * SOLAR_RADIUS
task241['koi_rad_err1'] = task241['koi_srad_err1'] * SOLAR_RADIUS
task241['koi_rad_err2'] = task241['koi_srad_err2'] * SOLAR_RADIUS

# M = gr^2/G (solar masses)
task241['mass_calculated'] = (task241['koi_sg'] * task241['koi_rad']**2) / G / SOLAR_MASS

#include uncertainties in calculation
task241['perc_unc_sgravity'] = (task241['koi_sg_err1'] - task241['koi_sg_err2']) / 2 / task241['koi_sg'] * 100
task241['perc_unc_radius'] = (task241['koi_rad_err1'] - task241['koi_rad_err2']) / 2 / task241['koi_rad'] * 100
task241['perc_unc_mass'] = task241['perc_unc_sgravity'] + task241['perc_unc_radius']
task241['abs_unc_mass'] = task241['perc_unc_mass'] / 100 * task241['mass_calculated']

#final submission - kepoi, surface gravity (log(cm/s^2)), radius (solar radii), mass (solar masses), 
task241_final = task241[['kepoi_name', 'koi_slogg', 'koi_slogg_err1', 'koi_slogg_err2', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'koi_smass', 'koi_smass_err1', 'koi_smass_err2', 'mass_calculated', 'abs_unc_mass']]
task241_final.to_csv('task241_final.csv', index=False)
# some datapoints appear to be duplicates because they are members of the same star system



