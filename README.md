# Food Tech Challenge FIAP
## Lambda de autenticação

Esse componente serve para autenticar os usuários que irão acessar nosso serivdor antes de processarmos a requisição no EKS.

A requisição é feita via API Gateway e retorna um token JWT.

## Auth
**Endpoint:** *https://*****1w3li.execute-api.us-east-2.amazonaws.com/HK/lambda_Auth*<br />
**Método:** *POST*

**Request Example:** 
<br />
```json
{
  "body": {
    "username": "12345233910",
    "password": "Techfi444"
  }
}
```
**Response Example:** 
```json
{
    "statusCode": 200,
    "body": "{\"token\": \"eyJraWQiOiJjR1hjR2NvVnhodTVJMW5pYU9YM2t5RnlneVBWbjJ6Ym10M3RFMHFpTTJjPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI1YWMxYjY5ZS1jM2VlLTRkNjctOTA4Mi05MTg5NDcyYzVmZWEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMi5hbWF6b25hd3MuY29tXC91cy1lYXN0LTJfb05VZUM5M1hkIiwiY29nbml0bzp1c2VybmFtZSI6IjEyMzQ1Njc4OTEwIiwib3JpZ2luX2p0aSI6IjhmNjYxOGQxLTNhM2MtNGU1ZS04OWU4LWZiYjY5YjI2NGI3YSIsImF1ZCI6InY3MTRxamZzdHVlbG1pNmJuYmdwOWpsYzIiLCJldmVudF9pZCI6Ijk4ZjliZTNiLTVmMDgtNGE4Mi04YTAyLTUxZWZlNmIzNThkOCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzEwODkyMTI5LCJleHAiOjE3MTA4OTU3MjksImlhdCI6MTcxMDg5MjEyOSwianRpIjoiOWEwMWVkMzItZTYxMy00ZGQ0LTgzZmYtMjZiZDVjOWI5YWRmIiwiZW1haWwiOiJndWlsaGVybWVwY3N0b3JlQGdtYWlsLmNvbSJ9.E3kRkpGQdOTzPOq8hMFllm3N7LW24KvQiwTfMmMtcKN6ZKJPXooJysbT5NuQu8ut3fOLVjc33E6B7oDqIsUO1tbCtI9OQvtGe54QX_NfSaY0Fpp3YpkGFXTwi-0BiW9A8OwwIlHxBWUnKCLsbp5aE21sgVx2erY7FaZwb9fvgbYmdHpqTr8650BgNUsOa5BbfHTxaUpl4bgsywY0JNMNBk3LYguvfHu9egEwWWgZ_DJKEOZbcM-HA2cJ3hnPqQIbU-UPDM38crt98Nci95JftHSBTsZWYVm2-dEy2MKE6uZZ5mtOo83Rt02_vBTUlk3rKn8j5i6TGZEncF8QIeuqOA\"}"
}
```
![image](https://github.com/Tech-Challenge-FIAP-GLR/lambda_techchallenge/assets/77997696/de42db08-619a-4648-a87c-0a1b4c746c64)
