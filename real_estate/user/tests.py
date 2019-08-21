import json, subprocess

signed_tx = json.loads(subprocess.getoutput('node ../smartcontract/test.js'))
print(signed_tx['rawTransaction'])
