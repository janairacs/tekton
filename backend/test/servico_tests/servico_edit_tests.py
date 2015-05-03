# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from servico_app.servico_model import Servico
from routes.servicos.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        servico = mommy.save_one(Servico)
        template_response = index(servico.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        servico = mommy.save_one(Servico)
        old_properties = servico.to_dict()
        redirect_response = save(servico.key.id(), )
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_servico = servico.key.get()

        self.assertNotEqual(old_properties, edited_servico.to_dict())

    def test_error(self):
        servico = mommy.save_one(Servico)
        old_properties = servico.to_dict()
        template_response = save(servico.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set([]), set(errors.keys()))
        self.assertEqual(old_properties, servico.key.get().to_dict())
        self.assert_can_render(template_response)
