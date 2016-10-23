import sys
import json

from openshift3.resources import load, dumps

path = len(sys.argv) >= 2 and sys.argv[1] or None
resources = load(path)

print(repr(resources))

import pprint
pprint.pprint(json.loads(dumps(resources)))
