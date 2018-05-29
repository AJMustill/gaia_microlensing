# microlensing.py

# Contains routines for astrometric and lensing calculations such as sky motion and photometric magnification.

import numpy as np

#----------------------------------------------------------------------------------------------
# magnification of a point source as a function of angular distance and einstein radius

def magnification(dist,R_E):
    
    u = dist/R_E
    
    return (u**2 + 2) / (u*np.sqrt(u**2+4))

#----------------------------------------------------------------------------------------------
# net magnification accounting for dilution by lens

def net_magnification(GLens,GSource,peakMag):
    
    FSource1 = 10**(0.4*(GLens-GSource))
    FSource2 = FSource1*peakMag
    
    return (1+FSource2)/(1+FSource1)-1

#----------------------------------------------------------------------------------------------
# Einstein radius in mas
# ML in MSol, pi in mas
def REinstein(ML,piL,piS):
    
    RESol = 5906.5002    # 4GMSol/c2: Einstein radius of Sun in m for D_LS / (D_L D_S) = 1
    rel_par = piL - piS  # parallax difference, mas
    m2kpc = 1.0/3.0856776e19
    return np.sqrt(RESol*ML*rel_par*m2kpc)*360*3600*1000/(2*np.pi)

#----------------------------------------------------------------------------------------------
# find alignments and calculate magnification factors etc
# lens and source are np arrays N x [delta_ra,delta_dec,pmra,pmdec,parallax] 
#                                in [as,as,mas/yr,mas/yr,mas] relative to source at epoch
# (setting lens to (0,0) avoids some flotaing point problems)
# delta_ra should have been corrected by *cos(dec)

# time is time interval in years
# ML is lens mass in Solar units
# Earth is table of Earth ephemeris as seen from Sun
# RA Dec are those of lens at epoch for parallax calculations (ignore pm here)

def get_alignments(lens,source,time,ML,Earth,RA,Dec):
        
    Ntime = len(time)
    Npair = len(source)
    # these Nlens x Ntime arrays store delta ra and dec of the lens(es) under proper motion and parallax
    raLens = (np.outer(lens[:,0],np.ones(Ntime)) + np.outer(lens[:,2],time)/1000 +
              (Earth['X']*np.sin(np.radians(RA)) - Earth['Y']*np.cos(np.radians(RA)))*np.outer(lens[:,4],np.ones(Ntime))/1000)
    decLens = (np.outer(lens[:,1],np.ones(Ntime)) + np.outer(lens[:,3],time)/1000 +
               (Earth['X']*np.cos(np.radians(RA))*np.sin(np.radians(Dec)) + 
                Earth['Y']*np.sin(np.radians(RA))*np.sin(np.radians(Dec)) -
                Earth['Z']*np.cos(np.radians(Dec)))*np.outer(lens[:,4],np.ones(Ntime))/1000)
    
    raSource = (np.outer(source[:,0],np.ones(Ntime)) + np.outer(source[:,2],time)/1000 +
                (Earth['X']*np.sin(np.radians(RA)) - Earth['Y']*np.cos(np.radians(RA)))*np.outer(source[:,4],np.ones(Ntime))/1000)
    
    decSource = (np.outer(source[:,1],np.ones(Ntime)) + np.outer(source[:,3],time)/1000 +
               (Earth['X']*np.cos(np.radians(RA))*np.sin(np.radians(Dec)) + 
                Earth['Y']*np.sin(np.radians(RA))*np.sin(np.radians(Dec)) -
                Earth['Z']*np.cos(np.radians(Dec)))*np.outer(source[:,4],np.ones(Ntime))/1000)
    
    # compute angular distances assuming sources fixed for now
    distance2 = (raSource - raLens)**2 + (decSource - decLens)**2
    distance = np.sqrt(distance2)
    
    # Einstein Radius in mas; set parallax of source to zero if -ve
    R_E = REinstein(ML,lens[:,4],np.maximum(source[:,4],np.zeros(Npair)))
    
    #magnification for each source--lens pair for all t
    mag_factor = magnification(distance,np.outer(R_E,np.ones(Ntime))/1000)
    
    return (np.swapaxes(np.array([raLens, decLens]),0,1), 
            np.swapaxes(np.array([raSource, decSource]),0,1), distance, R_E, mag_factor)