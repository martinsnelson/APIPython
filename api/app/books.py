from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serealizer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route("/mostrar", methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200


# @bp_books.route("/deletar", methods=['GET'])
# def deletar():
#     ..



# @bp_books.route("/modificar", methods=['PUT'])
# def modificar():
#     ..



@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = BookSchema()
    book, error = bs.load(request.json)

    if error:
        return jsonify(error), 401
        
    # bs.load(request.json)
    # import ipdb; ipdb.set_trace()
    # print(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 201