# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:59:52 2020

@author: CEC
"""

import urllib.parse
import  requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Ambato"
dest = "Riobamba"
key = "RbxfdBjmhC5LLRF5Qhu4Nf8kIMOueQNR"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)