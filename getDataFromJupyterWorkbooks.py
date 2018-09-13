# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 19:04:45 2018

@author: Gaston Guillaux
"""
#TO GET THE FILE DIRECTORY USED BY THE NOTEBOOK IN THE REMOTE SERVER
import os
print(os.getcwd())

#TO GET THE REMOTE HOST SERVER NAME
import socket
print(socket.gethostname())

#TO SHOW ALL AVAILABLE FILES IN THE PROJECT
from IPython.display import FileLink, FileLinks
FileLinks('.') #lists all downloadable files on server