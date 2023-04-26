from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repo as author_repo


def save(book):
    sql = "INSERT INTO books (title, pubdate, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.pubdate, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    print("From the save book func in book_repo", book.title)
    return book

def select_all():
    books = [ ]
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['id'])
        book = Book(row['title'], row['pubdate'], author, row['id'])
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select(id):
    book = None

    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = author_repo.select(result['id'])
        book = Book(result['title'], result['pubdate'], author, result['id'])
    return book