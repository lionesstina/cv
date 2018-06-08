#!/usr/bin/env python3
import re

from generate_utils import OutFile

with open('cv.html') as f:
    s = f.read();

R = re.compile('{{(.*?)\|(.*?)}}', re.DOTALL)

for i, lang in enumerate(('fr', 'en')):
    with OutFile('cv.{}.html'.format(lang), 'w') as f:
        f.write(R.sub(lambda m: m.group(i+1), s))
