#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:01:31 2022

@author: jerrysmacbookpro
"""
from datetime import datetime


def log_to_file(msg, fname, encoding="utf-8"):
    with open(fname, 'a') as f:
        f.write(f"{datetime.utcnow().isoformat()} - {' '.join(msg.split())}\n")
    return


file = "log.txt"
log_to_file("Start.", file)
log_to_file("Processing ...", file)
log_to_file("Read data.\n   Process data.   \n  Save    data.", file)
log_to_file("   Done.\n", file)
