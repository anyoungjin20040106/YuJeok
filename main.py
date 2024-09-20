from fastapi import FastAPI,Form
import pandas as pd
from fastapi.staticfiles import StaticFiles
app=FastAPI()
app.mount("/img",StaticFiles(directory="image"))
df=pd.read_json('data.json')
@app.post("/yujeck")
def yujeock(name:str=Form(...)):
    tf=df[df['이름']==name].copy()
    tf.rename(columns={'이름':'name','설명':'info'},inplace=True)
    return tf.to_dict('records')