from pathlib import Path
import base64,gzip,json,hashlib
p=Path(__file__).resolve().parent
manifest=json.loads((p/'manifest.json').read_text())
parts=[]
for i in range(manifest['chunks']):
 s=(p/'assets'/f'replay-{i:03}.js').read_text()
 parts.append(json.loads(s[len('window.N722BD_PARTS.push('):-3]))
raw=gzip.decompress(base64.b64decode(''.join(parts)))
assert hashlib.sha256(raw).hexdigest()==manifest['html_sha256']
(p/'N722BD_standalone.html').write_bytes(raw)
print('Verified standalone HTML:',len(raw),'bytes')
