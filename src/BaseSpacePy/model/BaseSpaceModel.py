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

class BaseSpaceModel:
    
    def __init__(self):
        #to be overriden
        self.Id = ''
        pass

    def __str__(self):
        self.isInit()
        return self.Id
    
    def __repr__(self):
        return str(self)
    
    def isInit(self):
        return 1
    
    def setAPI(self,api):
        self.api = api