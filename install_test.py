#!/usr/bin/env python

import serial
import sys,time
import signal
from time import ctime,sleep
import glob,struct
from multiprocessing import Process,Manager,Array
import threading
import hid


print 'Everything seems to be installed correctly!'

