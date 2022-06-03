1. Los archivos *.yaml tienen que compartirse aparte de la imagen docker del proyecto python.
2. Estos no se comparten, ya que se incluyen ya en el proyecto: https://github.com/th39uan60/PythonArquetype
	y debieron haberse aplicado al crear los contenedores de dicho proyecto
	namespace.yaml
	secret.yaml
	
3. Estos tendrán que agregarse como recursos en kubernetes (en orden) usando:
	kubectl apply -f deployment.yaml -n python-arq
	kubectl apply -f service.yaml -n python-arq
	kubectl apply -f ingress.yaml -n python-arq
