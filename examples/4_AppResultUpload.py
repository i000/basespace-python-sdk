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
import helper #@UnresolvedImport

"""
This script demonstrates how to create a new AppResults object, change its state
and upload result files to it and download files from it.  
"""
# FILL IN WITH YOUR APP VALUES HERE!
client_key                 = ""
client_secret              = ""
AppSessionId               = ""
accessToken                = ""
# test if client variables have been set
helper.checkClientVars({'client_key':client_key,'client_secret':client_secret,'AppSessionId':AppSessionId}) 

BaseSpaceUrl               = 'https://api.cloud-endor.illumina.com'
version                    = 'v1pre3'

# First, create a client for making calls for this user session 
myBaseSpaceAPI   = BaseSpaceAPI(client_key, client_secret, BaseSpaceUrl, version, AppSessionId,AccessToken=accessToken)


# Now we'll do some work of our own. First get a project to work on
# we'll need write permission, for the project we are working on
# meaning we will need get a new token and instantiate a new BaseSpaceAPI  
p = myBaseSpaceAPI.getProjectById('89')

# Assuming we have write access to the project
# we will list the current App Results for the project 
appRes = p.getAppResults(myBaseSpaceAPI,statuses=['Running'])
print "\nThe current running AppResults are \n" + str(appRes)

# now let's do some work!
# to create an appResults for a project, simply give the name and description
appResults = p.createAppResult(myBaseSpaceAPI,"testing","this is my results",appSessionId='')
print "\nSome info about our new app results"
print appResults
print appResults.Id
print "\nThe app results also comes with a reference to our AppSession"
myAppSession = appResults.AppSession
print myAppSession

# we can change the status of our AppSession and add a status-summary as follows
myAppSession.setStatus(myBaseSpaceAPI,'needsattention',"We worked hard, but encountered some trouble.")
print "\nAfter a change of status of the app sessions we get\n" + str(myAppSession)
# we'll set our appSession back to running so we can do some more work
myAppSession.setStatus(myBaseSpaceAPI,'running',"Back on track")


### Let's list all AppResults again and see if our new object shows up 
appRes = p.getAppResults(myBaseSpaceAPI,statuses=['Running'])
print "\nThe updated app results are \n" + str(appRes)
appResult2 = myBaseSpaceAPI.getAppResultById(appResults.Id)
print appResult2

## Now we will make another AppResult 
## and try to upload a file to it
appResults2 = p.createAppResult(myBaseSpaceAPI,"My second AppResult","This one I will upload to")
appResults2.uploadFile(myBaseSpaceAPI, '/home/mkallberg/Desktop/testFile2.txt', 'BaseSpaceTestFile.txt', '/mydir/', 'text/plain')
print "\nMy AppResult number 2 \n" + str(appResults2)

## let's see if our new file made it
appResultFiles = appResults2.getFiles(myBaseSpaceAPI)
print "\nThese are the files in the appResult"
print appResultFiles
f = appResultFiles[-1]

# we can even download our newly uploaded file
f = myBaseSpaceAPI.getFileById(f.Id)
f.downloadFile(myBaseSpaceAPI,'/home/mkallberg/Desktop/')