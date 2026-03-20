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
def category_detail(id,category_id):

    category = categoria_repository.get_category_by_id(id)
    prodotti = product_repository.get_products_by_category(category_id)

    return render_template("categories_detail.html", category=category, prodotti = prodotti)


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

        return render_template("category_create.html") 
    return render_template("category_create.html")       


@bp.route("/crea_prodotto", methods=("GET", "POST"))
def prodotto_create():
        
    if request.method == "POST":
        categoria_id = request.form["categoria_id"]
        nome = request.form["nome"]
        prezzo = request.form.get("prezzo", 0, type=int)
        error = None

        if not categoria_id:
            error = "La data è obbligatoria."
        if not nome:
            error = "Il vincitore è obbligatorio."
        if not prezzo:
            error = "Il punteggio del vincitore è obbligatorio."
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            product_repository.create_product(categoria_id, nome, prezzo)
            return redirect(url_for("main.index"))

        return render_template("prodotto_create.html")
    return render_template("prodotto_create.html")