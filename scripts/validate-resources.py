import sys
import json

from powershift.resources import load, dumps

path = len(sys.argv) >= 2 and sys.argv[1] or None
resources = load(path)

print(repr(resources))

import pprint
pprint.pprint(json.loads(dumps(resources)))
