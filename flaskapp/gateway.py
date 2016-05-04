from db import dbwrapper as db
from nat import natwrapper as nat

def findMappingByName(name):
	return db.findMappingByName(name)

def addMapping(ipv4, ipv6, name):
	return db.addMapping(ipv4, ipv6, name)

