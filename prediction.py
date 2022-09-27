import os
import requests

# définition de l'adresse de l'API
api_address = 'my_api_test_from_compose'
# port de l'API
api_port = 80
from requests.auth import HTTPBasicAuth
def verification_version_predictionmodelRandomForestRegressor(username,password,data):
	# requête
	"""r = requests.post(
    		url='http://{address}:{port}/predictionmodelRandomForestRegressor'.format(address=api_address, port=api_port),
    		params= {
    		    	'username': username,
        		'password': password,
			'prediction':prediction
    		}
	)"""
	"""data={}
	data['w'] = w
	data['at1']= at1
	data['at2']=at2
	data['ft']=ft
	data['ec'] = ec
	data['ep']=ep
	data['year']=year"""
	r = requests.post( url='http://{address}:{port}/predictionmodelRandomForestRegressor'.format(address=api_address, port=api_port),json=data, auth=HTTPBasicAuth(username, password))


	output = '''
	============================
    		Content test
	============================

	request done at "/predictionmodelRandomForestRegressor"
	| username={username}
	| password={password}
	|data={data}


	==>  {test_status}

	'''
	print (r.text)

	# statut de la requête
	status_code = r.status_code

	# affichage des résultats
	if status_code == 200:
    		test_status = 'SUCCESS'
	else:
    		test_status = 'FAILURE'
	print(output.format(username=username,password=password,data=data,status_code=status_code, test_status=test_status))

	# impression dans un fichier
	if os.environ.get('LOG') == 1:
    		with open('/home/work/api_test.log', 'a') as file:
		        file.write(output)
verification_version_predictionmodelRandomForestRegressor("alice","wonderland", {"W (mm)": 2456,
  "At1 (mm)": 1441,
  "At2 (mm)": 1434,
  "Ft": 2,
  "ec (cm3)": 999,
  "ep (KW)": 55,
  "year": 2015})
#verification_version_predictionmodelRandomForestRegressor("alice","wonderland",[])
#verification_version_predictionmodelRandomForestRegressor("alice","wonderland",[])
#verification_version_predictionmodelRandomForestRegressor("alice","wonderland","that sucks")

