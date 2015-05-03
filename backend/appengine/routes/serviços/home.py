# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from servico_app import servico_facade
from routes import admin


@login_not_required
@no_csrf
def index():
    cmd = servico_facade.list_servicos_cmd()
    servicos = cmd()
    public_form = servico_facade.servico_public_form()
    servico_public_dcts = [public_form.fill_with_model(servico) for servico in servicos]
    context = {'servicos': servico_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)