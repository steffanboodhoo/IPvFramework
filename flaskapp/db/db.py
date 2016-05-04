from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pprint import pprint


db = create_engine('mysql://root:admin@127.0.0.1/IPv',echo=True)
Base = declarative_base()

class Mapping(Base):
	__tablename__ = 'mapping'
	id = Column(Integer, primary_key=True)
	ipv4 = Column(String(30))
	ipv6 = Column(String(30))
	name = Column(String(60))

	def __init__(self, ipv4, ipv6, name):
		self.ipv4 = ipv4
		self.ipv6 = ipv6
		self.name = name

	def __repr__(self):
		return "<Mapping(ipv4='%s', ipv6='%s', name='%s')>" % (self.ipv4, self.ipv6, self.name)



def CreateTables():
	Base.metadata.create_all(db)

def AddMapping(ipv4, ipv6, name):
	session = sessionmaker(bind=db)
	session = session()
	new_mapping = Mapping(ipv4, ipv6, name)
	session.add(new_mapping)
	session.commit()
	return "success"

def QueryMappingByName(key_name):
	session = sessionmaker(bind=db)
	session = session()
	data_obj = []
	for instance in session.query(Mapping).filter(Mapping.name.like('%'+key_name+'%')):
		data_obj.append({'name':instance.name, 'ipv4':instance.ipv4, 'ipv6':instance.ipv6})
	
	pprint(data_obj)
	return data_obj


if __name__ == '__main__':
	QueryMapping("sang")