"""
Copyright 2012 Illumina

    Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from BaseSpacePy.api.BaseSpaceAPI import BaseSpaceAPI
import os
import helper 

"""
This script demonstrates basic browsing of BaseSpace objects once an access-token
for global browsing has been obtained. 
"""

# FILL IN WITH YOUR APP VALUES HERE!
client_key                 = ""
client_secret              = ""
AppSessionId               = ""
accessToken                = ""
# test if client variables have been set
helper.checkClientVars({'client_key':client_key,'client_secret':client_secret,'AppSessionId':AppSessionId}) 

BaseSpaceUrl               = 'https://api.cloud-endor.illumina.com/'
version                    = 'v1pre3'

# First, create a client for making calls for this user session 
myAPI   = BaseSpaceAPI(client_key, client_secret, BaseSpaceUrl, version, AppSessionId,AccessToken=accessToken)

# First, let's grab the genome with id=4
myGenome    = myAPI.getGenomeById('4')
print "\nThe Genome is " + str(myGenome)
print "We can get more information from the genome object"
print 'Id: ' + myGenome.Id
print 'Href: ' + myGenome.Href
print 'DisplayName: ' + myGenome.DisplayName

# Get a list of all genomes
allGenomes  = myAPI.getAvailableGenomes()
print "\nGenomes \n" + str(allGenomes)

# Let's have a look at the current user
user        = myAPI.getUserById('current')
print "\nThe current user is \n" + str(user)

# Now list the projects for this user
myProjects   = myAPI.getProjectByUser('current')
print "\nThe projects for this user are \n" + str(myProjects)

# We can also achieve this by making a call using the 'user instance'
myProjects2 = user.getProjects(myAPI)
print "\nProjects retrieved from the user instance \n" + str(myProjects2)

# List the runs available for the current user
runs = user.getRuns(myAPI)
print "\nThe runs for this user are \n" + str(runs)

# In the same manner we can get a list of accessible user runs
runs = user.getRuns(myAPI)
print "\nRuns retrieved from user instance \n" + str(runs)