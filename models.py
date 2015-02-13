from google.appengine.ext import ndb

class Transaction(ndb.Model):
    """A simple model to store the properties of an order"""
    total_amount = ndb.FloatProperty(indexed=False)
    transaction_id = ndb.StringProperty(indexed=False)
    transaction_ref = ndb.StringProperty(indexed=False)
    post_date = ndb.StringProperty(indexed=False)
    payment_id = ndb.StringProperty(indexed=True)
    authorization_code = ndb.StringProperty(indexed=False)
    result = ndb.StringProperty(indexed=False)
    udf1 = ndb.StringProperty(indexed=False)
    udf2 = ndb.StringProperty(indexed=False)
    udf3 = ndb.StringProperty(indexed=False)
    udf4 = ndb.StringProperty(indexed=False)
    udf5 = ndb.StringProperty(indexed=False)