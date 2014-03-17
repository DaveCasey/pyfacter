#!/usr/bin/env python

##############################################################################
# Copyright 2014 Joseph Chilcote
# 
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy
#  of the License at  
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
##############################################################################

import subprocess, sys, json

class Facter(object):
    '''Facter object'''

    def __init__(self):
        p = subprocess.Popen(['facter', '--json'], stdout=subprocess.PIPE)
        p.wait()
        self.data = json.loads(p.stdout.readlines()[0])

    def get(self, key):
        return self.data[key]

    def all(self):
        for k, v in sorted(self.data.items()):
            print "%s: %s" % (k, v)

def main():
    if len(sys.argv) > 2:
        print "Usage: ./pyfacter.py <key>"
        sys.exit(0)
    facts = Facter()
    if len(sys.argv) == 1:
        facts.all()
    elif len(sys.argv) == 2:
        print facts.get(sys.argv[1])

if __name__ == "__main__":
    main()
