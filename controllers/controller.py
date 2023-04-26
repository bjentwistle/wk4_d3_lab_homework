from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repo as book_repo
import repositories.author_repo as author_repo


books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():        #this function works on the /books route and shows all books
    books = book_repo.select_all() 
    return render_template("/books/index.html", all_books = books) #then renders all the books on the index page

# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')

# SHOW
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repo.select(id)
    return render_template('/books/show.html', book = book)

# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repo.select(id)
    author = author_repo.select_all()
    return render_template('/books/edit.html', book = book, all_authors = author)
