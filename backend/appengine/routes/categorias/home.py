from __future__ import absolute_import, unicode_literals
#from backend.appengine.categoria.categoria_model import Recado, RecadoForm
from backend.appengine.config.template_middleware import TemplateResponse
from backend.appengine.routes.categorias.edit import salvar
from gaecookie.decorator import no_csrf
from gaeforms import ndb
from recado_app.recado_commands import RecadoForm
from recado_app.recado_model import Recado
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf

def index (recado_selecionada=None):
    contexto = {'recados': Recado.query_ordenada_por_neto().fetch(),
                'salvar_path': to_path(salvar),'pesquisar_path':to_path(index)}
    if recado_selecionada is None:
        contexto['recado_selecionada']=None
    else:
        contexto['recado_selecionada']= Recado.get_by_id(int(recado_selecionada))
    return TemplateResponse(contexto,'categorias/categorias_home.html')

def salvar (**kwargs):
    form = RecadoForm(**kwargs)
    erros = form.validate()
    if not erros:
        recados = form.fill_model()
        recados.put()

def deletar(recado_id):
    key = ndb.Key( Recado, int(recado_id))
    key.delete()
    return RedirectResponse(index)