from random import random
import uuid
import string
import random
import datetime
def random_uuid():
    return(uuid.uuid1())
def randomid_Dvid(id):
    uuidRandom = random_uuid()
    return id + "-"+ str(uuidRandom)
def random_N_Crt(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
def date_convert():
    now = datetime.datetime.now()
    return str(now.year) + str(now.month)+str(now.day)