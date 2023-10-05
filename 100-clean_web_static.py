#!/usr/bin/python3
""" Cleans old files"""

from datetime import datetime
import tarfile
from fabric.api import *
import os

env.hosts = ["18.210.18.197 ", "54.86.230.242"]
env.user = "ubuntu"


def do_clean(value=0):
    """ Removes all but given value of archives"""
    value = int(value)
    if value < 2:
        value = 1
    value += 1
    value = str(value)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              value + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            value + " | xargs -I {} rm -rf -- {}")
