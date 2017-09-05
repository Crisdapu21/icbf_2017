function MiembroFamilia(id,f3,f6,f6_detalle,f7,f7_detalle,f8,f9,f10,f13,f14,f15,f16,listS,listN,listVC,listCD,listVD,listOC,listNA,listmf_15A,listmf_15D){
  if (f8  == "S") {
      VerificarArray("mf8_"+id,listS);
  }
  if (f8 == "N") {
      VerificarArray("mf8_"+id,listN);
  }
  if (f9 == "S") {
      VerificarArray("mf9_"+id,listS);
  }
  if (f9 == "N") {
      VerificarArray("mf9_"+id,listN);
  }
  if (f13 == "1") {
      VerificarArray("mf13_"+id,listVC);
  }
  if (f13 == "2") {
      VerificarArray("mf13_"+id,listCD);
  }
  if (f13 == "3") {
      VerificarArray("mf13_"+id,listVD);
  }
  if (f13 == "4") {
      VerificarArray("mf13_"+id,listOC);
  }
  if (f13 == "5") {
      VerificarArray("mf13_"+id,listNA);
  }
  if (f14 == "S") {
      VerificarArray("mf14_"+id,listS);
  }
  if (f14 == "N") {
      VerificarArray("mf14_"+id,listN);
  }
  if (f15 == "1") {
      VerificarArray("mf15_"+id,listmf_15A);
  }
  if (f15 == "2") {
      VerificarArray("mf15_"+id,listmf_15D);
  }
  if (f3 != "None") {
      $("#mf3_"+id).text(f3)
  }
  if (f6 != "None") {
      $("#mf6_"+id).text(f6_detalle)
  }
  if (f7 != "None") {
      $("#mf7_"+id).text(f7_detalle)
  }
  if (f10 != "None") {
      $("#mf10_"+id).text(f10)
  }
  if (f16 != "None") {
      $("#mf16_"+id).text(f16)
  }
}

function AddEventos(id,estado,tipo,beneficiario,allday,detalle,f_inicio,f_fin){
  if (tipo == "PENDIENTES") {
      var title = beneficiario+'\n'+detalle
      var start = f_inicio;
      var end = f_fin;
      var colores = "#ef6c00;";
  }else{
      var title = detalle
      var start = f_inicio;
      var end = f_fin;
      var colores = "#9c4e0d;";
  }
  if (estado == "REALIZADA") {
      colores = "#888";
  }
  var e = {
        title: title,
        start: start,
        end: end,
        url: '/calendario/editar/'+id,
        allday: allday,
        color: colores
  }
  eventos.push(e);
}


function setEstadoOperario(id,estado){
    if (estado == "A"){
        VerificarArray("e"+id,listA);
    }
    if (estado == "I"){
        VerificarArray("e"+id,listI);
        $("#list"+id).append("<a onclick=activarOperario("+id+")"+" style='padding-left: 10px;' data-popup='tooltip' title='ACTIVAR OPERARIO' data-placement='top' data-original-title='ACTIVAR OPERARIO'>&nbsp;&nbsp;<li class='icon-unlocked2'></li></a>");
    }
}
function setGeneroBeneficiario(id,genero){
  if (genero == "M"){
    VerificarArray("g"+id,listM);
  }
  if (genero == "F"){
    VerificarArray("g"+id,listF);
  }
}

function setGeneroBeneficiario(id,genero){
	if (genero == "M"){
    VerificarArray("g"+id,listM);
  }
  if (genero == "F"){
    VerificarArray("g"+id,listF);
  }
}

function setTipoBeneficiario(id,tipo){
	if (tipo == "1"){
      VerificarArray("t"+id,listBH);
  }
  if (tipo == "2"){
      VerificarArray("t"+id,listBM);
  }
}

function ValidarFormulario(lista,modelo,formulario){
  var correctos =[];
  for (i=0; i<lista.length; i++) {
    if ($("#"+modelo+"_"+lista[i]).val() != ""){
      correctos.push(lista[i]);
    }else{
      validarCampos(modelo,lista[i]);
    }
  }
  if ( correctos.length == lista.length ){
    document.getElementById(formulario).submit();
  }
}

