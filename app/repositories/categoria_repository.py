from app.db import get_db


def get_all_categories():
    db = get_db()
    query = """
        SELECT id, nome
        FROM categorie
        ORDER BY nome
    """
    categories = db.execute(query).fetchall()
    return [dict(g) for g in categories]

def get_category_by_id(category_id):
    
    db = get_db()

    query = """
        SELECT id, nome
        FROM categorie
        WHERE id = ?
    """

    category = db.execute(query,(category_id,)).fetchone()
    if category:
     return category
    else:

     return None
    


def create_category(nome):
    db = get_db()
    db.execute(
        "INSERT INTO categorie (nome) VALUES(?)",(nome)
    )
    db.commit()


    
