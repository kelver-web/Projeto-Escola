# Projeto-Escola
<h1>Como desenvolver</h1>
<ol>
<li>Clone o repositório</li>
<li>Crie um virtualenv com python 3.8</li>
<li>Ative o virtualenv</li>
<li>Instale as dependências</li>
<li>Configure a intância com o .env</li>
<li>Execute os textes</li>
</ol>


git clone git@github.com/kelver-web/Projeto-Escola.git
cd Projeto-Escola
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py

<h2>
  <h6>Para ter acesso a api digite no navegador http://127.0.0.1:8000/api/swagger/<h6>
  <h6>user: admin</h6>
  <h6>password: 123</h6>
<h2/>

<h2>
  <h6>Para ter acesso aos endpoints vá em token e gere um novo token</h6>
  <h6>Suba até Authorize e insira o token</h6>
  <h6>Acesse qualquer endpoint</h6>
<h2/>
