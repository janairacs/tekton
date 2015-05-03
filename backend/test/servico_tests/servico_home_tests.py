# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from servico_app.servico_model import Servico
from routes.servicos.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Servico)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        servico = mommy.save_one(Servico)
        redirect_response = delete(servico.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(servico.key.get())

    def test_non_servico_deletion(self):
        non_servico = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_servico.key.id())
        self.assertIsNotNone(non_servico.key.get())

