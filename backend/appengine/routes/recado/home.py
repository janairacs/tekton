# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.gae.middleware.json_middleware import JsonResponse
from tekton.gae.middleware.redirect import RedirectResponse
from recado_app import recado_facade
import json


@login_not_required
@no_csrf
def index(_resp, **kwargs):
    # Se for via Ajax
    if kwargs:
        # Procurar o recado com o ID passado pelo POST - AJAX
        recado_id = kwargs['id']
        cmd = recado_facade.get_recado_cmd(recado_id)
        try:
            recado = cmd()

        except CommandExecutionException:
            _resp.status_code = 500
            return JsonResponse(cmd.errors)

        recado_form = recado_facade.recado_form()
        dados = {
            'neto': recado.neto
        }

        return JsonResponse(recado_form.fill_with_model(recado)) # Json só aceita objetos simples, não podendo passar uma instância de Recado

    # Listagem de todos os recados
    cmd = recado_facade.list_recados_cmd()
    recado_list = cmd()
    recado_form = recado_facade.recado_form()
    context = {'recados': recado_list, 'form': recado_form}
    return TemplateResponse(context)
