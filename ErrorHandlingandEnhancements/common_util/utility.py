from schema import Schema, And, Use, SchemaError
from common_util.config import *
#Write code here for exception handling



def exceptions(raw_features):
    if len(raw_features) != len(rawfields):
        return [1,"Missing Input Features"]

    for k,v in raw_features.items():
        try:
            float(v)
        except:
            return [1,"Input of {} can only be Number".format(k)]
    
    return [0,""]