from fastapi import FastAPI

app = FastAPI()

book_dictionary = {
    "Book_1": {
        "title": "Title_1",
        "author": "Author_1"
    },
    "Book_2": {
        "title": "Title_2",
        "author": "Author_2"
    },
    "Book_3": {
        "title": "Title_3",
        "author": "Author_3"
    },
    "Book_4": {
        "title": "Title_4",
        "author": "Author_4"
    },
    "Book_5": {
        "title": "Title_5",
        "author": "Author_5"
    },
    "Book_6": {
        "title": "Title_6",
        "author": "Author_6"
    },
    "Book_7": {
        "title": "Title_7",
        "author": "Author_7"
    },
    "Book_8": {
        "title": "Title_8",
        "author": "Author_8"
    },
    "Book_9": {
        "title": "Title_9",
        "author": "Author_9"
    },
    "Book_10": {
        "title": "Title_10",
        "author": "Author_10"
    }
}


@app.get("/")
async def read_all_book(skip_book: str | None = None):
    if skip_book:
        new_books = book_dictionary.copy()
        del new_books[skip_book]
        return new_books
    return book_dictionary


@app.post("/")
async def new_book(book_title: str, book_author: str):
    print("running")
    curr_idx = 0
    for key in book_dictionary.keys():
        get_idx_key = int(key.split("_")[1])
        if get_idx_key > curr_idx:
            curr_idx = get_idx_key
    book_dictionary[f"Book_{curr_idx}"] = {"title": book_title, "author": book_author}
    return f"Success added {book_title}"


@app.delete("/{book_name}")
async def delete_book(book_name:str):
    del book_dictionary[book_name]
    return f"book {book_name} deleted"


@app.put("/{book_name}")
async def edit_book(book_name:str, book_title:str,book_author:str):
    book_dictionary[book_name] = {"title": book_title, "author": book_author}
    return f"book {book_name} is editted"


@app.get("/{book_name}")
async def read_selected_book(book_name: str):
    return book_dictionary[book_name]
