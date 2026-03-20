from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, product_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint("main", __name__)

@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    categories: list[dict] = categoria_repository.get_all_categories()

    # 2. Passiamo la variabile 'games' al template
    return render_template("index.html", categories=categories)


@bp.route("/category/<int:id>")
def category_detail(id):

    category = categoria_repository.get_category_by_id(id)

    return render_template("categories_detail.html", category=category)


@bp.route("/create", methods=("GET", "POST"))
def category_create():
        
    if request.method == "POST":
        nome = request.form["nome"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."

        if error is not None:
            flash(error)
        else:
            categoria_repository.create_category(nome)
            return redirect(url_for("main.index"))

        return render_template("game_create.html")




    return render_template("category_create.html")      

@bp.route("/game<int:id>/partite", methods=("GET", "POST"))
def get_partita(id):
    partita = partita_repo.get_partita_by_id(id)
    if partita is None:
        abort(404, f"Partita con id {id} non trovata.")
    return render_template("partita_detail.html", partita=partita)


@bp.route("/game<int:id>/partite/create", methods=("GET", "POST"))
def partita_create(id):
        
    if request.method == "POST":
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio_vincitore = request.form.get("punteggio_vincitore", 0, type=int)
        error = None
        game_id = id

        if not data:
            error = "La data è obbligatoria."
        if not vincitore:
            error = "Il vincitore è obbligatorio."
        if not punteggio_vincitore:
            error = "Il punteggio del vincitore è obbligatorio."
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il gioco
            partita_repo.create_partita(game_id, data, vincitore, punteggio_vincitore)
            return redirect(url_for("main.index"))

        return render_template("partita_create.html")
    return render_template("partita_create.html")