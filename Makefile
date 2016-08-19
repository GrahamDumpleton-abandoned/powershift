.PHONY : all validate

all : src/openshift3/resources/types.py

src/openshift3/resources/types.py : scripts/generate-types.py \
    schemas/openshift-v1-api.json schemas/openshift-v1-oapi.json
	rm -f $@
	python3 scripts/generate-types.py > $@

install :
	python3 setup.py install

validate :
	python3 scripts/validate-resources.py samples/all-resources.json
