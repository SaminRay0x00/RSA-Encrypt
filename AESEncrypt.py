import base64
from Crypto.Cipher import AES


class AESCrypto():

    BLOCK_SIZE = 32
    PADDING='#'

    def _pad(self,data, pad_with=PADDING):
        """
        Data to be encrypted should be on 16, 24 or 32 byte boundaries.
        So if you have 'hi', it needs to be padded with 30 more characters
        to make it 32 bytes long. Similary if something is 33 bytes long,
        31 more bytes are to be added to make it 64 bytes long which falls
        on 32 boundaries.
        - BLOCK_SIZE is the boundary to which we round our data to.
        - PADDING is the character that we use to padd the data.
        """
        return data + (self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE) * self.PADDING

    def encrypt(self,secret_key, data):
        """
        Encrypts the given data with given secret key.
        """
        cipher = AES.new(self._pad(secret_key, '@')[:32])
        return base64.b64encode(cipher.encrypt(self._pad(data)))

    def decrypt(self,secret_key, encrypted_data):
        """
        Decryptes the given data with given key.
        """
        cipher = AES.new(self._pad(secret_key, '@')[:32])
        return cipher.decrypt(base64.b64decode(encrypted_data)).rstrip(self.PADDING)

'''
KEY='a`123456'
decrypted =  encrypt(KEY, 'ramin')
print decrypted
print decrypt(KEY, decrypted)
'''

