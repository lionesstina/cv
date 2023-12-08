#!/usr/bin/env python3
import re

from generate_utils import OutFile

for filename in ('cv.html', 'cv-edu.html'):
  base = filename.split('.')[0]
  with open(f'{base}.html') as f:
    s = f.read();

  R = re.compile('{{(.*?)\|(.*?)}}', re.DOTALL)

  for i, lang in enumerate(('fr', 'en')):
    with OutFile(f'{base}.{lang}.html', 'w') as f:
        f.write(R.sub(lambda m: m.group(i+1), s))
