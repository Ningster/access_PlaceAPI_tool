#!/usr/bin/env python
import requests

class PlaceAPI:
    def __init__(self, access_token=None):
        self.access_token=access_token
    def request(self,action,params):
        paraDict = params
        paraDict['key']=self.access_token
        result_json = requests.get('https://maps.googleapis.com/maps/api/place'+action+'/json',params=paraDict)
        result_dict= result_json.json()
        if result_dict['status']=='OK':
            return result_dict
        else:
            try:
                error_message = result_dict["error_message"]
                raise Exception(error_message)
            except Exception as e:
                raise
