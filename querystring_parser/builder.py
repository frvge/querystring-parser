# coding: utf-8
'''
Created on 2012-03-28

@author: Tomasz 'Doppler' Najdek

Updated 2012-04-01 Bernard 'berni' Kobos
'''

import urllib.request, urllib.parse, urllib.error
import types

def build(item, encoding=None):
	def recursion(item, base=None):
		pairs = list()
		if(hasattr(item, 'values')):
			for key, value in list(item.items()):
				if encoding:
					quoted_key = urllib.parse.quote(str(key).encode(encoding))
				else:
					quoted_key = urllib.parse.quote(str(key))
				if(base):
					new_base = "%s[%s]" % (base, quoted_key)
					pairs += recursion(value, new_base)
				else:
					new_base = quoted_key
					pairs += recursion(value, new_base)
		elif(isinstance(item, list)):
			for (index, value) in enumerate(item):
				if(base):
					new_base = "%s" % (base)
					pairs += recursion(value, new_base)
				else:
					pairs += recursion(value)
		else:
			if encoding:
				quoted_item = urllib.parse.quote(str(item).encode(encoding))
			else:
				quoted_item = urllib.parse.quote(str(item))
			if(base):
				pairs.append("%s=%s" % (base, quoted_item))
			else:
				pairs.append(quoted_item)
		return pairs
	return '&'.join(recursion(item))
