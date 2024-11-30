# Jogo da Forca

Este é um simples **Jogo da Forca** implementado em Python utilizando a biblioteca `tkinter` para criar uma interface gráfica (GUI). O objetivo do jogo é adivinhar uma palavra, tentando descobrir as letras que a compõem antes de cometer um número máximo de erros.

## Objetivo do Projeto

O principal objetivo deste projeto é demonstrar o uso de controle de versão com Git e GitHub, enquanto cria um jogo funcional em Python. O código segue uma estrutura que pode ser facilmente modificada e expandida, e utiliza as práticas de boas práticas de versionamento.

## Funcionalidades Implementadas

- **Interface Gráfica**: Utilizando o Tkinter, foi criada uma interface simples onde o jogador pode visualizar o progresso da palavra a ser adivinhada, os erros cometidos e um boneco que vai sendo desenhado conforme os erros.
- **Gerenciamento de Letras**: O jogo permite que o jogador escolha uma letra a cada tentativa, e essas escolhas são comparadas com a palavra secreta.
- **Contador de Tentativas**: A cada letra errada, o número de tentativas diminui até que o jogador perca o jogo ou adivinhe todas as letras da palavra.
- **Exibição de Letras Usadas**: As letras já tentadas são exibidas para o jogador, evitando repetições.

## Como Executar

### Pré-requisitos

1. Certifique-se de que você tenha o Python 3.x instalado no seu sistema. Você pode verificar isso executando:
   ```bash
   python --version
