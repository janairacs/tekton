# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from servico_app import servico_facade
from routes.servicos import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = servico_facade.list_servicos_cmd()
    servicos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    servico_form = servico_facade.servico_form()

    def localize_servico(servico):
        servico_dct = servico_form.fill_with_model(servico)
        servico_dct['edit_path'] = router.to_path(edit_path, servico_dct['id'])
        servico_dct['delete_path'] = router.to_path(delete_path, servico_dct['id'])
        return servico_dct

    localized_servicos = [localize_servico(servico) for servico in servicos]
    context = {'servicos': localized_servicos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'servicos/servico_home.html')


def delete(servico_id):
    servico_facade.delete_servico_cmd(servico_id)()
    return RedirectResponse(router.to_path(index))

