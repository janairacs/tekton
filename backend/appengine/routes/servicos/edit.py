# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from servico_app import servico_facade
from routes import servicos
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(servico_id):
    servico = servico_facade.get_servico_cmd(servico_id)()
    servico_form = servico_facade.servico_form()
    context = {'save_path': router.to_path(save, servico_id), 'servico': servico_form.fill_with_model(servico)}
    return TemplateResponse(context, 'servicos/servico_form.html')


def save(servico_id, **servico_properties):
    cmd = servico_facade.update_servico_cmd(servico_id, **servico_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'servico': servico_properties}

        return TemplateResponse(context, 'servicos/servico_form.html')
    return RedirectResponse(router.to_path(servicos))

