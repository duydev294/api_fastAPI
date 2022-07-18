from fastapi import  FastAPI
from mongo import add_message,update_data
from pydantic import BaseModel
app = FastAPI()
class device(BaseModel):
    name:str
@app.get('/device/update_data/{api}')
async def readData(api,data:str):
    add_message(data)
    count = update_data(api,data)
    if count != 0:
        return {"result":"Update success!","Count":count,"message":data}
    else:
        return {"err":"Update data failt!"}
@app.post('/device/create')
async def create_device(newDevice:device):
    if create_device(newDevice.name):
        return {"result":"Create success!"}
    else:
        return {"err":"Create failt!"}