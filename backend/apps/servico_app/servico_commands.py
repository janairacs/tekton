# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from servico_app.servico_model import Servico



class ServicoSaveForm(ModelForm):
    """
    Form used to save and update Servico
    """
    _model_class = Servico
    _include = []


class ServicoForm(ModelForm):
    """
    Form used to expose Servico's properties for list or json
    """
    _model_class = Servico


class GetServicoCommand(NodeSearch):
    _model_class = Servico


class DeleteServicoCommand(DeleteNode):
    _model_class = Servico


class SaveServicoCommand(SaveCommand):
    _model_form_class = ServicoSaveForm


class UpdateServicoCommand(UpdateNode):
    _model_form_class = ServicoSaveForm


class ListServicoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListServicoCommand, self).__init__(Servico.query_by_creation())