function setSelect2(campo,valor,select,multi){
  if (campo != valor){
    setMultiSelect2(select,[multi])
  }
}
function setSelect(campo,valor,select,multi){
  if (campo != valor){
    setMultiSelect(select,[multi])
  }
}

function saveMultiSelect(select,campo){
  lista = [];
  $("#"+select+" :selected").each(function (i,sel) {
    lista.push($(sel).text().toString())
  });
  $("#"+campo).val(lista)
  $("#id_"+campo).val($('#'+select).val())
}

function setMultiSelect(select,multi){
  lista = [];
  for (i=0; i<multi.length; i++) {
    lista.push(multi[i]);
  }
  $("#"+select).val(lista);
}

function setMultiSelect2(select,multi){
  lista = [];
  for (i=0; i<multi.length; i++) {
    lista.push(multi[i]);
  }
  $('#'+select).select2('val',multi);
}


function limpiarMultiSelect2(select){
  for (i=0; i<select.length; i++) {
    $('#'+select[i]).select2('val','');
  }
}

function limpiar(campos){
  for (i=0; i<campos.length; i++) {
    $('#'+campos[i]).val('');
  }
}

function obtenerRespuesta(check,campo){
  // SI YA HE SELCCIONADO UN VALOR LO GUARDO EN EL INPUT
  if ($('input:radio[name='+check+']:checked').val() == 'SI') {
      $("#"+campo).val("S");
  }
  else {
      $("#"+campo).val("N");
  }
  //OBTENER VALOR DEL RADIOBUTTON DETECTANDO EL ONCHANGE
  $('input:radio[name='+check+']').change(function() {
      if (this.value == 'SI') {
          $("#"+campo).val("S");
      }
      else if (this.value == 'NO') {
          $("#"+campo).val("N");
      }
  });
}

//FIJAR EL VALOR DEL RADIOBUTTON
function fijarRespuesta(campo,valor){
  if ($("#"+campo).val() == "S"){
    $("#"+campo+"_"+valor).prop('checked',true);
    return false;
  }
  else if ($("#"+campo).val() == "N") {
    $("#"+campo+"_"+valor).prop('checked',true);
    return false;
  }
}

// FIJA UN SELECT CON UN VALOR
function fijarValorSelect(select_id,valor){
  $("#"+select_id).val(valor);
}

// VERIFICAR QUE UN DATO EXISTA EN UN ARRAY
function VerificarArray(id,lista){
  var array = lista;
  var resultado;
  resultado = $.inArray(id,array);
  if (resultado == -1){
    lista.push(id);
  }
}

// AGREGAR UNA CLASE CSS A UN ARRAY
function AgregarClase(lista,clase){
  for (i=0; i<lista.length; i++) {
    $('#'+lista[i]).addClass(clase);
  }
}

// REMPLAZA TEXTO EN UN ARRAY
function RemplazarTexto(lista,texto){
  for (i=0; i<lista.length; i++) {
    $('#'+lista[i]).text(texto);
  }
}

// CAMBIAR ESTADO DOCUMENTO  SEGUN CHECKED
function estadoDocumento(campo,bandera,formato){
	if ($('input:checkbox[name='+bandera+']:checked').val() == "on"){
		$("#"+formato).attr('required', true);
 }
 else {
		$("#"+formato).attr('required', false);
 }
}

// VALIDAR TIPOS DE ARCHIVO
function ValidarCargaArchivos(modelo,campo,extenciones,check) {
    var _validFileExtensions = extenciones;
    var arrInputs =  $("#"+modelo+"_"+campo);
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }
                if (!blnValid) {
                    $("#"+modelo+"_"+campo+"_success").hide();
                    $("#"+modelo+"_"+campo+"_error").show();
                    $("#"+modelo+"_"+campo).val("")
                    $(".filename").val("")
                    return false;
                }
            }
        }
    }
    $("#"+modelo+"_"+campo+"_error").hide();
    $("#"+modelo+"_"+campo+"_success").show();
    $("#checkDNI").prop("checked", true);
    return true;
}


