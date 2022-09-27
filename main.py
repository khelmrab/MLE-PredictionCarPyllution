import os
import pandas as pd
import numpy as np
import uvicorn
from pydantic import BaseModel,Field
import pickle
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

# la class  car pollution 

class CarPyllution(BaseModel):
    w: float = Field(alias='W (mm)')
    at1: float = Field(alias='At1 (mm)')
    at2: float = Field(alias='At2 (mm)')
    Ft: float
    ec: float = Field(alias='ec (cm3)')
    ep: float = Field(alias='ep (KW)')
    year: int

## Chargement des fichiers des modeles
modelRandomForestRegressor=pickle.load(open('modelRandomForestRegressor.pkl','rb'))
modelRandomForestClassifier=pickle.load(open('modelRandomForestClassifier.pkl','rb'))


api = FastAPI(
    title="Prediction Car Pollution",
    description="My project API to predict car pollution with modelRandomForestRegressor / modelRandomForestClassifier",
    version="1.0.0")

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users = {

    "alice": {
        "username": "alice",
        "hashed_password": pwd_context.hash('wonderland'),
    },
    "bob" : {
        "username" :  "bob",
        "hashed_password" : pwd_context.hash('builder'),
    },
    "clementine" : {
        "username" :  "clementine",
        "hashed_password" : pwd_context.hash('mandarine'),
    }
}
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    if not(users.get(username)) or not(pwd_context.verify(credentials.password, users[username]['hashed_password'])):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@api.get('/', name = "index")
def get_index():
    """Returns greetings
    """
    return {'greetings': 'Welcome'}


@api.get('/status', name = 'return status "OK" quand api marche')
def get_status():
    """Vérification que l'API est bien fonctionnelle si le status est return Ok
    """
    return {'status': 'OK'}


@api.get("/user")
def current_user(username: str = Depends(get_current_user)):
    return "Hello {}".format(username)


@api.post('/predictionmodelRandomForestRegressor')
def post_prediction(data:CarPyllution, username: str = Depends(get_current_user)):
    data = data.dict()
    w=data['w']
    at1=data['at1']
    at2=data['at2']
    ft=data['Ft']
    ec=data['ec']
    ep=data['ep']
    year=data['year']
    prediction = modelRandomForestRegressor.predict([[w,at1,at2,ft,ec,ep,year]]).tolist()
    return {"Prediction Enedc (g/km)": prediction}


@api.post('/predictionmodelRandomForestClassifier')
def predict_car_pollution(data: CarPyllution,  username: str = Depends(get_current_user)):
    data = data.dict()
    w=data['w']
    at1=data['at1']
    at2=data['at2']
    ft=data['Ft']
    ec=data['ec']
    ep=data['ep']
    year=data['year']
    prediction = modelRandomForestClassifier.predict([[w,at1,at2,ft,ec,ep,year]]).tolist()
    return {"Class prediction": prediction[0]}



# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)
#uvicorn main:api --reload

