# Food Tech Challenge FIAP
## Elastic Kubernetes Service (Amazon EKS)
Este repositório é responsável por criar toda a estrutura de Kubernetes com TerraForm dentro da nuvem da AWS utilizando o serviço EKS, assim a aplicação Food Tech Challenge utilizará desses serviços para realizar o deploy e ficar disponível para o usuário.

## Atualizando o EKS
Sempre que realizar uma atualização do código, deve-se criar um pull-request da branch utilizada para a branch "main", assim que realizar o merge, o github actions fará toda a atualizanção para a AWS.

## Requirements
* AWS account
* Configure aws access keys vars from Security Credentials:
  * export AWS_ACCESS_KEY_ID=[your-key-id]
  * export AWS_SECRET_ACCESS_KEY=[your-key-secret]
