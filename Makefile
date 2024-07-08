

getenv:
	virtualenv ./env

install :
	. env/bin/activate; pip install -r requirements.txt

add :
	. env/bin/activate; pip install $(pkg) ; pip freeze | grep $(pkg) >> requirements.txt

run:
	. env/bin/activate; python pylet.py
	python pylet.py $(prompt)


getmodel:
	git lfs install
	git clone https://huggingface.co/Markhit/CodeLlama3-8B-Python

lint :
	. env/bin/activate; pylint *.py

format :
	. env/bin/activate; black *.py