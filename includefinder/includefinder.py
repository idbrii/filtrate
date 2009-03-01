#! /usr/bin/env python

import xml.dom.minidom as minidom
import os.path as path

import slnparse

def fixpath(in_path):
    ''' Since os.path doesn't seem to care about converting Windows pathnames   
        to unix, we munge it here.

        >>> import os.path
        >>> fixpath('/file\\other.txt') # hacky. where is test run! 
        '/file/other.txt'
    '''
    in_path = in_path.replace('\\', '/')
    in_path = path.normpath(in_path)
    in_path = path.abspath(in_path)
    return in_path

def get_include_dirs(proj):
    inc_dirs = {}
    for tag in proj.getElementsByTagName('Tool'):
        try:
            # try to grab the value
            inc_dir = tag.attributes['AdditionalIncludeDirectories'].value

            # if we get it, then split it up and add
            for dir in inc_dir.split(','):
                inc_dirs[ fixpath(dir) ] = None # add to hash for quick uniquify
        except:
            pass

    # get unique elements
    return inc_dirs.keys()


# objects
sln = slnparse.parse('sample.sln')
projs = {}
inc_dirs = {}
for pName in sln:
    projs[pName] = minidom.parse( fixpath(pName) )
    inc_dirs[pName] = get_include_dirs( projs[pName] )

print inc_dirs.values()

# cleanup
for pName in sln:
    projs[pName].unlink()


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
