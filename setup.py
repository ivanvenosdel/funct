#Copyright (C) 2012 Ivan VenOsdel and Nathan Lundquist

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
#(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, 
#merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
#furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
#IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#!/usr/bin/env python

import distutils.core
import sys
# Importing setuptools adds some features like "setup.py develop", but is optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

distutils.core.setup(name='funct',
      version='1.0',
      description='Peachy-keen functional testing utilities.',
      author='Ivan VenOsdel, Nathan Lundquist',
      author_email='',
      url='https://github.com/FrostyFire/funct',
      license="http://opensource.org/licenses/mit-license.php",
      packages = ["funct"],
     )
