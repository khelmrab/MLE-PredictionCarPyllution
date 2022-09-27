FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt . 
COPY modelRandomForestClassifier.pkl .
COPY modelRandomForestRegressor.pkl .
RUN  pip install -r requirements.txt
COPY main.py .
EXPOSE 8000
CMD uvicorn main:api --host 0.0.0.0 --port 8000

