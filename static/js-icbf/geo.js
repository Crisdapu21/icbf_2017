
function limpiarSelects(params) {
  for (i=0; i<params.length; i++) {
      $('#'+params[i]).children('option:not(:first)').remove();
      $('#'+params[i]).select2().select2('val',"");
  }
}


function paises(campoPais,campoDep,campoCiu){
    if ($("#"+campoPais).val() !=""){
        traerDepartamentos($("#"+campoPais).val(),campoDep,campoCiu);
    }
    else{
      list = [campoDep,campoCiu]
      limpiarSelects(list);
  }
}

function departamentos(campoDep,campoCiu) {
  if ($("#"+campoDep).val() !=""){
      traerCiudades($("#"+campoDep).val(),campoCiu);
  }
  else{
    list = [campoCiu]
    limpiarSelects(list);
  }
}

function traerDepartamentos(pais,campoDep,campoCiu,departamento) {
    list = [campoCiu,campoDep]
    limpiarSelects(list);
    $.ajax({
        url: '/ajaxDepartamentos?pais='+pais,
        type: 'GET',
        success: function(data) {
            for (var i = 0; i < data.length; i++) {
                $("#"+campoDep).append("<option value='" + data[i].pk + "'>" + data[i].fields.departamento + "</option>");
            }
            $("#"+campoCiu+">option[value="+departamento+"]").attr("selected", "selected");
        }
    });
}

function traerCiudades(departamento,campoCiu) {
    list = [campoCiu]
    limpiarSelects(list);
    $.ajax({
        url: '/ajaxCiudades?departamento='+departamento,
        type: 'GET',
        success: function(data) {
            for (var i = 0; i < data.length; i++) {
                $("#"+campoCiu).append("<option value='" + data[i].pk + "'>" + data[i].fields.ciudad + "</option>");
            }
        }
    });
}
