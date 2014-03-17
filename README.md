pyfacter.py
=======

This script returns all or specified facts using facter.

Requirements
------------
+ install [facter](http://downloads.puppetlabs.com/mac/)
+ python 2.7  

Standalone
----------
Use pyfacter.py as a standalone script:

	./pyfacter.py [key]

Run with no arguments to return all facts:

	./pyfacter.py

Module
------
Import the module into your python script:

	from pyfacter import Facter

	facts = Facter()
	os_release = facts.get('operatingsystemrelease')
	print os_release
	print facts.all()

References
----------
+ [facter documentation](http://docs.puppetlabs.com/facter/1.7/release_notes.html)


License
-------

	Copyright 2014 Joseph Chilcote
	
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
		http://www.apache.org/licenses/LICENSE-2.0
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
