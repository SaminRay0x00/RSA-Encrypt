from RSAEncrypt import RSAEnrcyption


## Generator KEYS (publick_KEY,Private_KEY)

class PublicKEY(object):

    private_KEY = 0
    def public(self):

        KEYS = RSAEnrcyption().generate_RSA()
        public_key = KEYS[1]
        global private_KEY
        private_KEY = KEYS[0]
        text = "Hi Ramin ! This is a test"
        MessgeEncrypt = RSAEnrcyption().encrypt_RSA(public_key,str(text))
        return MessgeEncrypt

class PrivateKEY(object):

    def private(self):

            obj = PublicKEY().public()
            MessageDecryptRSA = RSAEnrcyption().decrypt_RSA(private_KEY,obj)
            return MessageDecryptRSA

objencrypt = PublicKEY().public()
print objencrypt

print  "#############################################DeCrypt###########################################"

objdecrypt = PrivateKEY().private()
print objdecrypt







