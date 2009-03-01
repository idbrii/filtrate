#! /usr/bin/env python

import re

def parse(filename):
    # open the file
    # search for Project delimiter
    file = open(filename, 'r')
    return find_project(file)

def find_project(file):
    '''
    >>> fake_file = (
    ... 'Microsoft Visual Studio Solution File, Format Version 10.00', 
    ... '# Visual C++ Express 2008', 
    ... 'Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "SDL", "SDL\SDL.vcproj", "{81CE8DAF-EBB2-4761-8E45-B71ABCCA8C68}"', 
    ... 'EndProject', 
    ... 'Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "SDLmain", "SDLmain\SDLmain.vcproj", "{DA956FD3-E142-46F2-9DD5-C78BEBB56B7A}"', 
    ... 'EndProject'
    ... )
    >>> results = find_project(fake_file)
    >>> for r in results: print r
    SDL\SDL.vcproj
    SDLmain\SDLmain.vcproj
    '''
    # capture the filepaths. format: Project(junk)=junk,junk, "filepath"
    proj_reg = re.compile('^Project(.*)=(.*),(.*),\s*\"(.*)\"')
    found_proj = []

    for line in file:
        result = proj_reg.match(line)
        if result:
            found_proj.append(result.group(3).strip(' "'))

    return found_proj

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
        
