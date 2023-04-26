import pdb
from models.book import Book
from models.author import Author

import repositories.book_repo as book_repo
import repositories.author_repo as author_repo


author1 = Author("J.R.R. Tolkien")
author_repo.save(author1)
book1 = Book("Lord of the rings", 1954, author1)
book_repo.save(book1)

author2 = Author("Philip Reeve")
author_repo.save(author2)
book2 = Book("His Dark Materials", 2003, author2)
book_repo.save(book2)
