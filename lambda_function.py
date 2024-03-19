import json
import boto3
from botocore.exceptions import ClientError

cognito_client = boto3.client('cognito-idp')

USER_POOL_ID = 'us-east-2_oNUeC93Xd'
CLIENT_ID = 'v714qjfstuelmi6bnbgp9jlc2'

def verify_cpf_format(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit()

def lambda_handler(event, context):
    req_body = event.get("body", {})
    user = req_body.get("username")
    pwd = req_body.get("password")

    if not user or not pwd:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "CPF e/ou senha não fornecidos."})
        }
    
    if not verify_cpf_format(user):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "CPF inválido!"})
        }

    try:
        response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user,
                'PASSWORD': pwd
            },
            ClientId=CLIENT_ID
        )
        challenge = response.get('ChallengeName')

        if challenge == 'NEW_PASSWORD_REQUIRED':
            challenge_response = cognito_client.respond_to_auth_challenge(
                ClientId=CLIENT_ID,
                ChallengeName='NEW_PASSWORD_REQUIRED',
                Session=response.get('Session'),
                ChallengeResponses={
                    'USERNAME': user,
                    'NEW_PASSWORD': pwd
                }
            )
            token = challenge_response.get("AuthenticationResult", {}).get("IdToken")
        else:
            token = response.get("AuthenticationResult", {}).get("IdToken")

        return {
            "statusCode": 200,
            "body": json.dumps({"token": token})
        }
    except ClientError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": str(e)})
        }