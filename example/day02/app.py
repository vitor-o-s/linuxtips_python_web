from flask import Flask, url_for, request

app = Flask(__name__)

# Contexto de configuração 
# Antes de servir a aplicação
app.config['APP_NAME'] = 'Um blog qualquer'

@app.errorhandler(404)
def not_found_page(error):
    return f"Not found on {app.config['APP_NAME']}"

# app.register_error_handler(404, not_found_page)


@app.route('/')
def index():
    content_url = url_for('read_content', title='Novidades de 2022')
    return (
        f"<h1>{app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Novidades de 2022</a>"
        "<hr>"
        f"{request.args}" # Contexto de request, gerenciado pelo Flask
    )

# @app.route('/<title>')
def read_content(title):
    index_url = url_for('index') # Contexto de aplicação/Já foi servido
    return f"<h1>{title}</h1> <a href='{index_url}'>Voltar</a>"

app.add_url_rule('/<title>', view_func=read_content) # Mesmo efeito do decorator