// INPUT QUE SOLO ACEPTA NUMEROS
function soloNumeros(e,modelo,id,bandera){
  if (bandera != "NO"){
	   validarCampos(modelo,id);
  }
	var key = window.Event ? e.which : e.keyCode
	return (key >= 48 && key <= 57)
}

// BLOQUEAR INTERFAZ CUANDO SE ENVIAN MULTIPLES PETICIONES AL SERVIDOR (MULTIPLE BORRADO, MULTIPLE EDICION)
function blockPanel(mensaje){
  $.blockUI({
      message: '<i class="icon-spinner10 spinner"></i><div id="custom-message" class="block_ui_font display-block">'+mensaje+'</div>',
      overlayCSS: {
          backgroundColor: '#1b2024',
          opacity: 0.9,
          cursor: 'wait',

      },
      css: {
          border: 0,
          color: 'white',
          padding: 0,
          backgroundColor: 'transparent',
					left: '30%',
					width: '41%',

      }
  });
}


//FUNCION GENERICA PARA BORRAR
function eliminar(url,id,mensaje) {
  var Notify=new PNotify({
  	title: 'ATENCIÓN:',
  	text: 'Una vez eliminado el elemento no podra recuperarse. ¿Esta Seguro?',
    type:"warning",
    addclass: "alert-styled-left",
  	hide: false,
  	confirm: {
  		confirm: true
  	},
  	buttons: {
  		closer: false,
  		sticker: false
  	},
  	history: {
  		history: false
  	}
  }).get().on('pnotify.confirm', function() {
    $.ajax({
        method: "DELETE",
        url: url + id,
    }).done(function (msg) {
        blockPanel(mensaje);
        location.reload();
    });
  }).on('pnotify.cancel', function() {
  })
}

function obtenerGenero(){
	// SI YA HE SELCCIONADO UN VALOR LO GUARDO EN EL INPUT
	if ($('input:radio[name=bedStatus]:checked').val() == 'masculino') {
			$("#genero").val("M");
      fijarGenero();
	}
	else if ($('input:radio[name=bedStatus]:checked').val() == 'femenino') {
			$("#genero").val("F");
      fijarGenero();
	}
	//OBTENER VALOR DEL RADIOBUTTON DETECTANDO EL ONCHANGE
	$('input:radio[name=bedStatus]').change(function() {
			if (this.value == 'masculino') {
					$("#genero").val("M");
          fijarGenero();
			}
			else if (this.value == 'femenino') {
					$("#genero").val("F");
          fijarGenero()
			}
	});

}
//FIJAR EL VALOR DEL RADIOBUTTON
function fijarGenero(){
  if ($("#genero").val() == "M"){
		$( "#masculino" ).prop( "checked", true );
	}
	else if ($("#genero").val() == "F") {
		$( "#femenino" ).prop( "checked", true );
	}
}


//SUBIR IMAGEN
function subirImagen() {
  document.getElementById('archivo').click();
}

$(function() {
  $('#archivo').change(function(e) {
    addImage(e);
  });

   function addImage(e){
    var file = e.target.files[0],
    imageType = /image.*/;

    if (!file.type.match(imageType))
     return;

    var reader = new FileReader();
    reader.onload = fileOnload;
    reader.readAsDataURL(file);
   }

   function fileOnload(e) {
    var result=e.target.result;
    $('#imgSalida').attr("src",result);
		$('#bandera_foto').val("CAMBIO")
   }
});


function adicionarNotas(){
	contacto_id= ($("#contacto_id").val());
	txt_notas = ($("#detallenotas").val().trim());
  validarCampos("notas","detallenotas");
  if (txt_notas != ""){
  	$.ajax({
  	method: "PUT",
  	url: "/guardarNota?contacto_id="+contacto_id+"&txt_notas="+txt_notas,
  	}).done(function( msg ) {
  		 if (msg == "Creada") {
         location.reload();
  			}
  	});
  }
}


