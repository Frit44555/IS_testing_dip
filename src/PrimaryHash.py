import binascii
import hashlib


def primary_hash(text):
    dk = hashlib.pbkdf2_hmac(hash_name='SHA224',
                             password=bytes(text, 'utf-8'),
                             salt=b'0fjsdkfF',
                             iterations=1000)
    # Хеш функция на стороне БД принимает тип text
    return str(binascii.hexlify(dk))[2:-1]
