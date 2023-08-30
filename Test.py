from Crypto.Cipher import AES
import base64
import hashlib
import json

m = hashlib.md5()

def decrypt_aes(text, aes_key, aes_iv):
    encrypt_bytes = base64.b64decode(text)
    aes = AES.new(aes_key.encode('utf-8'), AES.MODE_CBC, aes_iv.encode('utf-8'))
    decrypted_bytes = aes.decrypt(encrypt_bytes)
    return decrypted_bytes.rstrip(b'\0').decode('utf-8')

def encrypt_aes(text, aes_key, aes_iv):
    aes = AES.new(aes_key.encode('utf-8'), AES.MODE_CBC, aes_iv.encode('utf-8'))
    padded_text = text.encode('utf-8') + b'\0' * (AES.block_size - len(text) % AES.block_size)
    encrypted_bytes = aes.encrypt(padded_text)
    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_text

def math_iv(time_stamp):
    time_stamp += time_stamp
    iv_string = ""
    for i in range(len(time_stamp)):
        iv_string += str(int(time_stamp[i]) ** 2)
    iv_string = iv_string.ljust(32, '0')
    return iv_string


# Example usage:
text_to_decrypt = "HUuJjicmo6q0aXspGQh39n4uX1h0eGkCXosem1FMNkczaokvhIRyuBtDB+nWFLmwSjxjT7kCkKnEhM4pYeeSS1cowPfgaqFcRieQycDN0iqfW4yI4Fm58RrWZSgNK4hB4L3Cf8EXtDce61wAVYmkR5KJY5tHJ+nDhibmfDEWvss="  # Put your encrypted text here
text_to_encrypt = '{"TRANS_SN" : "","TRANS" : "1","MEMBER_CODE" : "1610000206","Src" : "c16859a27a3042128fc2d827011a3ecf","TIMESTAMP" : "2023-08-04 16:12:00:72"}'
aes_key = "c16859a27a3042128fc2d827011a3ecf"  # Put your AES key here
aes_iv = "1690946195"  # Put your AES IV here
# 建立 MD5 物件

decrypted_text = decrypt_aes(text_to_decrypt, aes_key, math_iv(aes_iv)[0:16])
#print(json.encoder(text_to_encrypt))
# encrypt_text = encrypt_aes(text_to_encrypt, aes_key, math_iv(aes_iv)[0:16])
# Test = decrypt_aes(encrypt_text, aes_key, math_iv(aes_iv)[0:16])

print(decrypted_text)
# print(encrypt_text)
# print(Test)





