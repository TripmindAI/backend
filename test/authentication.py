from authlib.jose import JsonWebToken


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
jwt = JsonWebToken(['RS256'])
public_key = read_file('../publickey.pem')

token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InI4V3F2RDlLLTJ4azlHYnRiUHVxZiJ9.eyJnaXZlbl9uYW1lIjoiUkYiLCJmYW1pbHlfbmFtZSI6IlgiLCJuaWNrbmFtZSI6InhyZnhyZnhyZnhyZnhyZiIsIm5hbWUiOiJSRiBYIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tEbHVYbUozVDZ6VTdPTWN3SEhLRGpFN2h4Y3R1RVFGNFRtaHNpMGZGZD1zOTYtYyIsImxvY2FsZSI6InpoLUNOIiwidXBkYXRlZF9hdCI6IjIwMjQtMDMtMDNUMjA6MTM6NTAuMjEyWiIsImVtYWlsIjoieHJmeHJmeHJmeHJmeHJmQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL3RyaXBtaW5kYWkudXMuYXV0aDAuY29tLyIsImF1ZCI6IjhPeXl1THRBZFdmWlVhbzVLdk9qajFJUDlrZG4wZFBMIiwiaWF0IjoxNzA5NDk2ODMxLCJleHAiOjE3MDk1MzI4MzEsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2NDIyOTgwMDk5Mzg3NTcxNjk3Iiwic2lkIjoiQktUTFV4NUJnejZ6Q05zd2FzX2VjNS1QZzlHbEU3YkUiLCJub25jZSI6IjlvUzZxYzBBVWhPM0xpTjA0c0FKcnVkZi1HNElQZEY4eVJ1MjFhUjg0dEEifQ.KCiw7Ck83zB7aMqdeX5OC_IZE0zwnUsRTErb5qgkBU2DV8LAkD6iH4uWyUnTKCeQz7s63ZjUY1JalOjufKb9ASwdz176Icu3fhSikqc3phAcmHP1gyZfdwR3i-Wy8jUxYkP_PVUWovuKz-nX_hx-gi8PqOAX_8Do0TyMDO00mQPZdMscPFoGbR0cQoaKkkntGRjhO5WWJ82ltWXz61G6oJpX_a348Yw2CEbO4SMYyussXk995v9Q_EJWW7PquiAhK5N60kShiuTvDwfJWkjK6-oWPuat903i0cCiYrsweArB3_In-SszCGlVVoc3deUwjsh3m4DEcISmwUaCIqeHaQ'
claims = jwt.decode(token, public_key)
print(claims)


