# [🚀 Sistema de Controle de Entrada/Saída](https://pumbadev.com)

![GitHub repo size](https://img.shields.io/github/repo-size/DevUnusual/flaskServer_EspClient?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/DevUnusual/flaskServer_EspClient?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/DevUnusual/flaskServer_EspClient?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/DevUnusual/flaskServer_EspClient?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/github/issues-pr/DevUnusual/flaskServer_EspClient?style=for-the-badge)

> Aplicação desenvolvida em ESP 32 e API Python para controlar o fluxo de entrada e saída de um ambiente. Para o controle é utilizado um banco de usuários que guarda o saldo e identificador de cada um.

## 💻 Pré-requisitos

Antes de começar, verifique se você atende às seguintes dependências:

- [`< Git >`](https://git-scm.com/)
- [`< Python 3 >`](https://www.python.org/)


## 📝 Funcionamento

### Equipamentos

- Esp32Cam IA thinker
- HC-SR04 (sensor de distancia ultrassonico) IO 14 e 15
- 2 Leds (Verde e Vermelho) IO 2 e 4

### Fluxo de Entrada

- Aponte o QR Code do seu ID na ESP CAM.

- A API irá verificar a lotação e seu saldo, caso tenha erro a luz vermelha se acenderá.

- Case a entrada seja permitida, a luz verde se acenderá.


### Fluxo de Saída

- Passe próximo ao Sensor de Distância Ultrassônico

- Caso o sensor detecte sua presenta, ele permitirá sua saída e decrementará a lotação.

## ⚙️ Instalando o Projeto

Siga estas etapas:

- Clonando projeto

```
git clone https://github.com/DevUnusual/flaskServer_EspClient.git
```

- Instalando dependências

```
pip install -r requirements.txt
```

- Hospedando API e Populando BD

```
python main.py first
```

- Gravando Esp 32 com IA Thinker

```
Instale a biblioteca quirc

Grave o QRCODEreader.ino no esp32Cam IA thinker
```

## 💻 Feito Com:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🤝 Desenvolvido Por

<table>
  <tr>
    <!-- Pumba Developer -->
    <td align="center">
      <a href="https://github.com/pumba-dev">
        <img src="https://static.wikia.nocookie.net/disneypt/images/c/cf/It_means_no_worries.png/revision/latest?cb=20200128144126&path-prefix=pt" width="100px;" height="100px;" alt="Foto do Pumbadev no GitHub"/><br>
        <sub>
          <b>Pumba Developer</b>
        </sub>
      </a>
    </td>
    <!-- Carlos Menezes -->
    <td align="center">
      <a href="https://github.com/DevUnusual">
        <img src="https://avatars.githubusercontent.com/u/48740928?v=4" width="100px;" height="100px;" alt="Foto do Carlos Menezes"/><br>
        <sub>
          <b>Carlos Menezes</b>
        </sub>
      </a>
    </td>
    <!-- Gabriel Reis -->
    <td align="center">
      <a href="https://github.com/usernamegran">
        <img src="https://avatars.githubusercontent.com/u/37776927?v=4" width="100px;" height="100px;" alt="Foto do Gabriel Reis"/><br>
        <sub>
          <b>Gabriel Reis</b>
        </sub>
      </a>
    </td>
    <!-- Antonio Correia -->
    <td align="center">
      <a href="https://github.com/acorreiacruz">
        <img src="https://avatars.githubusercontent.com/u/86582096?v=4" width="100px;" height="100px;" alt="Foto do Antonio Correia"/><br>
        <sub>
          <b>Antonio Correia</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 😄 Seja um dos Contribuidores<br>

Entre em contato para se tornar um contribuidor.

## 💰 Donate

[![PicPay](https://img.shields.io/badge/PicPay-%40PumbaDev%20-brightgreen)](https://picpay.me/pumbadev)
[![Nubank](https://img.shields.io/badge/Nubank-Pix%20QR%20Code-blueviolet)](https://nubank.com.br/pagar/1ou9f/ifu2K7YNO7)

## 📝 Licença

Copyright © 2023 Universidade Federal do Piaui - UFPI

[⬆ Voltar ao topo](#webservice-with-socket)<br>
