from __future__ import absolute_import,unicode_literals
#from backend.appengine.categoria.categoria_model import RecadoForm, Recado
from backend.appengine.config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
#from config.template_middleware import TemplateResponse
from recado_app.recado_commands import RecadoForm
from recado_app.recado_model import Recado
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def salvar (**kwargs):
    form = RecadoForm (**kwargs)
    erros=form.validade()


    if not erros:
        valores_normalizados = form.normalize()
        recado = Recado(**valores_normalizados)
        recado.put()
        return RedirectResponse(recado)
    else:
        contexto = {'recado': kwargs, 'erros':erros}
        return TemplateResponse(contexto,'categorias/categorias_form.html') # criar templeiiiite categoria



