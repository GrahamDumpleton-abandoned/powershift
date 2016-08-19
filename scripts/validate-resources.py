import sys
import json

from openshift3.resources import load, dumps

resources = load(sys.argv[1])
print(repr(resources))

import pprint
pprint.pprint(json.loads(dumps(resources)))
