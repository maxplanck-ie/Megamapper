#!/usr/bin/env python
# megamapper intersector
# by Nikolaus Obholzer, Jan 2012

import sys, re, tempfile, subprocess
import os, shutil
#import pkg_resources; pkg_resources.require( "bx-python" )
#from bx.cookbook import doc_optparse
from galaxy import eggs

def stop_err(msg):
    sys.stderr.write(msg)
    sys.exit()

def main():

    # Handle input params
    in_fname1 = sys.argv[1]
    in_fname2 = sys.argv[2]
    out_file1 = sys.argv[3]
    rscript_path = '/export/local_tools/MegaMapper/candidator.R'

    try:
    #prepare command line 
#        print os.getcwd()

        cmd  = 'Rscript --vanilla %s %s %s %s' %(rscript_path, in_fname1, in_fname2, out_file1 )
#        print cmd # for debugging 
        os.system(cmd)
#        subprocess.Popen(args=cmd, shell=True).wait

    finally:

    # check that there are results in the output file
        if os.path.getsize( out_file1 ) >= 0:
            sys.stdout.write( 'Candidate list compiled.' )
        else:
            stop_err( 'The output file is empty. Your input file may not have had SNPs, or there may be an error with your input file or settings.' )
    
if __name__ == "__main__":
    main()
