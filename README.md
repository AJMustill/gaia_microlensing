# gaia_microlensing

This repository contains code and tables to reproduce our predictions of future microlensing events based on an analysis of Gaia DR2. 

(C) 2018 Alexander James Mustill, Lund Observatory, Department of Astronomy & Theoretical Physics, Lund University, Box 43, SE-221 00 Lund, Sweden

If you make use of this code, please cite Mustill, Davies &amp; Lindegren (2018, A&amp;A submitted, https://arxiv.org/abs/1805.11638).

Please direct any queries to Alexander Mustill, alex@astro.lu.se

The repository contains the following files:

getNearbyStars.ipynb

This is a simple script to query the Gaia DR2 archive for stars within 100pc. To avoid the risk of the connexion being lost during a long query, the sky is divided into 360 sectors of 1 degree RA and a separate query executed for each, the results being saved into files 100pc_nnn.vot

analyseNearbyStars.ipynb

This queries the Gaia DR2 archive to find background objects to the list of nearby stars obtained from getNearbyStars.ipynb, searching within 20 years' proper motion plus parallax for any other sources. A list "interesting" of indices can be supplied if you have previously down-selected a sample and don't want to run queries on all 700,000 objects.

analyseInterestingStars.ipynb

This queries the Gaia archive for background sources to the list of "interesting" stars and picks out source--lens pairs that approach within 0.1 arcsec, accounting for nominal parallax and proper motion.

DR2_5918299904067162240.ipynb

This script queries one particular object (DR2 5918299904067162240 by default), performs MC simulations of the source and lens trajectories, and generates diagnostic plots of the sky motion, magnification, duration and other key lensing parameters.

DR2_5918299904067162240.vot

VOTable containing a single lens star, to be read by DR2_5918299904067162240.ipynb

microlensing.py

Contains routines for astrometric and lensing calculations such as sky motion and photometric magnification.

photometry.py

Contains routines related to Gaia photometry, such as bolometric correction and a mass--luminosity relation.

gaiaDR2

Folder containing astroquery.gaia ( https://astroquery.readthedocs.io/en/latest/gaia/gaia.html ) files modified for Gaia DR2.

EarthEphemerisNt8000.txt
SolRADecNt8000.txt

Tables from JPL Horizons service ( https://ssd.jpl.nasa.gov/horizons.cgi ) containing the Earth's (x,y,z) position from 2015.5 to 2035.5 for the calculation of parallax and the Sun's RA and Dec for the calculation of Solar elongation at a given epoch.

DR2_final.csv

Ascii file containing details for all 30 of our close source--lens pairs. Includes the columns of Table A1 of Mustill, Davies & Lindegren (2018). A full listing of columns is: 

DR2 id lens:        Gaia DR2 id of the lens star
G mag lens:         G-band appanent magnitude of the lens star
RA lens:            Right ascension of the lens star (degrees)
Dec lens:           Declination of the lens star (degrees)
pmra lens:          Proper motion in RA mu_alpha* of the lens star (mas/yr)
pmdec lens:         Proper motion in Dec mu_delta of the lens star (mas/yr)
parallax lens:      Parallax of the lens star (mas)
Teff lens low:      Priam Teff of the lens star (16th percentile, K)
Teff lens:          Priam Teff of the lens star (nominal, K)
Teff lens high:     Priam Teff of the lens star (84th percentile, K)
M lens low:         Mass estimate for lens star from low Teff (M_Sol)
M lens:             Mass estimate for lens star from nominal Teff (M_Sol)
M lens high:        Mass estimate for lens star from high Teff (M_Sol)
L lens low:         Luminosity estimate for lens star from low Teff (L_Sol)
L lens:             Luminosity estimate for lens star from nominal Teff (L_Sol)
L lens high:        Luminosity estimate for lens star from high Teff (L_Sol)
RHZ low:            Habitable zone radius of lens star estimated from low Teff (au)
RHZ:                Habitable zone radius of lens star estimated from nominal Teff (au)
RHZ high:           Habitable zone radius of lens star estimated from high Teff (au)
RE as low:          Angular Einstein radius estimate from low Teff (arcsec)
RE as:              Angular Einstein radius estimate from nominal Teff (arcsec)
RE as high:         Angular Einstein radius estimate from high Teff (arcsec)
RE au low:          Einstein radius estimate from low Teff (au)
RE au:              Einstein radius estimate from nominal Teff (au)
RE au high:         Einstein radius estimate from high Teff (au)
DR2 id source:      Gaia DR2 id of the source star
G mag source:       G-band appanent magnitude of the source star
RA source:          Right ascension of the source star (degrees)
Dec source:         Declination of the source star (degrees)
pmra source:        Proper motion in RA mu_alpha* of the source star (mas/yr)
pmdec source:       Proper motion in Dec mu_delta of the source star (mas/yr)
parallax source:    Parallax of the source star (mas)
prob 1RE:           Probability of passing within 1 nominal Einstein radius (%)
Dmin low:           Minimum approach (16th percentile, arcsec)
Dmin:               Minimum approach (median, arcsec)
Dmin high:          Minimum approach (84th percentile, arcsec)
max mag low:        Maximum magnification (no dilution, 16th percentile)
max mag:            Maximum magnification (no dilution, median)
mag max high:       Maximum magnification (no dilution, 84th percentile)
max mag net low:    Maximum magnification (with dilution, 16th percentile)
max mag net:        Maximum magnification (with dilution, median)
mag max net high:   Maximum magnification (with dilution, 84th percentile)
Tmax low:           Date of peak magnification (16th percentile)
Tmax:               Date of peak magnification (median)
Tmax high:          Date of peak magnification (84th percentile)
duration low:       Time undiluted magnification exceeds 10^-2 (16th percentile, days)
duration:           Time undiluted magnification exceeds 10^-2 (median, days)
duration high:      Time undiluted magnification exceeds 10^-2 (84th percentile, days)
duration net low:   Time diluted magnification exceeds 10^-4 (16th percentile, days)
duration net:       Time diluted magnification exceeds 10^-4 (median, days)
duration net high:  Time diluted magnification exceeds 10^-4 (84th percentile, days)
Sol elongation low: Solar elongation at peak magnification (16th percentile, degrees)
Sol elongation:     Solar elongation at peak magnification (median, degrees)
Sol elongation high: Solar elongation at peak magnification (84th percentile, degrees)
