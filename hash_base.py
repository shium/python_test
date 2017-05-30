#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import base64

mm_1 = 'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'
print base64.decodestring(mm_1)

mm_2 = [u'我们在一起吧', u'我选择原谅你', u'别说话，吻我', u'多喝热水']

for i in mm_2:
    mm = hashlib.new('md5',i.encode('utf-8')).hexdigest()
    print mm
