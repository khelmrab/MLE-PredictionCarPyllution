import os
import requests

# définition de l'adresse de l'API
api_address = 'my_api_test_from_compose'
#'my_api_test_from_compose'
# port de l'API
api_port = 80
from requests.auth import HTTPBasicAuth

def verification_permissions(username,password):
	# requête
	r = requests.get( url='http://{address}:{port}/user'.format(address=api_address, port=api_port), auth=HTTPBasicAuth(username, password))
	output = '''
	============================
    		Authentication test
	============================

	request done at "/login
	| username={username}
	| password={password}

	==>  {test_status}

	'''


	# statut de la requête

	status_code = r.status_code
	# affichage des résultats
	if status_code == 200:
    		test_status = 'SUCCESS'
	else:
    		test_status = 'FAILURE'
	print(output.format(username=username,password=password,status_code=status_code, test_status=test_status))
	#print(output.format(status_code=status_code, test_status=test_status))

	# impression dans un fichier
	if os.environ.get('LOG') == 1:
    		with open('/home/work/api_test.log', 'a') as file:
		        file.write(output)
verification_permissions("alice","data")
verification_permissions("bob","builder")
verification_permissions("clementine","fauxpassword")

