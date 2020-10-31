#!/usr/bin/env python

# Copyright (c) 2020 Gregor Hildebrand

import os

workdir = os.path.expanduser("~/AppData/Local/Temp/")
workdir2 = os.path.expanduser("~/AppData/Local/Microsoft/Windows/Explorer/")
workdir3 = os.path.expanduser("~/AppData/Local/Microsoft/INetCache/IE/")
workdir4 = os.path.expanduser("~/Windows/Temp/")
workdir5 = os.path.expanduser("~/AppData/Local/CrashDumps/")
workdir6 = os.path.expanduser("~/Windows/Logs/")

if os.path.exists(workdir):
	for root,dirs,files in os.walk(workdir):
		for file in files:
			os.remove(os.path.join(root,file)) # join-method concatenates paths intelligently

if os.path.exists(workdir2):
	for root,dirs,files in os.walk(workdir2):
		for file in files:
			os.remove(os.path.join(root,file))

if os.path.exists(workdir3):
	for root,dirs,files in os.walk(workdir3):
		for file in files:
			os.remove(os.path.join(root,file))

if os.path.exists(workdir4):
	for root,dirs,files in os.walk(workdir4):
		for file in files:
			os.remove(os.path.join(root,file))

if os.path.exists(workdir5):
	for root,dirs,files in os.walk(workdir5):
		for file in files:
			os.remove(os.path.join(root,file))

if os.path.exists(workdir6):
	for root,dirs,files in os.walk(workdir6):
		for file in files:
			os.remove(os.path.join(root,file))
