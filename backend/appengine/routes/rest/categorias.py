from categoria.categoria_model import Categoria, CategoriaForm
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


@login_not_required
@no_csrf
def listar():
    form = CategoriaForm ()
    recados = Categoria.query_ordenada_por_nome().fetch()
    recados = [form.fill_with_model (p) for p in recados]
    return JsonUnsecureResponse(recados)

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = CategoriaForm (**propriedades)
    erros = form.validate()

    if not erros:
        recado = form.fill_model()
        recado.put()
        dct = form.fill_model(recado)
        return JsonUnsecureResponse(dct)
    _resp.set_status(400)
    return JsonUnsecureResponse (erros)
