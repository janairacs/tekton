# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from book_app.book_commands import ListBookCommand, SaveBookCommand, UpdateBookCommand, BookForm,\
    GetBookCommand, DeleteBookCommand


def save_book_cmd(**book_properties):
    """
    Command to save Book entity
    :param book_properties: a dict of properties to save on model
    :return: a Command that save Book, validating and localizing properties received as strings
    """
    return SaveBookCommand(**book_properties)


def update_book_cmd(book_id, **book_properties):
    """
    Command to update Book entity with id equals 'book_id'
    :param book_properties: a dict of properties to update model
    :return: a Command that update Book, validating and localizing properties received as strings
    """
    return UpdateBookCommand(book_id, **book_properties)


def list_books_cmd():
    """
    Command to list Book entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListBookCommand()


def book_form(**kwargs):
    """
    Function to get Book's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return BookForm(**kwargs)


def get_book_cmd(book_id):
    """
    Find book by her id
    :param book_id: the book id
    :return: Command
    """
    return GetBookCommand(book_id)



def delete_book_cmd(book_id):
    """
    Construct a command to delete a Book
    :param book_id: book's id
    :return: Command
    """
    return DeleteBookCommand(book_id)

