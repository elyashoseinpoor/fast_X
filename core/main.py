#libraris
from fastapi import FastAPI,Query,HTTPException,status,Path,Form,Body,UploadFile
import random
import colorama
from fastapi.responses import JSONResponse
from typing import Optional


#for_color's
colorama.init()

#main_object
app = FastAPI()


#my_data_base
name_list_example = [
    {"id":1 ,"name":"ghasem"},
    {"id":2 ,"name":"hamed"},
    {"id":3 ,"name":"saber"},
    {"id":4 ,"name":"kazem"},
    {"id":5 ,"name":"jaber"},
]



#opration_1
@app.get("/")
def elyasjoon():
    return JSONResponse(content={"message","hello world!"},status_code=status.HTTP_202_ACCEPTED)

#opration_2
@app.get("/names")
def name_list():
    return name_list_example

#opration_3
@app.get("/names/{item_id}")
def names_detail(item_id: int = Path()):
    for name in name_list_example:
        if name["id"] == item_id:
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")

#opration_4
@app.post("/names",status_code=status.HTTP_201_CREATED)
def names_create(name: str):
    new_name = {"id": random.randint(1,1000), "name": name}
    name_list_example.append(new_name)
    return new_name

#opration_5
@app.put("/names/{item_id}",status_code=status.HTTP_200_OK)
def names_update(item_id: int, name: str):
    for n in name_list_example:
        if n["id"] == item_id:
            n["name"] = name
            return {"message": f"Name with ID {item_id} updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")


#opration_6
@app.delete("/names/{item_id}",status_code=status.HTTP_204_NO_CONTENT)
def names_delete(item_id: int):
    for n in name_list_example:
        if n["id"] == item_id:
            name_list_example.remove(n)
            return JSONResponse(content={"message": f"Name with ID {item_id} deleted successfully"},status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")

#search_1
@app.get("/search")
def search_jaber(q=None):
    print("q =", q)
    if q:
        for i in name_list_example:
            if i["name"] == q:
                return i
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")

#search_2
@app.get("/search2/")
async def read_items(
    q: Optional[str] = Query(None, min_length=1)
):
    result = []

    if q:
        for i in name_list_example:
            if q.lower() in i["name"].lower():
                result.append(i)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")