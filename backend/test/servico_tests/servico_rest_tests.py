# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from servico_app.servico_model import Servico
from routes.servicos import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Servico)
        mommy.save_one(Servico)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        servico_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', ]), set(servico_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Servico.query().get())
        json_response = rest.new(None, )
        db_servico = Servico.query().get()
        self.assertIsNotNone(db_servico)

        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set([]), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        servico = mommy.save_one(Servico)
        old_properties = servico.to_dict()
        json_response = rest.edit(None, servico.key.id(), )
        db_servico = servico.key.get()

        self.assertNotEqual(old_properties, db_servico.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        servico = mommy.save_one(Servico)
        old_properties = servico.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, servico.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set([]), set(errors.keys()))
        self.assertEqual(old_properties, servico.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        servico = mommy.save_one(Servico)
        rest.delete(None, servico.key.id())
        self.assertIsNone(servico.key.get())

    def test_non_servico_deletion(self):
        non_servico = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_servico.key.id())
        self.assertIsNotNone(non_servico.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

