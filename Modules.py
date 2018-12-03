#! /usr/bin/env python3

import fibo

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib
print(fib(500))
from fibo import *

print(fib(100))
import sys

sys.path.append('/ufs/guido/lib/python')
import fibo, sys

print(dir(fibo))
print(dir(sys))
a = [1, 2, 3, 4, 5]
import fibo

fib = fibo.fib
print(dir())
import builtins

print(dir(builtins))
print('包')
'''
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
'''
