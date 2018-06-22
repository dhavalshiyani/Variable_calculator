#!/usr/bin/python

import commands
import math
import linecache
import colorama
from colorama import Fore, Back, Style
import argparse
import os
from os import sys, path
goaldir = os.path.join(os.getcwd(), "lib")
lib_path = os.path.abspath(goaldir)
sys.path.append(lib_path)

import configinfo
import logic 
import styles
    
def main():
    
    styles.ShowBanner()
    #args = sys.argv[1:]
    
    parser = argparse.ArgumentParser(description="Choose your tool:")
    parser.add_argument('--constants', action='store_true', help='Display constants')
    parser.add_argument('--turbcalc', action='store_true', help='Calculate turbulence properties')
    parser.add_argument('--timecalc', action='store_true', help='Calculate timestep')
    parser.add_argument('--rossitercalc', action='store_true', help='Calculate rossiter modes')
    parser.add_argument('--solvertype', default='blb', help='Choose a Boundary Layer based solver (blb) or a Mixing length based solver (mlb) | Default: blb')
    
    args = parser.parse_args()
    
    mu, Cmu = configinfo.constants()
   
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        print('\n')
        sys.exit(1)
    
    if args.constants:
        configinfo.display_defaults(mu, Cmu)
    
    if args.turbcalc:
        if args.solvertype in ('blb','mlb'):
            solverType = args.solvertype
        else:
            print('Enter the solver type either as \'blb\' or \'mlb\'')
            sys.exit(1)
        logic.turbcalc(mu, Cmu, solverType)
        sys.exit(1)

    if args.timecalc:
        logic.timecalc()
        sys.exit(1)

    if args.rossitercalc:
        logic.rossitercalc()
        sys.exit(1)
  

if __name__ == '__main__':
  main()

  



