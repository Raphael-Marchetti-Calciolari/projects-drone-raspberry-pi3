# ProjetoDroneRaspberryPi3

## Descrição do Projeto

O objetivo inicial do projeto é desenvolver uma forma de controlar um Parrot AR Drone 2.0 através do módulo Wifi do Raspberry Pi 3.
O objetivo final do projeto é desenvolver uma API no Raspberry Pi 3 que se comunica com o drone e o envia para localizações geográficas específicas simulando entregas e retornando ao ponto de partida.

### Sobre a conexão com o drone:
- O Raspberry irá se conectar na rede hosteada pelo drone, configurá-lo enviando comandos AT via UDP em sua porta 5556.
- Gráficos irão exibir a leitura dos dados realizados pelos sensores do drone recebidos pela rede via UDP em sua porta 5554.
- O vídeo gravado pela câmera do drone que é recebido pela rede via UDP em sua porta 5555 será exibido em tempo real.

### Sobre a visualização dos dados:
Os gráficos de navdata e vídeo em tempo real coletados pelo drone serão exibidos em uma das rotas da API hosteada pelo Raspberry Pi 3.

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
- GET ```/navdata``` - retorna informações de navdata do drone tais como status, posição e velocidade.
- GET ```/live``` - exibe o vídeo capturado pela câmera do drone em tempo real.
- GET ```/delivery/status``` - exibe informações relativas ao progresso da entrega atual tais como, se foi entregue, posição, velocidade e progresso.
- POST ```/delivery/request``` - body data convention:
  ```
  {
    "flight-speed" : "speed in kilometers per second",
    "height" : "ground distance in centimeters",
    "position" : "coordinates lat & lon",
    "scheduled-delivery-time" : "time in HH:MM:SS that the drone will arrive at the destination"
  }
  ```

### Membros envolvidos no projeto
1. **Raphael Marchetti Calciolari** - RA: 19.00828-7
2. **Martin Ropke** - RA: 19.01592-5
3. **Guilherme Costa e Souza** - RA: 19.00065-0
4. **Bruno Vilardi Bueno** - RA: 19.00331-5
