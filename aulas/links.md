•	Criar conta: [URL](https://aws.amazon.com/pt/free/?trk=c9dcfe7b-33fc-4345-b0c3-77b810bbd58c&sc_channel=ps&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
•	Instalar AWS CLI: https://github.com/aws/aws-cli
•	Instalar eb cli: https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/eb-cli3-install.html#eb-cli3-install.scripts
•	Tutorial: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

# Packotes
Para resolver o problema no SQLAlchemy, instale o seguinte pacote
pip3 install flask_sqlalchemy

# AWS
Criar conta: [URL](https://aws.amazon.com/pt/free/?trk=c9dcfe7b-33fc-4345-b0c3-77b810bbd58c&sc_channel=ps&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
•	Instalar AWS CLI: https://github.com/aws/aws-cli      
•	Instalar eb cli: https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/eb-cli3-install.html#eb-cli3-install.scripts
•	Tutorial: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
# CLI
•	https://docs.aws.amazon.com/cli/v1/userguide/install-windows.html#msi-on-windows 
# IAM Para criar usários para gerar chave de conexão
•	https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/users

# Server
λ python3 -m http.server -b 127.0.0.1 8080
λ flask run
λ flask run --port 5001
λ flask --app hello run

# ======= Erro no server =======
# Verifique se a porta já está em uso
O Flask, por padrão, roda na porta 5000. Se outro processo estiver usando essa porta, você pode:
Alterar a porta que o Flask está usando para uma disponível, executando:

flask run --port 5001

Ou verificar qual processo está usando a porta 5000 e matá-lo. Dependendo do sistema operacional:

# Linux/Unix/MacOS:
lsof -i :5000
Em seguida, mate o processo:
kill -9 <PID>

# Windows: Primeiro, veja qual processo está ocupando a porta:
netstat -ano | findstr :5000
Use o ID do processo (PID) obtido para encerrar:
taskkill /PID <PID> /F