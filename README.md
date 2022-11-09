# ProjetoDroneRaspberryPi3

## Descrição do Projeto
O objetivo inicial do projeto é desenvolver uma forma de controlar um Parrot AR Drone 2.0 através de qualquer interface Wifi, utilizaremos a do Raspberry Pi 3.

### Sobre a conexão com o drone:
- O Raspberry irá se conectar na rede hosteada pelo drone, no nosso caso _ardrone2_326331_, configurá-lo enviando comandos AT via UDP em sua porta 5556.
- Gráficos irão exibir a leitura dos dados realizados pelos sensores do drone recebidos pela rede via UDP em sua porta 5554.
- O vídeo gravado pela câmera do drone que é recebido pela rede via UDP em sua porta 5555 será exibido em tempo real. (Não acessado neste projeto)

### Sobre a visualização dos dados:
Os gráficos de navdata em tempo real coletados pelo drone são enviados para uma API hospedada no Node-RED exibidos em uma das rotas da API hosteada pelo Raspberry Pi 3.

### Inicializar o Node-RED
#### Instalação via npm
- Rode o comando ```npm install -g node-red``` (adicione sudo caso seja linux)
- Rode com o comando ```node-red```

##### Erro ao tentar rodar ```node-red```

![erro](https://user-images.githubusercontent.com/79259612/200924382-a38b0485-8a70-42e1-afdb-ec2e9e4e5625.png)

- Tente com o comando do npx abaixo para uma solução mais rápida.
- Para solucionar o problema, procure a instalação do node-red (windows)
  - Procure em sua instalação local do npm
  - Busque no ```%appdata%/npm```
  - Adicione o caminho ao node-red no PATH

#### Rodando via npx
- Rode o comando ```npx node-red```

### Importando o flow do projeto no node-red
Ao iniciar o Node-RED seu log será parecido com o abaixo:
![log-nodered](https://user-images.githubusercontent.com/79259612/200917584-af2ca2e0-c22e-4ab3-bb06-c13f9d1db9d4.png)

Verifique onde o servidor está rodando e acesse o endereço via browser (no nosso caso é ```http://127.0.0.1:1880```)

Selecione Manage Palete e instale o node-red-dashboard.

![image](https://user-images.githubusercontent.com/79259612/200922821-167ac87e-925c-4c65-ae37-53bc664c31a4.png)

![image](https://user-images.githubusercontent.com/79259612/200919593-3bc7edab-f8cf-4ded-beea-57b3ffeb692a.png)


Após a instalação, clique 2 vezes sobre a aba "Flow 1" e o renomeie para evitar confusões posteriores.

![aba](https://user-images.githubusercontent.com/79259612/200923311-e42e3dcf-e923-43f8-b422-dee4574be38e.png)

![image](https://user-images.githubusercontent.com/79259612/200918261-2d6dc995-6e06-4f48-a7d6-1d6c95800cfd.png)

Selecione a opção import para utilizar o flow do projeto.

![image](https://user-images.githubusercontent.com/79259612/200923577-611bc733-118c-4b3a-8337-464b933c85e3.png)

![image](https://user-images.githubusercontent.com/79259612/200920071-d765e9f6-cff3-4e90-a64e-c941754b2d15.png)

Selecione o arquivo ```flows``` deste projeto em ```/nodeRed```

![image](https://user-images.githubusercontent.com/79259612/200920104-3190476d-17ee-4f47-9ad4-4c8601cb1572.png)

Ao importar o novo fluxo, apague o anterior (clique 2 vezes sobre a aba e selecione Delete) e faça o deploy (botão vermelho no canto superior direito).

Acesse o recurso no seu endereço em ```/ui```, no nosso caso ```http://127.0.0.1:1880/ui``` e verifique se o dashboard aparece como na imagem abaixo.

![image](https://user-images.githubusercontent.com/79259612/200920679-4058e4a9-e8ed-4e59-851f-d0d469bcb9e7.png)


## Controle inicial do AR Drone 2.0 através do Raspberry Pi 3
### Movimentação por teclado:
  - W - drone se desloca para a frente de onde ele está direcionado
  - S - drone se desloca para trás de onde ele está direcionado
  - A - drone se desloca lateralmente para a esquerda de onde ele está direcionado
  - D - drone se desloca lateralmente para a direita de onde ele está direcionado
  - Espaço - drone sobe
  - Shift - drone desce
  - Q - drone gira no sentido anti-horário
  - E - drone gira no sentido horário
  - T - decolagem do drone (Takeoff)
  - L - pouso do drone (Land)

### Movimentação por mouse:
  - Mouse se movimenta horizontalmente - drone gira no sentido correspondente
  - Mouse se movimenta verticalmente - drone se desloca para frente ou para trás de acordo com a intensidade.
  - Scroll do mouse - drone sobe (scroll para cima) ou desce (scroll para baixo)
  - Botão esquerdo - Pousar
  - Botão direito - Decolar

## API
- GET ```/navdata?droneId=<id>``` - retorna informações de navdata do drone tais como status, posição e velocidade.
- GET ```/live?droneId=<id>``` - exibe o vídeo capturado pela câmera do drone em tempo real.
- GET ```/delivery/status?deliveryId=<id>&droneId=<id>``` - exibe informações relativas ao progresso da entrega tais como, se foi entregue, posição, velocidade e progresso.
- POST ```/delivery/request?droneId=<id>``` - body data convention:
  ```
  {
    "flight-speed" : "speed in kilometers per second during flight",
    "height" : "ground distance in centimeters during flight",
    "position" : "coordinates in x,y and z in centimeters",
  }
  ```

## Arquitetura
O código será desenvolvido seguindo uma interpretação de arquitetura limpa

### Definição padrão
![Default Definition](https://miro.medium.com/max/1400/1*0u-ekVHFu7Om7Z-VTwFHvg.png)

### Interpretação que será utilizada
![Reference Definition](https://raw.githubusercontent.com/PropysMaua/ProjetoLPARQ/main/docFiles/BackEnd-Arch.png)

#### Detalhamento
Entities:
- Delivery
- Drone
- Keyboard
- Mouse

Features:
- GetDeliveryStatus
- RequestDelivery
- CancelDelivery
- UpdateDelivery
- GetLiveData
- GetNavData
- KeyboardControlDrone
- MouseControlDrone

### Membros envolvidos no projeto
1. **Raphael Marchetti Calciolari** - RA: 19.00828-7
2. **Martin Ropke** - RA: 19.01592-5
3. **Guilherme Costa e Souza** - RA: 19.00065-0
4. **Bruno Vilardi Bueno** - RA: 19.00331-5
