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

class CoverageMetadata:

    def __init__(self):
        self.swaggerTypes = {
            'MaxCoverage': 'int',
            'CoverageGranularity': 'int'
        }
    def __str__(self):
        return "CoverageMeta: max=" + str(self.MaxCoverage) + " gran=" + str(self.CoverageGranularity)
    def __repr__(self):
        return str(self)


        # Maximum coverage value of any base, on a per-base level, for the entire chromosome. Useful for scaling
        self.MaxCoverage = None # int


        # Supported granularity of queries
        self.CoverageGranularity = None # int

