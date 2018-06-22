#!/usr/bin/python

import commands
import math
import linecache
import colorama
from colorama import Fore, Back, Style
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
    args = sys.argv[1:]
    
    mu, Cmu = configinfo.constants()
   
    if not args:
        print('\n' + Fore.BLACK + Style.BRIGHT + 'Usage:' + Style.RESET_ALL) 
        print('Turbulence calc [--turbcalc] Timestep calc [--timecalc] Rossiter Modes calc [rossitercalc] constants [--constants] help [--help, -h]' + '\n')
        sys.exit(1)

    if args[0] in ('--help','-h'):
        configinfo.display_defaults(mu, Cmu)
    
    if args[0] in ('--constants'):
        configinfo.display_defaults(mu, Cmu)
    
    if args[0] == '--turbcalc':
        logic.turbcalc(mu, Cmu)
        sys.exit(1)

    if args[0] == '--timecalc':
        logic.timecalc()
        sys.exit(1)

    if args[0] == '--rossitercalc':
        logic.rossitercalc()
        sys.exit(1)
  

if __name__ == '__main__':
  main()

  



