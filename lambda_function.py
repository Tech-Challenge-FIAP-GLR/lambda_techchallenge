import json
import boto3
from botocore.exceptions import ClientError

cognito_client = boto3.client('cognito-idp')

USER_POOL_ID = 'us-east-2_oNUeC93Xd'
CLIENT_ID = 'v714qjfstuelmi6bnbgp9jlc2'

def valida_CPF(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit() 

def lambda_handler(event, context):
    body = event.get("body", {})
    username = body.get("username")
    password = body.get("password")

    if not username or not password:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "CPF e/ou senha não informados."})
        }
    
    if not valida_CPF(username):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "CPF invalido!"})
        }

    try:
        response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            },
            ClientId=CLIENT_ID
        )
        challenge_name = response.get('ChallengeName')

        if challenge_name == 'NEW_PASSWORD_REQUIRED':
            challenge_response = cognito_client.respond_to_auth_challenge(
                ClientId=CLIENT_ID,
                ChallengeName='NEW_PASSWORD_REQUIRED',
                Session=response.get('Session'),
                ChallengeResponses={
                    'USERNAME': username,
                    'NEW_PASSWORD': password
                }
            )
            id_token = challenge_response.get("AuthenticationResult", {}).get("IdToken")
        else:
            id_token = response.get("AuthenticationResult", {}).get("IdToken")

        return {
            "statusCode": 200,
            "body": json.dumps({"token": id_token})
        }
    except ClientError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": str(e)})
        }
