# 📦 QR Code Web App (Flask + Docker)

Aplicação web simples para **gerar QR Codes** a partir de links.  
O usuário cola a URL em uma interface web e faz o download do QR Code em formato `.png`.

---

## 🚀 Tecnologias
- [Python 3.12](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [qrcode](https://pypi.org/project/qrcode/) (com [Pillow](https://pypi.org/project/Pillow/))
- [Docker](https://www.docker.com/)

---

## 📂 Estrutura do projeto
```
qr-code-app/
│── app.py               # Código principal Flask
│── requirements.txt     # Dependências do projeto
│── Dockerfile           # Configuração Docker
│── templates/
│    └── index.html      # Interface web
│── README.md            # Documentação
```

---

## ▶️ Como rodar com Docker

### 1. Construir a imagem
```bash
docker build -t qr-code-app .
```

### 2. Rodar o container
```bash
docker run -d -p 5000:5000 --name qr-code-app qr-code-app
```

### 3. Acessar a aplicação
Abra no navegador:
```
http://localhost:5000
```

---

## 🛠️ Rodando localmente (sem Docker)

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/qr-code-app.git
cd qr-code-app
```

### 2. Criar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar a aplicação
```bash
python app.py
```

Acesse em:
```
http://localhost:5000
```

---

## 📸 Demonstração

### Tela inicial:
Formulário simples onde o usuário cola o link e clica em **Gerar**.

### Resultado:
Um arquivo `qrcode.png` é baixado automaticamente.

---
