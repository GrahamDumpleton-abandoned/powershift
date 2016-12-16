.PHONY : all

all : src/powershift/resources/types.py src/powershift/endpoints/api.py

src/powershift/resources/types.py : scripts/generate-types.py \
    schemas/openshift-v1-api.json schemas/openshift-v1-oapi.json
	rm -f $@
	python3 scripts/generate-types.py > $@

src/powershift/endpoints/api.py : scripts/generate-api.py \
    schemas/openshift-v1-api.json schemas/openshift-v1-oapi.json
	rm -f $@
	python3 scripts/generate-api.py > $@

install : all
	pip3 install -U .

validate-samples :
	python3 scripts/validate-resources.py samples/all-resources.json

validate-samples-strict :
	OPENSHIFT_API_VALIDATE=true \
	  python3 scripts/validate-resources.py samples/all-resources.json

validate-client :
	python3 examples/list-projects.py
	python3 examples/list-pods.py
	python3 examples/list-public-addresses.py

package :
	python3 setup.py sdist
	python3 setup.py bdist_wheel --python-tag py3

release : clean package
	twine upload dist/*

clean :
	rm -rf build dist powershift.egg-info
