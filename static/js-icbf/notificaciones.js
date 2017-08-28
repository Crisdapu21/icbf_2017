
function mensagesWarning(titulo,campo,texto,duracion){
  var Notify=new PNotify({
	title:titulo,
	text: campo+' '+texto,
	type:"warning",
	addclass: "alert-styled-left",
	delay:duracion,
	animation:"fade",
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false,sticker:false},
	desktop: {desktop: true,fallback: true},
  });
  Notify.get().click(function() {
      Notify.remove();
  });
}

function mensagesSuccess(titulo,campo,texto){
  var Notify=new PNotify({
	title:titulo,
	text: campo+' '+texto,
	type:"success",
	addclass: "alert-styled-left",
	delay:2000,
	animation:"fade",
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false,sticker:false},
	desktop: {desktop: true,fallback: true},
  });
  Notify.get().click(function() {
      Notify.remove();
  });
}
function mensagesError(titulo,campo,texto){
  var Notify=new PNotify({
	title:titulo,
	text: campo+' '+texto,
	type:"error",
	addclass: "alert-styled-left",
	delay:3000,
	animation:"fade",
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false,sticker:false},
	desktop: {desktop: true,fallback: true},
  });
  Notify.get().click(function() {
      Notify.remove();
  });
}

function mensagesInfo(titulo,campo,texto,clase){
  var Notify=new PNotify({
	title:titulo,
  type: "info",
	text: campo+' '+texto,
	addclass: "alert-styled-left",
  cornerclass: clase,
	delay:6000,
  hide: true,
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false, sticker:false},
	desktop: {desktop: true, fallback: false},
  });
  Notify.get().click(function() {
    Notify.remove();
  });
}


function Notificaciones(){
  setInterval(Notificaciones, 30000);
  function Notificaciones(){
    $.ajax({
       type:'GET',
       url: '/getNotifications',
       success: function (data) {
         $.each(data, function(key, value){
            if (value.fields.tipo == "TAREAS"){
              mensagesInfo(value.fields.tipo,value.fields.detalle,'','notificacion_tareas');
            }
            if (value.fields.tipo == "PENDIENTES"){
              mensagesInfo(value.fields.nombre,value.fields.detalle,'','notificacion_pendientes');
            }
         });
       }
    });
  }
}
