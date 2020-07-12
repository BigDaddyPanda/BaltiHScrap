# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:41:40 2020

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:29:30 2020

@author: asus
"""

import json
import facebook

def main():
    token = ("EAAJaNr3pdTcBAAAMjetN4ZAh40LZABOdJRZBfzWZBEZAWrOzNUjZC7Wanwgl4sSCgkxlwSw5lD6iYA5ThWAPYDVHD06qIWln19kPPL74PbNjZAwHtLzYDE4YXN9vuDt9KRGWrlJLplZC1ze0FJDLMtpngmCvdc7VTbxXFJX23ljuWmERRhNd92XdewwO18NVk8JgTxQrtCIvf7D6IZAeXq4hpOf9gz5vpPlyJnpMSJVbHrwwasRcAL3ZAFYOvkNQ2E650ZD")
    graph = facebook.GraphAPI(token)
    fields = ['about','name', 'id']
    fields = ','.join(fields)
    
    page = graph.get_object("100701600517312", fields=fields)
    
    print(json.dumps(page, indent=4))
    
if __name__ == "__main__":
    main()