#from backend.appengine.categoria.categoria_model import Recado, RecadoForm
from backend.appengine.config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from recado_app.recado_commands import RecadoForm
from recado_app.recado_model import Recado
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index (recado_id):
    recado = Recado.get_by_id (int(recado_id))
    contexto={ 'recado': recado,
               'salvar_path':to_path(salvar)}
    return TemplateResponse(contexto,'categorias/categorias_form.html')

def salvar(recado_id, **kwargs):
    recados = Recado.get_by_id(recado_id)
    recado = RecadoForm (**kwargs)
    recado.put()
    return RedirectResponse(recados)
