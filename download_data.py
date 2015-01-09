# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:26:40 2015

@author: damienrj
"""

import urllib
import time
secs = 2
urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atusresp_0313.zip", "./data/atusresp_0313.zip")
time.sleep(secs)
print("Download 1 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atusrost_0313.zip", "./data/atusrost_0313.zip")
time.sleep(secs)
print("Download 2 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atusact_0313.zip", "./data/atusact_0313.zip")
time.sleep(secs)
print("Download 3 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atussum_0313.zip", "./data/atussum_0313.zip")
time.sleep(secs)
print("Download 4 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atuswho_0313.zip", "./data/atuswho_0313.zip")
time.sleep(secs)
print("Download 5 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atuscps_0313.zip", "./data/atuscps_0313.zip")
time.sleep(secs)
print("Download 6 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atusrostec_1113.zip", "./data/atusrostec_1113.zip")
time.sleep(secs)
print("Download 7 done")

urllib.urlretrieve ("http://www.bls.gov/tus/special.requests/atuswgts_0313.zip", "./data/atuswgts_0313.zip")
time.sleep(secs)
print("Downloading done")