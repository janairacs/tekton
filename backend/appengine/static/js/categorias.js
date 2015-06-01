/**
 * Created by janairacs on 29/05/2015.
 */

$(document).ready(function () {
    var $txtInput = $('#txt-input');
    var $listaDiv = $('#lista-div');
    var $inputNeto = $("input[name='neto']");
    var $inputData = $("input[name='data']");
    var $inputAvo = $("input[name='avo']");
    var $inputVideo = $("input[name='video']");
    var $inputMensagem = $("input[name='mensagem']");
    var $ajaxImg = $('#ajax-img');
    var $categoriasLista = $('#categorias-lista');

  function adicionarPedido(recado) {

      var li = '<li id="li-' + recado.id + '" ><button id="btn-apagar-' + recado.id;
      li += '" class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button>';
      li += recado.neto + ' - ' + recado.data + ' - ' + recado.avo + ' - ' + recado.video + ' - ' + recado.mensagem + '</li>';
      $categoriasLista.append(li);

      $('#btn-apagar-' + recado.id).click(function () {
          $.post('/rest/categorias/apagar', {'recado_id': recado.id}, function () {
              $('#li-' + recado.id).remove();
          });
      });
  }


    $.get('/rest/categorias/listar', function (recados) {
        $.each(recados, function (i, recado) {
            adicionarPedido(recado);
        });

    });

    $ajaxImg.hide();

    var $msgUl = $('#msg-ul');
    var $selectRecado = $("select[name='recado']");
    var $inputNeto = $("input[name='neto']");
    var $inputData = $("input[name='data']");
    var $inputAvo = $("input[name='avo']");
    var $inputVideo = $("input[name='video']");
    var $inputMensagem = $("input[name='mensagem']");



    function obterInputs() {
        return {
            'neto': $inputNeto.val(),
            'data': $inputData.val(),
            'avo': $inputAvo.val(),
            'video': $selectVideo.val(),
            'mensagem': $selectMensagem.val()
        };
    }

    var $salvarBotao = $('#salvar-recado-btn');

    $salvarBotao.click(function () {
        $('div.has-error').removeClass('has-error');
        $('span.help-block').text('');

        $ajaxImg.fadeIn();
        $salvarBotao.attr('disabled', 'disabled');

        $.post('/rest/categorias/salvar', obterInputs(), function (recado) {
            adicionarPedido(recado);
            $('input.form-control').val('');

        }).error(function (erro) {

            var errosJson = erro.responseJSON;

            for (propriedade in  errosJson) {
                $('#' + propriedade + '-div').addClass('has-error');
                $('#' + propriedade + '-span').text(errosJson[propriedade]);
            }

        }).always(function () {
            $ajaxImg.fadeOut();
            $salvarBotao.removeAttr('disabled');
        });
    });

    $('#jq').click(function fcn(evento) {
        $listaDiv.slideToggle();
    });


    $('#jq2').click(function fcn(evento) {
        $listaDiv.empty();
    });

    $('#enviar-btn').click(function () {
        var msg = $txtInput.val();
        $txtInput.val('');
        var item = '<li>' + msg + '</li>';

        $msgUl.prepend(item);
        $msgUl.fadeOut(400, function () {
            $msgUl.fadeIn(2000);
        });
    });
});
