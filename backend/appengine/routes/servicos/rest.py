# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from servico_app import servico_facade


def index():
    cmd = servico_facade.list_servicos_cmd()
    servico_list = cmd()
    servico_form = servico_facade.servico_form()
    servico_dcts = [servico_form.fill_with_model(m) for m in servico_list]
    return JsonResponse(servico_dcts)


def new(_resp, **servico_properties):
    cmd = servico_facade.save_servico_cmd(**servico_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **servico_properties):
    cmd = servico_facade.update_servico_cmd(id, **servico_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = servico_facade.delete_servico_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        servico = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    servico_form = servico_facade.servico_form()
    return JsonResponse(servico_form.fill_with_model(servico))

