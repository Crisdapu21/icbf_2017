# -*- encoding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.models import User,Group
from operarios.models import Operario
from parametrizacion.views import registrarLogs

class Validator(object):
    _post  = None
    required = []
    _message = ''

    def __init__(self, post):
        self._post = post

    def is_empty(self, field):
        if field == '' or field is None:
            return True
        return False

    def is_valid(self):
        for field in self.required:
            if self.is_empty(self._post[field]):
                self._message = 'El campo %s no puede ser vacio' %  field
                return False
        return True

    def getMessage(self):
        return self._message


class FormLoginValidator(Validator):

    acceso = None
    def is_valid(self):
        if not super(FormLoginValidator, self).is_valid():
            return False

        correo = self._post['txtEmail']
        clave = self._post['txtPassword']

        if User.objects.filter(email=correo).exists():
            usuario = User.objects.get(email=correo)
            operario = Operario.objects.get(id = usuario.id)
            acceso = auth.authenticate(username = usuario, password = clave )
            self.acceso = acceso

            if acceso is None:
                if operario.intentos >= '1' and operario.estado != 'I':
                    operario.intentos = int(operario.intentos) - 1
                    operario.save()
                    self._message = 'CONTRASEÑA INCORRECTA\n'+'Intentos Restantes: '+ str(operario.intentos)
                    registrarLogs(usuario.first_name+' '+usuario.last_name,'INICIO DE SESSIÓN','Login','Inicio de Sessión Fallido Contraseña Incorrecta.','')
                    return False
                else:
                    operario.estado = 'I'
                    operario.save()
                    self._message = 'INTENTOS SUPERADOS\n'+'Contacta con el Administrador'
                    registrarLogs(usuario.first_name+' '+usuario.last_name,'CUENTA BLOQUEADA','Login','Intentos de Contraseña Superados.','')
                    return False
            else:
                if operario.intentos >= '1' and operario.estado != 'I':
                    operario.intentos = 5
                    operario.save()
                    registrarLogs(usuario.first_name+' '+usuario.last_name,'INICIO DE SESSIÓN','Login','Inicio de Sessión Exitoso.','')
                    return True
                else:
                    self._message = 'INTENTOS SUPERADOS\n'+'Contacta con el Administrador'
                    registrarLogs(usuario.first_name+' '+usuario.last_name,'CUENTA BLOQUEADA','Login','Intentos de Contraseña Superados.','')
                    return False
        else:
            self._message = 'El Correo NO se encuentra Registrado'
            return False

def existInGroup(id,grupo):
    if User.objects.filter(id=id, groups__name=grupo).exists():
        return True
