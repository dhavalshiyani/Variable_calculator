import sys
import os
import commands
import math
#from tabulate import tabulate
import linecache
import colorama
from colorama import Fore, Back, Style

def constants():
    mu = 1.325581395e-05
    Cmu=0.09 
    
    return mu, Cmu

def display_defaults(mu, Cmu):
    print '\n''Constants:'
    print '----------------------------------------'
    print 'mu = %f kg/m3' %(mu)
    print 'Cmu=',Cmu
    print 'Speed of Sound (a) = 343.54 m/s'
    print 'All constants above evaluated at 273K', '\n' 
    print 'Rossiter Mode Constants (Heller & Bliss)'  
    print 'alpha = 0.25'
    print 'k = 0.57'
    print 'gamma = 1.4 (Monoatomic)'
    print '----------------------------------------'
    print '\n'
    
    return 0

def license():
    print(Fore.BLACK + Style.DIM + '''MIT License
Copyright (c) [2018] [Dhaval Shiyani]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
----------------------------------------------------------------------''' + Style.RESET_ALL)
    
    return 0

def help():
    #placeholder
    return 0