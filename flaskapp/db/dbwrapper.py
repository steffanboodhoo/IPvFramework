import db
import json
from pprint import pprint

#!!!!!!!!!!!!!!!!! DONT FORGET TO ADD A STATUS TO EVERYTHING

def findMappingByName(name):
	return_obj = json.dumps(db.QueryMappingByName(name))
	pprint(return_obj)
	return return_obj

def addMapping(ipv4, ipv6, name):
	return_obj = db.AddMapping(ipv4, ipv6, name)
	return return_obj