function validarCampos(modelo,campo){
  if ($("#"+modelo+"_"+campo).val() == ""){
    $("#"+modelo+"_"+campo).focus();
    $("#"+modelo+"_"+campo+"_success").hide();
    $("#"+modelo+"_"+campo+"_error").show();
  }
  else{
    $("#"+modelo+"_"+campo+"_error").hide();
    $("#"+modelo+"_"+campo+"_success").show();

  }
}


// ACTIVAR OPERARIO
function activarOperario(id) {
		$.ajax({
  		method: "PUT",
  		url: "/activarOperario?id="+id,
  		}).done(function( msg ) {
        mensagesSuccess('EXITO AL ACTIVAR','Operario Activado','Exitosamente')
        setTimeout(function(){
          location.reload();
        }, 3000);
  		});
}

// VERIFICA QUE NO EXISTA EL EMAIL
function verificarEmail() {
		email=($("#email").val());
		$.ajax({
		method: "PUT",
		url: "/verificarEmail?email="+email,
		}).done(function( msg ) {
			if (msg == "Campos Correctos") {
			}
			else if (msg == "El E-MAIL ya Existe"){
					$("#email").focus();
					var str = $("#email").val();
					var ultimo = str.length-1;
					var res = str.substring(0, ultimo);
					$("#email").val(res);
					mensagesError("ERROR:      "+email,"El E-mail","ya Existe.");
				}
		});
}


function EliminarArray(id,lista){
  var array = lista;
  var resultado;
  resultado = $.inArray(id,array);
  if (resultado >= 0){
    lista.splice(resultado,1);
  }
}

var lista_check1 = []
var lista_check2 = []
var lista_check3 = []
var lista_check4 = []
var lista_check5 = []
var lista_check6 = []
var lista_check7 = []
var lista_check8 = []
var lista_check9 = []

function guardarCheckbox(check, campo, listaCheck){
	if (listaCheck == 'lista_check1'){
		lista = lista_check1
  }
  if (listaCheck == 'lista_check2'){
    lista = lista_check2
  }
  if (listaCheck == 'lista_check3'){
    lista = lista_check3
  }
  if (listaCheck == 'lista_check4'){
    lista = lista_check4
  }
  if (listaCheck == 'lista_check5'){
    lista = lista_check5
  }
  if (listaCheck == 'lista_check6'){
    lista = lista_check6
  }
  if (listaCheck == 'lista_check7'){
    lista = lista_check8
  }
  if (listaCheck == 'lista_check8'){
    lista = lista_check8
  }
  if (listaCheck == 'lista_check9'){
    lista = lista_check9
  }

  if(check.checked){
    VerificarArray(check.value,lista)
    $("#"+campo).val(lista)
  }else{
    EliminarArray(check.value,lista)
    $("#"+campo).val(lista)
  }
}

// FIJA LOS CHECKED RECIBIENDO UNA STTRING CONVIRTIENDOLO ARRAY
function setChek(list_check,campo){
  var list = list_check.split(",");
	for (i=0; i<list.length; i++) {
  	$("#"+list[i]).prop( "checked", true );
    $("#"+campo).val(list)
    lista_check1.push(list[i])
	}
}

// CAMBIAR ESTADO SEGUN CHECKED
function changeEstado(campo,bandera){
  if ($('input:checkbox[name='+bandera+']:checked').val() == "on"){
    $("#"+campo).val("REALIZADA");
	}
	else {
    $("#"+campo).val("NO REALIZADA");
	}
}

// FIJA EL ESTADO DEL EVENTO CON LO QUE LLEGA DE LA DB Y LO CAMBIA DE COLOR
function setEstado(campo,bandera,header,color,newcolor,formulario,buttton){
    if ($("#"+campo).val() == "REALIZADA"){
        $("#"+bandera).attr('checked','checked');
        $("#"+header).removeClass("modal-header "+color).addClass("modal-header "+newcolor);
        $("#"+formulario).addClass(newcolor);
        $("#"+buttton).addClass(newcolor);
    }else{
        $("#"+campo).removeAttr('checked');
    }
}
