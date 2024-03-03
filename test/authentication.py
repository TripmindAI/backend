from authlib.jose import JsonWebToken


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
jwt = JsonWebToken(['RS256'])
public_key = read_file('../publickey.pem')

token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InI4V3F2RDlLLTJ4azlHYnRiUHVxZiJ9.eyJnaXZlbl9uYW1lIjoiUkYiLCJmYW1pbHlfbmFtZSI6IlgiLCJuaWNrbmFtZSI6InhyZnhyZnhyZnhyZnhyZiIsIm5hbWUiOiJSRiBYIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tEbHVYbUozVDZ6VTdPTWN3SEhLRGpFN2h4Y3R1RVFGNFRtaHNpMGZGZD1zOTYtYyIsImxvY2FsZSI6InpoLUNOIiwidXBkYXRlZF9hdCI6IjIwMjQtMDMtMDNUMjA6MTM6NTAuMjEyWiIsImVtYWlsIjoieHJmeHJmeHJmeHJmeHJmQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL3RyaXBtaW5kYWkudXMuYXV0aDAuY29tLyIsImF1ZCI6IjhPeXl1THRBZFdmWlVhbzVLdk9qajFJUDlrZG4wZFBMIiwiaWF0IjoxNzA5NDk2ODMxLCJleHAiOjE3MDk1MzI4MzEsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2NDIyOTgwMDk5Mzg3NTcxNjk3Iiwic2lkIjoiQktUTFV4NUJnejZ6Q05zd2FzX2VjNS1QZzlHbEU3YkUiLCJub25jZSI6IjlvUzZxYzBBVWhPM0xpTjA0c0FKcnVkZi1HNElQZEY4eVJ1MjFhUjg0dEEifQ.KCiw7Ck83zB7aMqdeX5OC_IZE0zwnUsRTErb5qgkBU2DV8LAkD6iH4uWyUnTKCeQz7s63ZjUY1JalOjufKb9ASwdz176Icu3fhSikqc3phAcmHP1gyZfdwR3i-Wy8jUxYkP_PVUWovuKz-nX_hx-gi8PqOAX_8Do0TyMDO00mQPZdMscPFoGbR0cQoaKkkntGRjhO5WWJ82ltWXz61G6oJpX_a348Yw2CEbO4SMYyussXk995v9Q_EJWW7PquiAhK5N60kShiuTvDwfJWkjK6-oWPuat903i0cCiYrsweArB3_In-SszCGlVVoc3deUwjsh3m4DEcISmwUaCIqeHaQ'
claims = jwt.decode(token, public_key)
print(claims)


# import jwt
# public_key=b"""
# -----BEGIN PUBLIC KEY-----
# MIIDCTCCAfGgAwIBAgIJdV9BrU3E85S8MA0GCSqGSIb3DQEBCwUAMCIxIDAeBgNV
# BAMTF3RyaXBtaW5kYWkudXMuYXV0aDAuY29tMB4XDTI0MDIxMzIyMTgwNFoXDTM3
# MTAyMjIyMTgwNFowIjEgMB4GA1UEAxMXdHJpcG1pbmRhaS51cy5hdXRoMC5jb20w
# ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCVEt8TUEuMLU94EQhuB8Ns
# sAH+zKKEFwgbwbFs/9ovlhgJWyLGnB2pOC9jIZqSnDTyOwGSg95RyS69wkjWR02/
# 4DwzeelVToPrTrM7W6Uyqj3e4BtFpg0HohbhG2Nvx+E1u2aAMi4gONHAmNyR3wrm
# /jobHBee07C7ww2oAIqbo2heUvgsNpJDtSZHoplAzhs7Dt63G58me7VweR2WE1d2
# Zaytcov0KJPgrsqKUSnKIhojLM/mhgemm94pCKepNH3b8LAFhtJB6f6NnAESfkgv
# Rxb2I7jRPq46y792f5E6wpx7OVwSKJmSqGHiqJVp5MxdTJDm6vqXqV6+BmeV1TzD
# AgMBAAGjQjBAMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFO7UlZEiqIR1Wpag
# IYDgAydhZwFfMA4GA1UdDwEB/wQEAwIChDANBgkqhkiG9w0BAQsFAAOCAQEAf2qq
# C+RJK7J90YFZ5BuV0HoorT6+WAAyzZGsJQwgEKV7u5XvQ8NYYTN/UDAf+FoVpLEp
# Nv18OEXlQ8kHjgsZa2mRKANLWLl5V12o9fsXUeQnXa8ApGnXqUe5JOHc73cRtg2c
# U7LwE/UHG0HArPl5NjkQcU4ZlKqhclzzBVZBfaf0Udai3YjhacCYt9JfBv3/2Rh9
# iWUNx2xyYGthVroUJ7wYWEvF/6nKAzRmc1fYJy5/Qd9dzwkKLgXhvCNz15iTquBY
# Tj5qrP97JVrn0b/aASPoG4fEzlDJ10v5Ah+GpEJ6hxb3phYv6owUGWo4UBziOI9Y
# RtE5WrYWcBVk9YykpQ==
# -----END PUBLIC KEY-----
# """
# token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InI4V3F2RDlLLTJ4azlHYnRiUHVxZiJ9.eyJnaXZlbl9uYW1lIjoiUkYiLCJmYW1pbHlfbmFtZSI6IlgiLCJuaWNrbmFtZSI6InhyZnhyZnhyZnhyZnhyZiIsIm5hbWUiOiJSRiBYIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tEbHVYbUozVDZ6VTdPTWN3SEhLRGpFN2h4Y3R1RVFGNFRtaHNpMGZGZD1zOTYtYyIsImxvY2FsZSI6InpoLUNOIiwidXBkYXRlZF9hdCI6IjIwMjQtMDMtMDNUMjA6MTM6NTAuMjEyWiIsImVtYWlsIjoieHJmeHJmeHJmeHJmeHJmQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL3RyaXBtaW5kYWkudXMuYXV0aDAuY29tLyIsImF1ZCI6IjhPeXl1THRBZFdmWlVhbzVLdk9qajFJUDlrZG4wZFBMIiwiaWF0IjoxNzA5NDk2ODMxLCJleHAiOjE3MDk1MzI4MzEsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2NDIyOTgwMDk5Mzg3NTcxNjk3Iiwic2lkIjoiQktUTFV4NUJnejZ6Q05zd2FzX2VjNS1QZzlHbEU3YkUiLCJub25jZSI6IjlvUzZxYzBBVWhPM0xpTjA0c0FKcnVkZi1HNElQZEY4eVJ1MjFhUjg0dEEifQ.KCiw7Ck83zB7aMqdeX5OC_IZE0zwnUsRTErb5qgkBU2DV8LAkD6iH4uWyUnTKCeQz7s63ZjUY1JalOjufKb9ASwdz176Icu3fhSikqc3phAcmHP1gyZfdwR3i-Wy8jUxYkP_PVUWovuKz-nX_hx-gi8PqOAX_8Do0TyMDO00mQPZdMscPFoGbR0cQoaKkkntGRjhO5WWJ82ltWXz61G6oJpX_a348Yw2CEbO4SMYyussXk995v9Q_EJWW7PquiAhK5N60kShiuTvDwfJWkjK6-oWPuat903i0cCiYrsweArB3_In-SszCGlVVoc3deUwjsh3m4DEcISmwUaCIqeHaQ'
# res=jwt.decode(token, public_key, algorithms=["RS256"])
# print(res)
