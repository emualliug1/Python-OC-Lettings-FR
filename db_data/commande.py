# python manage.py dumpdata -o backup.json
# python -m json.tool backup.json

import json

with open('backup.json', 'r') as backup:
    parsed = json.load(backup)


with open('new.json', 'w') as new:
    new.write(json.dumps(parsed, indent=4))
