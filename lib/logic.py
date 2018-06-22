import sys
import os
import commands
import math
import argparse
import linecache
import configinfo

mu,Cmu = configinfo.constants()

def turbcalc(mu, Cmu):
    
    #WIP to set defaults
    #parser = argparse.ArgumentParser(description="Change default #solver type")
    #parser.add_argument('--solvertype', default='blb', help='Choose a #Boundary Layer based solver (blb) or a Mixing length based solver #(mlb) -- Default: blb')
    #args = parser.parse_args()
  
    #User-input
    try:
        calcType = raw_input('\n'"Calculate boundary layer(\"del\") or inlet length(\"len\"): ")
        solverType = raw_input("SolverType boundary layer based \"blb\" or Mixing length based \"mlb\": ")

        velocity = float(input('\n'"Enter freestream velocity: "))
        turb_intensity = (float(input("Enter turbulent intensity(%): ")))*0.01
        
        print(turb_intensity)
    
    except ValueError:
        PrintException()
        print'Match the words within \'\''
        sys.exit(1)

  #Basic_Calculations 
    k = (1.5*((velocity*turb_intensity)**2))
  
    
  #Case_Dependent Calculations:
    if calcType == 'del':  
        ref_length = float(input("Enter reference length: "))
        Re = float((velocity*ref_length)/mu)
        if Re < 2300:
            delta = 4.91*ref_length/(Re**(1.0/5.0))
    else:
        delta = 0.382*ref_length/(Re**(1.0/5.0)) 
    
    if calcType == 'len': #Fix this Re calculated before knowing the value
        delta = float(input("Enter boundary layer thickness: "))
        if Re < 2300:
            ref_length = (delta*(Re**(1.0/5.0)))/4.91
        else:
            ref_length = (delta*(Re**(1.0/5.0)))/0.382      
            Re = float((velocity*ref_length)/mu)

    if solverType == 'blb':
        l = (0.22*delta)
        epsilon = (Cmu*((k**1.5)/l))
        omega = ((math.sqrt(k))/l)

    if solverType == 'mlb':
        l = (0.4*delta)
        epsilon = ((Cmu**(3.0/4.0))*((k**1.5)/l))
        omega = ((Cmu**(-1.0/4.0))*((math.sqrt(k))/l)) 


  #Output
    print '\n''Output:'
    print '--------------------------------------'
    if Re > 2300:
        print 'Flow is TURBULENT'
    else:
        print 'Flow is LAMINAR'

    print '\n''Re:', round(Re, 4) 
    print 'Boundary layer thickness:', round(delta, 6), ' m'
    print 'Mixing length(l):', round(l, 4)

    print '\n''k:', round(k, 6)
    print 'Epsilon:', round(epsilon, 6)
    print 'Omega:', round(omega, 6)
    print '--------------------------------------''\n'

    return(Re, k, epsilon,omega, delta)

def timecalc():

  #User-input
  l = float(input('\n'"Enter length of the edge (m): "))
  n = float(input("Enter number of divisions (n): "))
  R = float(input("Enter bias factor (R): "))
  velocity = float(input("Enter freestream velocity (m/s): "))
  
  #Small r calc:
  try:
    r = R**(1.0/(n-1.0))
  except ZeroDivisionError, e:
    #Simpler way to throw exception without details #z = e
    #print '\n', z, '\n''Number of divisions (n) cannot be 1'
    PrintException()
    print 'Number of divisions cannot be 1''\n'
    sys.exit(1)
  
  #Grading dependent calculations:
  if R > 1.0:
    alpha = R
    #Smallest Cell size calculation:
    deltax_s = (l*(r-1))/((alpha*r)-1)
  if R < 1.0:
    alpha = (1.0-(r**(-n))+(r**(-1.0)))
    #Smallest Cell size calculation:
    deltax_s = (l*(r-1))/((alpha*r)-1)
  if R == 1.0:
    print '\n'"No Biasing found"
    deltax_s = l/n  

  #Time-step calc
  delta_t = (1.0*deltax_s)/velocity 
  
  #Output:
  print '\n''Output:'
  print '-----------------------------------------'
  print "Time-step should be <= ",delta_t
  print "Smallest cell size = ",deltax_s
  print '-----------------------------------------'
  print '\n'

  return

def rossitercalc():
  
  #create list of output
  L_Frequencies = [] 
  L_keys = []

  #constants
  alpha = 0.25
  k = 0.57
  a = 343.54
  gamma = 1.4

  #User-input
  m = int(input('\n'"Enter the number of modes: "))
  L = float(input("Enter the length of cavity (m): "))
  Uinf = float(input("Enter freestream velocity (m/s): "))      
  
  #Common terms calculated once (time savers):
  Minf = Uinf/a
  #print '\n'"M: ", Minf 
  outside_multiplier = Uinf/L
  #print 'outside_multiplier: ', outside_multiplier
  gamma_term = (gamma-1)/2
  #print '\n', gamma_term
  denominator = ((Minf/math.sqrt(1+gamma_term*Minf))+(1/k))
  #print '\n'"Denominator: ", denominator
  print '\n'
  print 'Rossiter Frequencies'
  print '--------------------'
  for i in range(1, m+1):
    fi = outside_multiplier*(i-alpha)/denominator
    print 'f%d = %f Hz' %(i, fi)
    L_Frequencies.append(fi)
    L_keys.append("f_%d" %(i))
  
  print '--------------------'
  print '\n'


  #Table format from tabulate ignored for now
  #print L_keys
  #print L_Frequencies
  return