#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf8'))
sha1.update('python hashlib?'.encode('utf8'))
print(sha1.hexdigest())
