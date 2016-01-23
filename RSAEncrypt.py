from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

class RSAEnrcyption(object):

    def generate_RSA(self,bits=2048):

        '''
        Generate an RSA keypair with an exponent of 65537 in PEM format
        param: bits The key length in bits
        Return private key and public key
        '''

        self.new_key = RSA.generate(bits, e=65537)
        self.public_key = self.new_key.publickey().exportKey("PEM")
        self.private_key = self.new_key.exportKey("PEM")
        return self.private_key, self.public_key

    def encrypt_RSA(self,public_key, message):

        '''
        param: public_key_loc Path to public key
        param: message String to be encrypted
        return base64 encoded encrypted string
        '''
        self.msg = message
        self.key = public_key
        self.rsakey = RSA.importKey(self.key)
        rsakey = PKCS1_OAEP.new(self.rsakey)
        self.encrypted = rsakey.encrypt(self.msg)
        return self.encrypted.encode('base64')


    def decrypt_RSA(self,private_key, package):

        '''
        param: public_key_loc Path to your private key
        param: package String to be decrypted
        return decrypted string
        '''

        self.key = private_key
        self.rsakey = RSA.importKey(self.key)
        self.rsakey = PKCS1_OAEP.new(self.rsakey)
        self.str = package.replace(" ","+")
        decrypted = self.rsakey.decrypt(b64decode(self.str))
        return decrypted


