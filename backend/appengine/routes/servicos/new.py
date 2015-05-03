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
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'servicos/servico_form.html')


def save(**servico_properties):
    cmd = servico_facade.save_servico_cmd(**servico_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'servico': servico_properties}

        return TemplateResponse(context, 'servicos/servico_form.html')
    return RedirectResponse(router.to_path(servicos))

