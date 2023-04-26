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

