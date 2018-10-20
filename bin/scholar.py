#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:27:31 2018

@author: fabrizzio
"""

from pyquery import PyQuery as pq
from six.moves import urllib
from math import floor, sqrt

#def install_and_import(package):
#    import importlib
#    try:
#        importlib.import_module(package)
#    except ImportError:
#        import pip
#        pip.main(['install', package])
#    finally:
#        globals()[package] = importlib.import_module(package)


        
class Author:
    def __init__(self, author = None):
        
        if (author == None):
            raise ValueError('Missing author.')
        
        self.hIndex = 0;
        self.gIndex = 0;
        self.citations = 0;
        self.author = author
        self.publication = []
        self.__extractScholar(author)
        
    def __extractScholar(self,author):
        
        scholarUrl = "https://scholar.google.com/citations"
        url = scholarUrl + "?user=" + author + "&hl=en&cstart=0&pagesize=100"
        f = urllib.request.urlopen(url)
        res = f.read()
        f.close()
        
        
        tmpFind = pq(res).find( "#gsc_a_b" )
        tmpPubliArray = pq(tmpFind).find( ".gsc_a_t" ).find( "a" )
        tmp_publi_cite = pq(tmpFind).find( ".gsc_a_c" )
        
        citedPapers = 0;
        regexTerm = ".*(citation_for_view=[\\d\\w\\-_]+\\:)"
        for i in range (0,len(tmpPubliArray)):
            name = pq(tmpPubliArray[i]).text()
            id = (pq(tmpPubliArray[i]).attr( "data-href").replace(regexTerm, ""))[110:]
            url = 'https://scholar.google.com' + (pq(tmpPubliArray[i]).attr( "data-href").replace(regexTerm, ""))
            citen = pq(tmp_publi_cite[i]).text()
            if (citen is ""):
                count = 0
            else:
                if (citen[-1:] == "*"):
                    count = int(citen[0:-1])
                else:
                    count = int(citen)
            
            citedPapers += count    
            self.publication.append({"id": id, "name": name, "url": url, "citecount" : count})
        
        tmpCitationFind = pq(res).find( "#gsc_rsb_st" )
        tmp_total_cite = pq(tmpCitationFind).find( ".gsc_rsb_std" )
        
        for i in range (0, len(tmp_total_cite)):
            if ( i == 0 ):
                citations = int(pq(tmp_total_cite[i]).text())
                sqrtCitations = floor(sqrt(int(citations)))
                gIndex = (citedPapers, sqrtCitations)[sqrtCitations <= citedPapers]        				
            if ( i == 2 ):
                hIndex = int(pq(tmp_total_cite[i]).text())
    
        self.citations = citations
        self.hIndex = hIndex
        self.gIndex = gIndex
