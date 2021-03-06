# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from produto_app.produto_model import Produto
from routes.produtos.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        produto = mommy.save_one(Produto)
        template_response = index(produto.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        produto = mommy.save_one(Produto)
        old_properties = produto.to_dict()
        redirect_response = save(produto.key.id(), )
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_produto = produto.key.get()

        self.assertNotEqual(old_properties, edited_produto.to_dict())

    def test_error(self):
        produto = mommy.save_one(Produto)
        old_properties = produto.to_dict()
        template_response = save(produto.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set([]), set(errors.keys()))
        self.assertEqual(old_properties, produto.key.get().to_dict())
        self.assert_can_render(template_response)
