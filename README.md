# gaia_microlensing

This repository contains code and tables to reproduce our predictions of future microlensing events based on an analysis of Gaia DR2. 

(C) 2018 Alexander James Mustill, Lund Observatory, Department of Astronomy & Theoretical Physics, Lund University, Box 43, SE-221 00 Lund, Sweden

If you make use of this code, please cite Mustill, Davies &amp; Lindegren (2018, A&amp;A submitted).

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

DR2_final.csv

Ascii file containing details for all 30 of our close source--lens pairs. Includes the columns of Table A1 of Mustill, Davies & Lindegren (2018).

EarthEphemerisNt8000.txt
SolRADecNt8000.txt

Tables from JPL Horizons service ( https://ssd.jpl.nasa.gov/horizons.cgi ) containing the Earth's (x,y,z) position from 2015.5 to 2035.5 for the calculation of parallax and the Sun's RA and Dec for the calculation of Solar elongation at a given epoch.
