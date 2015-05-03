# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from servico_app.servico_model import Servico
from routes.servicos.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Servico.query().get())
        redirect_response = save()
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_servico = Servico.query().get()
        self.assertIsNotNone(saved_servico)


    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set([]), set(errors.keys()))
        self.assert_can_render(template_response)
