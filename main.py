#!/usr/bin/python
#import sys
import commands
import math
#from tabulate import tabulate
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

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print '\n''EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    
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

  



