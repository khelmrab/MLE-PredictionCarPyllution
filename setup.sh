#Construction des images 
docker image pull khedidja/my_project_fastapi:latest
docker image build --no-cache -f Dockerfile.authentication . -t my_authentication_image:latest
docker image build --no-cache -f Dockerfile.prediction . -t my_prediction_image:latest
docker image build --no-cache -f Dockerfile.predictionclassifier . -t my_predictionclassifier_image:latest

#Lancement de docker-compose
docker-compose up

