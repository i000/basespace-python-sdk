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

class Coverage:

    def __init__(self):
        self.swaggerTypes = {
            'Chrom': 'str',
            'BucketSize': 'int',
            'MeanCoverage': 'list<int>',
            'EndPos': 'int',
            'StartPos': 'int'
        }
    def __str__(self):
        return 'Chr' + self.Chrom + ": " + str(self.StartPos) + "-" + str(self.EndPos) +\
             ": BucketSize=" + str(self.BucketSize) 
    def __repr__(self):
        return str(self)

        # 
        self.Chrom = None # str

        # Each returned number will represent coverage of this many bases.
        self.BucketSize = None # int

        # 
        self.MeanCoverage = None # list<Str>

        # End position, possibly adjusted to match zoom boundaries
        self.EndPos = None # int

        # Start position, possibly adjusted to match zoom boundaries
        self.StartPos = None # int

