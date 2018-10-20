#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:39:23 2018

@author: fabrizzio
"""

import sys
from scholar import Author
import json

def main(args):
    
   if (len(args) < 2):    
        raise Exception('Author id missing!')
   else:
       author = args[1]

   return Author(author)
#----------------------------------------------

authorData = main(sys.argv)

file = open("citecount.json","w")
file.write(json.dumps(authorData.publication))
file.close()
