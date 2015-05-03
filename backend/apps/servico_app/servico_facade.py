# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from servico_app.servico_commands import ListServicoCommand, SaveServicoCommand, UpdateServicoCommand, ServicoForm,\
    GetServicoCommand, DeleteServicoCommand


def save_servico_cmd(**servico_properties):
    """
    Command to save Servico entity
    :param servico_properties: a dict of properties to save on model
    :return: a Command that save Servico, validating and localizing properties received as strings
    """
    return SaveServicoCommand(**servico_properties)


def update_servico_cmd(servico_id, **servico_properties):
    """
    Command to update Servico entity with id equals 'servico_id'
    :param servico_properties: a dict of properties to update model
    :return: a Command that update Servico, validating and localizing properties received as strings
    """
    return UpdateServicoCommand(servico_id, **servico_properties)


def list_servicos_cmd():
    """
    Command to list Servico entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListServicoCommand()


def servico_form(**kwargs):
    """
    Function to get Servico's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ServicoForm(**kwargs)


def get_servico_cmd(servico_id):
    """
    Find servico by her id
    :param servico_id: the servico id
    :return: Command
    """
    return GetServicoCommand(servico_id)



def delete_servico_cmd(servico_id):
    """
    Construct a command to delete a Servico
    :param servico_id: servico's id
    :return: Command
    """
    return DeleteServicoCommand(servico_id)

