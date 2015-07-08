
import datetime as dt
from pprint import pprint
import pymongo


class QueryTemplate:
    def connect(self):
        try:
            client = pymongo.MongoClient('localhost', 27017)
            db = client['noaa']
            self.collection = db['ocean_data']
        except pymongo.errors.ConnectionFailure:
            raise

    def construct_query(self):
        raise NotImplementedError

    def do_query( self, find=True, update=False ):
        if find==True: self.cursor=self.collection.find(self.query, self.projection)
        if update==True: self.cursor=self.collection.update(self.query)

    def format_results(self):
        raise NotImplementedError





"""
class StationsQuery(QueryTemplate):
    def construct_query( self ):
        # here shall be the query and the proyection
        self.query = {"station_id" : 9440910}
        self.projection = None

    def format_results( self ):
        # here shall be operations over the cursor
        print( self.cursor.count() ) 

    def output_results( self ):
        pass
        #for doc in self.cursor: pprint( doc )



def main():
    o =StationsQuery()
    o.process_format()


if __name__=="__main__":
    main()
"""