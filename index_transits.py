# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:55:39 2016

@author:
Maximilian N. Guenther
Battcock Centre for Experimental Astrophysics,
Cavendish Laboratory,
JJ Thomson Avenue
Cambridge CB3 0HE
Email: mg719@cam.ac.uk
"""



import numpy as np
from utils import mask_ranges



def index_transits(dic, obj_nr=None):
    """
    Returns:
    --------
    ind_tr : array
        indices of points in transit
    ind_out : array
        indices of points out of transit
    """
    
    if obj_nr is not None:
        N = int( 1. * ( dic['TIME'][obj_nr][-1] - dic['EPOCH'][obj_nr] ) / dic['PERIOD'][obj_nr] ) + 1
        tmid = np.array( [ dic['EPOCH'][obj_nr] + i * dic['PERIOD'][obj_nr] for i in range(N) ] )
        
        _, ind_tr, mask_tr = mask_ranges( dic['TIME'][obj_nr], tmid - dic['WIDTH'][obj_nr]/2., tmid + dic['WIDTH'][obj_nr]/2. )
        _, ind_tr_half, _ = mask_ranges( dic['TIME'][obj_nr], tmid - dic['WIDTH'][obj_nr]/4., tmid + dic['WIDTH'][obj_nr]/4. )
        _, ind_tr_double, _ = mask_ranges( dic['TIME'][obj_nr], tmid - dic['WIDTH'][obj_nr], tmid + dic['WIDTH'][obj_nr] )
              
        ind_out = np.arange( len(dic['TIME'][obj_nr]) )[ ~mask_tr ]

    else:
        N = int( 1. * ( dic['TIME'][-1] - dic['EPOCH'] ) / dic['PERIOD'] ) + 1
        
        tmid = np.array( [ dic['EPOCH'] + i * dic['PERIOD'] for i in range(N) ] )
        
        _, ind_tr, mask_tr = mask_ranges( dic['TIME'], tmid - dic['WIDTH']/2., tmid + dic['WIDTH']/2. )
        _, ind_tr_half, _ = mask_ranges( dic['TIME'], tmid - dic['WIDTH']/4., tmid + dic['WIDTH']/4. )
        _, ind_tr_double, _ = mask_ranges( dic['TIME'], tmid - dic['WIDTH'], tmid + dic['WIDTH'] )
              
        ind_out = np.arange( len(dic['TIME']) )[ ~mask_tr ]

    return ind_tr, ind_out 
    
    

#::: for binaries, mark the primary and secondary eclipse
def index_eclipses(dic, obj_nr=None):
    """
    Returns:
    --------
    ind_ecl1 : array
        indices of points in primary eclipse
    ind_ecl2 : array
        indices of points in secondary eclipse
    ind_out : array
        outside of any eclipse
    
    ! this assumes circular orbits !
    """
    #TODO: implement non-circular orbits
    
    
    if obj_nr is not None:
        print 'Not currently implemented.'
        return None


    else:
        N = int( 1. * ( dic['TIME'][-1] - dic['EPOCH'] ) / dic['PERIOD'] ) + 1
        
        tmid_ecl1 = np.array( [ dic['EPOCH'] +                    i * dic['PERIOD']  for i in range(N) ] )
        tmid_ecl2 = np.array( [ dic['EPOCH'] - dic['PERIOD']/2. + i * dic['PERIOD']  for i in range(N+1) ] )
        
        _, ind_ecl1,        mask_ecl1 = mask_ranges( dic['TIME'], tmid_ecl1 - dic['WIDTH']/2., tmid_ecl1 + dic['WIDTH']/2. )
#        _, ind_ecl1_half,   _         = mask_ranges( dic['TIME'], tmid_ecl1 - dic['WIDTH']/4., tmid_ecl1 + dic['WIDTH']/4. )
#        _, ind_ecl1_double, _         = mask_ranges( dic['TIME'], tmid_ecl1 - dic['WIDTH'],    tmid_ecl1 + dic['WIDTH']    )
              
        _, ind_ecl2,        mask_ecl2 = mask_ranges( dic['TIME'], tmid_ecl2 - dic['WIDTH_2']/2., tmid_ecl2 + dic['WIDTH_2']/2. )
#        _, ind_ecl2_half,   _         = mask_ranges( dic['TIME'], tmid_ecl2 - dic['WIDTH']/4., tmid_ecl2 + dic['WIDTH']/4. )
#        _, ind_ecl2_double, _         = mask_ranges( dic['TIME'], tmid_ecl2 - dic['WIDTH'],    tmid_ecl2 + dic['WIDTH']    )
        
        ind_out = np.arange( len(dic['TIME']) )[ ~(mask_ecl1 | mask_ecl2) ]


    return ind_ecl1, ind_ecl2, ind_out
    
