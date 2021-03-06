#!/usr/bin/python
# -*- coding: utf-8 -*-
# ----------------------------------------------
# Aligot project
#
# Copyright, licence: who cares?
# ----------------------------------------------

# When no cipher specified, all of them will be test in the list order 
# (so let's put the ones with variable-length parameters at the end...)
implementedCiphers = ['tea','xtea','russian_tea','rc4','aes_128_core','md5_core']

class cipherTemplate():

	'''
		Template to define a reference cipher. Each method has to be implemented.
	'''

	def encipher(self, inputText, key):
		
		'''
			Input are passed as hexadecimal strings.
		'''

		raise NotImplementedError("Missing encipher method")

	def decipher(self, inputText, key):
		
		'''
			Input are produced as hexadecimal strings.
		'''

		raise NotImplementedError("Missing decipher medthod")

	def _encode(self, inputText):
		
		'''
			Translate hexadecimal strings in the implementation format.
		'''

		raise NotImplementedError("Missing encoding method")

	def _decode(self, inputText):
		
		'''
			Translate implementation format in to hexadecimal strings.
		'''

		raise NotImplementedError("Missing decoding method")

	def isBlacklistedValue(self, val):

		'''
			Test if a value should not be considered as a parameter,
			because it is a classic values of the cipher (S-BOXs...)
		'''

		raise NotImplementedError("Missing isBlacklistedValue method")

	def getName(self):

		raise NotImplementedError("Missing getName method")

	def getPlaintextLength(self):

		raise NotImplementedError("Missing getPlaintextLength method")

	def getKeyLength(self):

		raise NotImplementedError("Missing getKeyLength method")

	def getCiphertextLength(self):

		raise NotImplementedError("Missing getCiphertextLength method")



