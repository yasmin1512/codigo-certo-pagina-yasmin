from flask import Flask, render_template, send_from_directory

# Importa a ferramenta para trabalhar com caminhos
import os

# Cria a aplicação Flask
app = Flask(
    __name__,
    template_folder="Templates",
    static_folder="Static"
)


# Abre a página de taxas
@app.route("/")
def inicio():
    return render_template("taxas.html")


# Mostra a logo do CredMais
@app.route("/logo")
def logo():
    caminho = os.path.join(app.root_path, "Static", "Uploads")
    return send_from_directory(caminho, "logo.png")


# Mostra o ícone de taxas
@app.route("/icone_taxas")
def icone_taxas():
    caminho = os.path.join(app.root_path, "Static", "Uploads")
    return send_from_directory(caminho, "icone_taxas.png")


# Executa o projeto
if __name__ == "__main__":
    app.run(debug=True)