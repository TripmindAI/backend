from authlib.jose import JsonWebToken
import base64


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def decodeJWT(token:str):
    jwt = JsonWebToken(['RS256'])
    public_key = read_file('../../publickey.pem')
    claims = jwt.decode(token, public_key)
    print(claims)
    return claims
