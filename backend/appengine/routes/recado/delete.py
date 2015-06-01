# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router
from recado_app import recado_facade
from routes import recado
from tekton.gae.middleware.json_middleware import JsonResponse
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf


@no_csrf
def index(_resp, **kwargs):
    id = kwargs['id']
    cmd = recado_facade.delete_recado_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)

    return JsonResponse({'mensagem': 'Recado excluido com sucesso!'})