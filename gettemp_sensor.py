#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:43:44 2019

@author: jmanning
"""

import os
import glob
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir='/sys/bus/w1/devices/'
device_folder=glob.glob(base_dir+'28*')[0]
device_file=device_folder+'/w1_slave'
def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()

    return lines
def read_temp():
    lines=read_temp_raw()
    while lines[0].strip()[-3:]!='YES':
        time.sleep(0.2)
        lines=read_temp_raw()
    equals_pos=lines[1].find('t=')
    if equals_pos!=-1:
        temp_string=lines[1][equals_pos+2:]
        temp=float(temp_string)/1000
    return temp
for i in range(60):
    print(read_temp())
    time.sleep(1)