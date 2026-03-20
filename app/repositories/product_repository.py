from app.db import get_db



def get_all_products():
    db = get_db()
    query = """
        SELECT p.id, p.nome, p.prezzo, p.categoria_id, c.nome
        FROM categorie c
        Join prodotti p On c.id = p.categoria_id
        ORDER BY nome
    """
    categories = db.execute(query).fetchall()
    return [dict(g) for g in categories]






def get_products_by_category(categoria_id):
    
    db = get_db()

    query = """
        SELECT p.id, p.nome, p.prezzo, p.categoria_id, c.nome, c.id
        FROM categorie c
        Join prodotti p On c.id  = p.categoria_id
        WHERE categoria_id = ?
    """

    product = db.execute(query,(categoria_id,)).fetchall()
    if product:
     return product
    else:

     return None
    

def create_product(categoria_id, nome, prezzo):
    """Crea una nuova partita."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (?, ?, ?)", (categoria_id, nome, prezzo)
    )
    db.commit()
    return cursor