# photometry.py
#
# Contains routines related to Gaia photometry, such as bolometric correction and a mass--luminosity relation.

import numpy as np

# bolometric correction for G band as defined in Andrae+18, Eq 7 and Table 4

# I haven't vectorised it so feed it one Teff at a time!

# Teff in K

def BCG(Teff):
    
    TeffSol = 5772.0
    
    if Teff >= 4000:
        a = np.array([6.000e-02,6.731e-05,-6.647e-08,2.859e-11,-7.197e-15])
    else:
        a = np.array([1.749e+00,1.977e-03,3.737e-07,-8.966e-11,-4.183e-14])
        
    i = np.array([0,1,2,3,4])
    return sum(a*(Teff-TeffSol)**i)


# log10 of bolometric luminosity (Andrae+18, Eq 4)

# G is apparent G mag
# Teff in K
# parallax in mas
# AG is G-band extinction

def logLBol(G,Teff,parallax,AG):
    
    MBolSol = 4.74
    
    MG = G - 5.0*np.log10(100.0/parallax) - AG
    
    return -0.4*(MG + BCG(Teff) - MBolSol)

# mass-luminosoity relation from Salaris & cassisi 05
# mass, luminosity in Solar units

def MtoL(M):
    if M >= 2.0:
        return 1.866*M**3.6
    if M >= 0.5 and M < 2.0:
        return M**4.5
    if M < 0.5:
        return 0.2679*M**2.6
    
def LtoM(L):
    if L >= 22.63:
        return (L/1.866)**(1.0/3.6)
    if L >= 0.04419 and L < 22.63:
        return L**(1.0/4.5)
    if L < 0.04419:
        return (L/0.2679)**(1.0/2.6)
    
# Nominal HZ where T_eq = T_eq, Earth
# returns R in au

def RHZ(L):
    return np.sqrt(L)