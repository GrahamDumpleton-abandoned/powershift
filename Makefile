.PHONY : all validate

all : src/powershift/resources/types.py src/powershift/endpoints/api.py

src/powershift/resources/types.py : scripts/generate-types.py \
    schemas/openshift-v1-api.json schemas/openshift-v1-oapi.json
	rm -f $@
	python3 scripts/generate-types.py > $@

src/powershift/endpoints/api.py : scripts/generate-api.py \
    schemas/openshift-v1-api.json schemas/openshift-v1-oapi.json
	rm -f $@
	python3 scripts/generate-api.py > $@

package :
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal

install : all
	pip3 install -U .

validate :
	python3 scripts/validate-resources.py samples/all-resources.json

validate-strict :
	OPENSHIFT_API_VALIDATE=true \
	  python3 scripts/validate-resources.py samples/all-resources.json

clean :
	rm -rf build dist powershift.egg-info
