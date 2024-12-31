# Detecção de Objetos em Vídeo com YOLO

Bem-vindo ao repositório de Detecção de Objetos em Vídeo utilizando o modelo YOLO! Este repositório contém um script em Python que realiza a detecção de objetos em cada frame de um vídeo, utilizando o modelo YOLO (You Only Look Once) para identificar e marcar objetos.

## Índice

*   [Introdução](#introdução)
*   [Pré-requisitos](#pré-requisitos)
*   [Instalação](#instalação)
*   [Uso](#uso)
*   [Explicação do Código](#explicação-do-código)
*   [Contribuição](#contribuição)

## Introdução

Este projeto utiliza o modelo YOLO para realizar a detecção de objetos em vídeos. O YOLO é um dos modelos mais populares para tarefas de detecção de objetos devido à sua velocidade e precisão. Este script processa cada frame de um vídeo, detecta objetos e desenha caixas delimitadoras ao redor deles.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pacotes instalados:

*   Python 3.6 ou superior
*   OpenCV
*   Ultralytics YOLO
*   Pandas

## Instalação

Para instalar as dependências necessárias, você pode usar o pip:

```bash
pip install opencv-python ultralytics pandas
```
## Uso 
Baixe ou clone o repositório:
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git) # Substitua pelo seu repositório
cd seu-repositorio
```
Certifique-se de ter um arquivo de vídeo (.mp4) na pasta correta. Altere o caminho no script (main.py) conforme necessário:

```python
cap = cv2.VideoCapture("videos/meu_video.mp4") # Exemplo: vídeo na pasta "videos"
```

Baixe o modelo YOLO pré-treinado (se necessário). O código abaixo verifica se o modelo existe e o baixa caso contrário:

```python
import os
import torch
from ultralytics import YOLO

modelo_path = "yolov8n.pt" # Ou outro modelo como yolov8s.pt, yolov8m.pt, etc.
if not os.path.exists(modelo_path):
    print(f"Baixando modelo {modelo_path}...")
    torch.hub.download_url_to_file(f'[URL inválido removido]', modelo_path)
    print("Download concluído.")

model = YOLO(modelo_path)
```

Execute o script:

```bash
python main.py
```

## Explicação do código

Este código carrega um modelo YOLO pré-treinado, abre um arquivo de vídeo, processa cada frame, realiza a detecção de objetos, desenha caixas delimitadoras e rótulos e exibe o vídeo resultante.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver alguma sugestão de melhoria, por favor, abra uma issue ou envie um pull request.
