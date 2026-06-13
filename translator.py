#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TRADUCTOR VPS-BARBA - Modo "Vulgar y Callejero"
Traducción directa, sin mamadas, con el lenguaje que se usa en la puta calle.
El dueño de este desmadre lo habla así, y así se queda.
"""

import os
import re
import subprocess
import sys

# Colores de la verga (pa' que se vea chingón)
RESET = "\033[0m"
RED = "\033[38;5;214m"
GREEN = "\033[38;5;82m"
YELLOW = "\033[38;5;220m"
BLUE = "\033[1;34m"
PURPLE = "\033[38;5;213m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
BARRA = "\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m"

# ==============================================
# DICCIONARIO DE ESPAÑOL DE BARRIO (BIEN VERGA)
# ==============================================
# Esto es lo que realmente se dice en la calle, sin mamadas.
# Si no te gusta, chingas a tu madre, pero así lo quiere el creador.

DICCIONARIO_ES = {
    # ==========================================
    # MENÚ PRINCIPAL - El jefe de este desmadre
    # ==========================================
    "ADMINISTRADOR": "EL PINCHE JEFE",
    "ADMINISTRADOR DE SERVICIOS": "EL QUE CONTROLA ESTA MADRE",
    "GESTIONAR USUARIOS": "MANEJAR A LOS WEYES",
    "HERRAMIENTAS": "HERRAMIENTAS DE LA VERGA",
    "ACTUALIZAR": "ACTUALIZAR ESTA CHINGADERA",
    "ACTUALIZANDO SISTEMA...": "PONIENDO AL DÍA ESTE PEDO...",
    "Sistema actualizado": "EL SISTEMA YA QUEDÓ AL DÍA, WEY",
    "DESINSTALAR VPS BARBA": "BORRAR ESTE VPS DEL ORTO",
    "¿Está seguro de desinstalar VPS-BARBA? (s/n)": "¿SEGURO QUIERES BORRAR ESTA VERGA? (s/n)",
    "VPS-BARBA ha sido desinstalado": "VPS-BARBA YA VALIÓ MADRE",
    "CONTROL DE USUARIOS CONECTADOS": "VER A LOS WEYES CONECTADOS",
    "Usuarios conectados": "COMPAS CONECTADOS",
    "Usuarios logueados": "COMPAS METIDOS",
    "Últimos accesos": "LOS ÚLTIMOS EN CAER",
    "Intentos fallidos": "LOS QUE TRATARON Y VALIERON VERGA",
    "No hay datos": "NO HAY NADA, WEY",
    "CAMBIAR IDIOMA": "CAMBIAR EL PINCHI IDIOMA",
    "AUTO-INICIO DEL SCRIPT": "QUE EL SCRIPT ARRANQUE SOLO",
    "Auto-inicio activado": "YA ARRANCA SOLO, CABRÓN",
    "Auto-inicio desactivado": "HAY QUE PRENDERLO A MANO",
    "CREDITOS DEL SCRIPT": "LOS PINCHE CRÉDITOS",
    "Script de administración para VPS": "CHINGADERA PA' CONTROLAR EL VPS",
    "Autor": "EL QUE LA HIZO",
    "Versión": "VERSIÓN",
    "Funcionalidades": "LO QUE HACE ESTA MADRE",
    "Gestión de usuarios": "MANEJAR A LOS WEYES",
    "Administración de servicios": "CONTROLAR LOS SERVICIOS",
    "Herramientas del sistema": "HERRAMIENTAS DEL SISTEMA",
    "Optimización del sistema": "PONER MÁS RÁPIDO ESTE PEDO",
    "Traducción multi-idioma": "TRADUCIR EN VARIOS IDIOMAS",
    "Enter para Continuar": "DALE ENTER PA' SEGUIR, WEY",
    "Seleccione una Opcion": "ELIGE UNA OPCIÓN, VERGA",
    "SALIR": "ABRIRSE ALV",
    "Traductor": "EL TRADUCTOR",
    "Idioma cambiado correctamente": "YA CAMBIÓ EL IDIOMA, WEY",
    "Seleccione una opción": "ELIGE UNA OPCIÓN",
    "Opción inválida": "ESA OPCIÓN NO SIRVE, WEY",
    "VOLVER AL MENÚ PRINCIPAL": "REGRESAR AL MENÚ PRINCIPAL",
    "REGRESAR": "REGRESAR",
    "VOLVER": "VOLVER",
    "SALIENDO...": "ABRIÉNDOME, WEY...",

    # ==========================================
    # GESTIÓN DE USUARIOS - Pa' la bandita
    # ==========================================
    "CREAR NUEVO USUARIO": "AGREGAR UN COMPA NUEVO",
    "ELIMINAR USUARIO": "SACAR A UN WEY DEL SISTEMA",
    "EDITAR USUARIO": "CAMBIRLE LOS DATOS AL COMPA",
    "RENOVAR USUARIO": "DARLE MÁS TIEMPO AL MORRO",
    "DETALLES DE TODOS LOS USUARIOS": "VER A TODA LA BANDA",
    "MONITOR DE USUARIOS CONECTADOS": "CHECAR QUIÉN ANDA POR AHÍ",
    "ELIMINAR USUARIOS VENCIDOS": "BORRAR A LOS QUE YA CADUCARON",
    "BACKUP DE USUARIOS": "GUARDAR LA INFO DE LA BANDA",
    "BANNER SSH": "LA MAMALONA DE BIENVENIDA",
    "VERIFICACIONES": "VERIFICACIONES",
    "GESTIÓN DE USUARIOS": "MANEJAR A LOS WEYES",
    "USUARIO NULO": "EL NOMBRE NO SIRVE, WEY",
    "USUARIO CON NOMBRE MUY CORTO": "EL NOMBRE ESTÁ MUY CHIQUITO",
    "USUARIO CON NOMBRE MUY GRANDE": "EL NOMBRE ESTÁ MUY LARGO",
    "USUARIO YA EXISTE": "ESE WEY YA ESTÁ REGISTRADO",
    "CONTRASEÑA NULA": "LA CONTRASEÑA NO SIRVE",
    "CONTRASEÑA MUY CORTA": "LA CONTRASEÑA ESTÁ MUY CHIQUITA",
    "CONTRASEÑA MUY GRANDE": "LA CONTRASEÑA ESTÁ MUY LARGA",
    "DURACIÓN NULA": "LOS DÍAS NO SIRVEN",
    "DURACIÓN INVÁLIDA, USE NÚMEROS": "PON SOLO NÚMEROS, CABRÓN",
    "DURACIÓN MÁXIMA ES DE UN AÑO": "NO PUEDE PASAR DE UN AÑO",
    "LÍMITE NULO": "EL LÍMITE NO SIRVE",
    "LÍMITE INVÁLIDO, USE NÚMEROS": "PON SOLO NÚMEROS EN EL LÍMITE",
    "LÍMITE MÁXIMO ES DE 999": "EL LÍMITE MÁXIMO ES 999",
    "NOMBRE DEL NUEVO USUARIO": "NOMBRE DEL COMPA NUEVO",
    "CONTRASEÑA DEL NUEVO USUARIO": "LA CLAVE DEL COMPA NUEVO",
    "DÍAS DE DURACIÓN DEL NUEVO USUARIO": "DÍAS QUE VA A DURAR EL COMPA",
    "LÍMITE DE CONEXIÓN DEL NUEVO USUARIO": "CUÁNTAS CONEXIONES PUEDE TENER EL COMPA",
    "IP DEL SERVIDOR": "LA IP DEL SERVIDOR",
    "USUARIO": "COMPA",
    "CONTRASEÑA": "CLAVE",
    "DÍAS DE DURACIÓN": "DÍAS",
    "FECHA DE EXPIRACIÓN": "FECHA DE CADUCIDAD",
    "LÍMITE DE CONEXIÓN": "CONEXIONES MÁXIMAS",
    "USUARIO CREADO CON ÉXITO": "EL COMPA QUEDÓ REGISTRADO, WEY",
    "ERROR, USUARIO NO CREADO": "VALIÓ VERGA, NO SE PUDO CREAR",
    "USUARIO SELECCIONADO": "EL COMPA ELEGIDO",
    "ELIMINADO": "SACADO",
    "NO ELIMINADO": "NO SE PUDO SACAR",
    "NUEVOS DÍAS DE DURACIÓN PARA": "DÍAS NUEVOS PARA",
    "USUARIO MODIFICADO CON ÉXITO": "EL COMPA QUEDÓ MODIFICADO",
    "ERROR, USUARIO NO MODIFICADO": "VALIÓ MADRE, NO SE PUDO MODIFICAR",
    "EXPIRADO": "EXPIRADO",
    "USUARIO VÁLIDO": "USUARIO VÁLIDO",
    "USUARIO ILIMITADO": "SIN LÍMITE",
    "HERRAMIENTA DE BACKUP DE USUARIOS": "RESPALDO DE USUARIOS",
    "CREAR BACKUP": "CREAR RESPALDO",
    "RESTAURAR BACKUP": "RESTAURAR RESPALDO",
    "PROCEDIMIENTO REALIZADO": "PROCEDIMIENTO REALIZADO",
    "RUTA DEL BACKUP": "RUTA DEL RESPALDO",
    "VERIFICACIÓN INICIADA": "VERIFICACIÓN INICIADA",
    "VERIFICACIÓN DETENIDA": "VERIFICACIÓN DETENIDA",
    "BIENVENIDO, ESTE ES EL INSTALADOR DE BANNER": "BIENVENIDO, INSTALADOR DE BANNER",
    "MENSAJE PRINCIPAL DEL BANNER": "MENSAJE PRINCIPAL",
    "VERDE": "VERDE",
    "ROJO": "ROJO",
    "AZUL": "AZUL",
    "AMARILLO": "AMARILLO",
    "MORADO": "MORADO",
    "COLOR": "COLOR",
    "AGREGAR MENSAJE SECUNDARIO": "AGREGAR MENSAJE SECUNDARIO",
    "MENSAJE SECUNDARIO": "MENSAJE SECUNDARIO",
    "BANNER AGREGADO CON ÉXITO": "BANNER AGREGADO",
    "Ningún usuario registrado": "NO HAY WEYES REGISTRADOS",
    "Usuarios actualmente activos en el servidor": "WEYES ACTIVOS EN EL SERVIDOR",
    "Digite o seleccione un usuario": "ESCRIBE O SELECCIONA UN WEY",
    "Error, usuario inválido": "ERROR, ESE WEY NO SIRVE",

    # ==========================================
    # SERVICIOS - Los chingaderos del sistema
    # ==========================================
    "SERVICIO": "SERVICIO",
    "ESTADO": "ESTADO",
    "INSTALACIÓN": "INSTALACIÓN",
    "ACTIVO": "ACTIVO",
    "INACTIVO": "INACTIVO",
    "INSTALADO": "INSTALADO",
    "NO INSTALADO": "NO INSTALADO",
    "INSTALAR": "INSTALAR",
    "INICIAR": "INICIAR",
    "DETENER": "DETENER",
    "REINICIAR": "REINICIAR",
    "VER CONFIGURACIÓN": "VER CONFIGURACIÓN",
    "DESINSTALAR": "DESINSTALAR",
    "INSTALACIÓN COMPLETADA": "INSTALACIÓN COMPLETADA",
    "SERVICIO INICIADO": "SERVICIO INICIADO",
    "SERVICIO DETENIDO": "SERVICIO DETENIDO",
    "SERVICIO REINICIADO": "SERVICIO REINICIADO",
    "CONFIGURACIÓN DEL SERVICIO": "CONFIGURACIÓN DEL SERVICIO",
    "NO HAY CONFIGURACIÓN ESPECÍFICA PARA MOSTRAR": "NO HAY CONFIGURACIÓN ESPECÍFICA",
    "¿Desinstalar": "¿DESINSTALAR",
    "DESINSTALACIÓN COMPLETADA": "DESINSTALACIÓN COMPLETADA",
    "SSH": "SSH",
    "SQUID PROXY": "SQUID PROXY",
    "DROPBEAR": "DROPBEAR",
    "SSL STUNNEL": "SSL STUNNEL",
    "FAIL2BAN": "FAIL2BAN",
    "APACHE2": "APACHE2",
    "NGINX": "NGINX",
    "MYSQL": "MYSQL",
    "OPENVPN": "OPENVPN",
    "XRAY / V2RAY": "XRAY / V2RAY",
    "WEBMIN": "WEBMIN",
    "VER SERVICIOS ESCUCHANDO": "VER SERVICIOS ESCUCHANDO",
    "PROXY SOCKS PYTHON": "PROXY SOCKS PYTHON",
    "SERVICIOS ESCUCHANDO (LISTEN)": "SERVICIOS ESCUCHANDO",
    "Puerto": "PUERTO",
    "Puertos": "PUERTOS",
    "activos": "ACTIVOS",
    "TOTAL DE SERVICIOS ACTIVOS": "TOTAL DE SERVICIOS ACTIVOS",
    "DETENIENDO SSL TUNNEL ANTERIOR...": "DETENIENDO SSL TUNNEL...",
    "¡Detenido con éxito!": "DETENIDO, WEY",
    "INICIANDO INSTALACIÓN AUTOMÁTICA SSL VPS-BARBA": "INSTALANDO SSL AUTOMÁTICO",
    "Buscando puerto Dropbear...": "BUSCANDO PUERTO DROPBEAR...",
    "Dropbear no detectado activo. Buscando puertos alternativos...": "DROPBEAR NO ACTIVO, BUSCANDO OTROS PUERTOS...",
    "Redirección Interna (Puerto-Local) asignada:": "PUERTO LOCAL ASIGNADO:",
    "Puerto SSL (Listen-SSL) asignado automáticamente:": "PUERTO SSL ASIGNADO:",
    "Instalando SSL...": "INSTALANDO SSL...",
    "INSTALADO Y CONFIGURADO CON ÉXITO": "INSTALADO Y CONFIGURADO",
    "SSL escuchando en el puerto:": "SSL ESCUCHANDO EN PUERTO:",
    "Redireccionando internamente al puerto:": "REDIRIGIENDO A PUERTO:",
    "DESINSTALANDO DROPBEAR POR COMPLETO": "DESINSTALANDO DROPBEAR",
    "DROPBEAR DESINSTALADO COMPLETAMENTE": "DROPBEAR DESINSTALADO",
    "INSTALANDO DROPBEAR EN EL PUERTO 443": "INSTALANDO DROPBEAR EN PUERTO 443",
    "EN USO, no se utilizará": "PUERTO EN USO",
    "Error: El puerto 443 ya está ocupado por otro servicio.": "ERROR: PUERTO 443 OCUPADO",
    "Instalando dropbear...": "INSTALANDO DROPBEAR...",
    "Configurando dropbear solo en el puerto 443...": "CONFIGURANDO DROPBEAR EN PUERTO 443...",
    "REINICIANDO SERVICIOS": "REINICIANDO SERVICIOS",
    "DROPBEAR CONFIGURADO CON ÉXITO": "DROPBEAR CONFIGURADO",
    "PUERTO:": "PUERTO:",
    "DROPBEAR INSTALADO PERO CON ERRORES": "DROPBEAR INSTALADO CON ERRORES",
    "CONFIGURACIÓN DE DROPBEAR": "CONFIGURACIÓN DE DROPBEAR",
    "REMOVIENDO SQUID POR COMPLETO": "ELIMINANDO SQUID",
    "SQUID REMOVIDO COMPLETAMENTE": "SQUID ELIMINADO",
    "SQUID CONFIGURADO": "SQUID CONFIGURADO",
    "AÑADIR HOST A SQUID": "AÑADIR HOST A SQUID",
    "REMOVER HOST DE SQUID": "ELIMINAR HOST DE SQUID",
    "ELIMINAR SQUID (LIMPIEZA TOTAL)": "ELIMINAR SQUID",
    "Hosts Actuales dentro de Squid": "HOSTS ACTUALES",
    "Escribe el nuevo host": "NUEVO HOST",
    "Comienza con un punto (.)": "COMIENZA CON PUNTO (.)",
    "El host ya existe": "EL HOST YA EXISTE",
    "Host Añadido con Éxito": "HOST AÑADIDO",
    "Introduce un Host": "INTRODUCE UN HOST",
    "Host No Encontrado": "HOST NO ENCONTRADO",
    "Host Removido con Éxito": "HOST ELIMINADO",
    "CONFIGURACIÓN AUTOMÁTICA DE SQUID": "CONFIGURACIÓN AUTOMÁTICA DE SQUID",
    "SOPORTE: UBUNTU 18.04 A 25.10": "SOPORTE UBUNTU 18.04 A 25.10",
    "ACTUALIZANDO REPOSITORIOS": "ACTUALIZANDO REPOSITORIOS",
    "INSTALANDO VERSIÓN ESTÁNDAR DE SQUID": "INSTALANDO SQUID ESTÁNDAR",
    "CONFIGURADO CON ÉXITO": "CONFIGURADO",
    "PUERTO: 3128": "PUERTO: 3128",
    "WEBMIN YA ESTÁ INSTALADO": "WEBMIN YA INSTALADO",
    "ABRIR WEBMIN EN NAVEGADOR": "ABRIR WEBMIN",
    "REINICIAR WEBMIN": "REINICIAR WEBMIN",
    "CAMBIAR PUERTO WEBMIN": "CAMBIAR PUERTO WEBMIN",
    "Nuevo puerto para Webmin": "NUEVO PUERTO",
    "Puerto inválido": "PUERTO INVÁLIDO",
    "Puerto cambiado a": "PUERTO CAMBIADO A",
    "Webmin desinstalado correctamente": "WEBMIN DESINSTALADO",
    "INSTALADOR WEBMIN": "INSTALADOR WEBMIN",
    "¿Desea instalar Webmin? (s/n)": "¿INSTALAR WEBMIN? (s/n)",
    "INSTALANDO WEBMIN...": "INSTALANDO WEBMIN...",
    "AGREGANDO REPOSITORIO WEBMIN": "AGREGANDO REPOSITORIO WEBMIN",
    "ACCESO WEBMIN": "ACCESO WEBMIN",
    "Usuario: root": "USUARIO: ROOT",
    "Contraseña: (tu contraseña de root)": "CONTRASEÑA: (TU CLAVE ROOT)",
    "WEBMIN INSTALADO Y CONFIGURADO CON ÉXITO": "WEBMIN INSTALADO Y CONFIGURADO",
    "GESTOR DE PROXY SOCKS PYTHON": "GESTOR DE PROXY SOCKS PYTHON",
    "SOCKS PYTHON SIMPLES": "SOCKS SIMPLE",
    "SOCKS PYTHON SEGURO": "SOCKS SEGURO",
    "SOCKS PYTHON DIRECT": "SOCKS DIRECTO",
    "SOCKS PYTHON OPENVPN": "SOCKS OPENVPN",
    "SOCKS PYTHON GETTUNEL": "GETTUNEL",
    "SOCKS PYTHON TCP BYPASS": "TCP BYPASS",
    "PARAR TODOS LOS SOCKETS": "PARAR TODOS LOS SOCKS",
    "CONFIGURACIÓN DEL PROXY SOCKS": "CONFIGURACIÓN PROXY SOCKS",
    "Puerto para el proxy": "PUERTO DEL PROXY",
    "Texto de bienvenida": "TEXTO DE BIENVENIDA",
    "INICIANDO PROXY": "INICIANDO PROXY",
    "PROXY SIMPLES | PUERTO:": "PROXY SIMPLE | PUERTO:",
    "PROXY SEGURO | PUERTO:": "PROXY SEGURO | PUERTO:",
    "PROXY DIRECT | PUERTO:": "PROXY DIRECTO | PUERTO:",
    "PROXY OPENVPN | PUERTO:": "PROXY OPENVPN | PUERTO:",
    "TCP BYPASS | PUERTO:": "TCP BYPASS | PUERTO:",
    "PARANDO TODOS LOS SOCKETS PYTHON": "PARANDO TODOS LOS SOCKS",
    "TODOS LOS SOCKETS HAN SIDO DETENIDOS": "TODOS LOS SOCKS DETENIDOS",
    "ENCENDIDO": "ENCENDIDO",
    "APAGADO": "APAGADO",
    "GETTUNEL INICIADO CON ÉXITO": "GETTUNEL INICIADO",
    "GETTUNEL NO HA SIDO INICIADO": "GETTUNEL NO INICIADO",
    "Contraseña:": "CONTRASEÑA:",

    # ==========================================
    # HERRAMIENTAS - Las mamadas útiles
    # ==========================================
    "CREANDO BACKUP...": "CREANDO RESPALDO...",
    "BACKUP CREADO EN:": "RESPALDO CREADO EN:",
    "BACKUPS DISPONIBLES": "RESPALDOS DISPONIBLES",
    "No hay backups disponibles": "NO HAY RESPALDOS",
    "Seleccione backup": "SELECCIONA RESPALDO",
    "Backup restaurado correctamente": "RESPALDO RESTAURADO",
    "LIMPIANDO CACHE...": "LIMPIANDO CACHE...",
    "Cache de traducciones eliminado": "CACHE DE TRADUCCIONES ELIMINADO",
    "Cache del sistema limpiada": "CACHE DEL SISTEMA LIMPIA",
    "BADUDP - INSTALADOR": "BADUDP - INSTALADOR",
    "Instalar BadUDP": "INSTALAR BADUDP",
    "Iniciar BadUDP": "INICIAR BADUDP",
    "Detener BadUDP": "DETENER BADUDP",
    "Configurar Puerto": "CONFIGURAR PUERTO",
    "BadUDP instalado correctamente": "BADUDP INSTALADO",
    "BadUDP iniciado en puerto 7300": "BADUDP INICIADO EN PUERTO 7300",
    "BadUDP detenido": "BADUDP DETENIDO",
    "BadUDP configurado en puerto": "BADUDP CONFIGURADO EN PUERTO",
    "TCP SPEED - OPTIMIZACIÓN": "OPTIMIZACIÓN TCP",
    "Optimización TCP aplicada (BBR activado)": "OPTIMIZACIÓN TCP APLICADA (BBR ACTIVADO)",
    "FAIL2BAN - INSTALACIÓN": "FAIL2BAN - INSTALACIÓN",
    "Fail2ban instalado y activado": "FAIL2BAN INSTALADO Y ACTIVADO",
    "Fail2ban ya está instalado": "FAIL2BAN YA INSTALADO",
    "Reiniciar Fail2ban": "REINICIAR FAIL2BAN",
    "Ver estado": "VER ESTADO",
    "Ver bans": "VER BANEADOS",
    "ARCHIVO EN LÍNEA": "ARCHIVO EN LÍNEA",
    "SUBIR ARCHIVO": "SUBIR ARCHIVO",
    "REMOVER ARCHIVO ONLINE": "ELIMINAR ARCHIVO ONLINE",
    "VER LINKS DE ARCHIVOS ONLINE": "VER LINKS DE ARCHIVOS",
    "No hay archivos en el directorio HOME": "NO HAY ARCHIVOS EN HOME",
    "No hay archivos disponibles para subir": "NO HAY ARCHIVOS PARA SUBIR",
    "Seleccione el archivo a subir": "SELECCIONA ARCHIVO A SUBIR",
    "Archivo subido con éxito": "ARCHIVO SUBIDO",
    "No hay archivos online": "NO HAY ARCHIVOS ONLINE",
    "No hay archivos para remover": "NO HAY ARCHIVOS PARA ELIMINAR",
    "Seleccione el archivo a remover": "SELECCIONA ARCHIVO A ELIMINAR",
    "Archivo removido con éxito": "ARCHIVO ELIMINADO",
    "LINKS DE ARCHIVOS ONLINE": "LINKS DE ARCHIVOS",
    "TEST DE VELOCIDAD": "TEST DE VELOCIDAD",
    "Instalando speedtest...": "INSTALANDO SPEEDTEST...",
    "INFORMACIÓN DEL VPS": "INFORMACIÓN DEL VPS",
    "No disponible": "NO DISPONIBLE",
    "GENERADOR DE PAYLOAD": "GENERADOR DE PAYLOAD",
    "DOMINIO/IP:": "DOMINIO/IP:",
    "MÉTODO (GET/CONNECT/POST):": "MÉTODO (GET/CONNECT/POST):",
    "PAYLOADS GENERADOS": "PAYLOADS GENERADOS",
    "GESTIÓN DE PUERTOS": "GESTIÓN DE PUERTOS",
    "Puertos abiertos": "PUERTOS ABIERTOS",
    "Abrir puerto": "ABRIR PUERTO",
    "Cerrar puerto": "CERRAR PUERTO",
    "Escaneo de puertos": "ESCANEO DE PUERTOS",
    "IP a escanear": "IP A ESCANEAR",
    "Puerto inicial": "PUERTO INICIAL",
    "Puerto final": "PUERTO FINAL",
    "Puerto abierto": "PUERTO ABIERTO",
    "Puerto cerrado": "PUERTO CERRADO",
    "SCANNER DE SUBDOMINIOS": "ESCÁNER DE SUBDOMINIOS",
    "Buscando subdominios...": "BUSCANDO SUBDOMINIOS...",
    "VNC SERVER - INSTALACIÓN": "VNC SERVER - INSTALACIÓN",
    "VNC instalado. Configure contraseña:": "VNC INSTALADO. CONFIGURA CONTRASEÑA:",
    "VNC ya está instalado": "VNC YA INSTALADO",
    "Iniciar VNC": "INICIAR VNC",
    "Detener VNC": "DETENER VNC",
    "Cambiar contraseña": "CAMBIAR CONTRASEÑA",
    "FUERZA BRUTA - HIDRA": "FUERZA BRUTA - HIDRA",
    "Servicio a atacar": "SERVICIO A ATACAR",
    "Target (IP/Dominio)": "TARGET (IP/DOMINIO)",
    "Wordlist (ruta)": "WORDLIST (RUTA)",
    "Iniciando ataque...": "INICIANDO ATAQUE...",
    "BLOQUEAR TORRENT": "BLOQUEAR TORRENT",
    "Torrent bloqueado correctamente": "TORRENT BLOQUEADO",
    "DESBLOQUEAR VULTR": "DESBLOQUEAR VULTR",
    "Eliminando restricciones de VULTR...": "ELIMINANDO RESTRICCIONES DE VULTR...",
    "VULTR desbloqueado. Reinicie el sistema si es necesario": "VULTR DESBLOQUEADO. REINICIA SI ES NECESARIO",
}

# ==============================================
# FUNCIÓN DE TRADUCCIÓN
# ==============================================
def fun_trans(texto):
    idioma_file = ".idioma"
    texto_file = ".texto"
    
    # Leer idioma guardado
    linguage = "es"
    if os.path.exists(idioma_file):
        with open(idioma_file, "r") as f:
            linguage = f.read().strip()
            if not linguage:
                linguage = "es"
    
    # Si es español de barrio (es-mx), usar el diccionario
    if linguage == "es-mx":
        texto_upper = texto.upper()
        if texto_upper in DICCIONARIO_ES:
            return DICCIONARIO_ES[texto_upper]
        return texto
    
    # Si es español normal, devolver el texto original
    if linguage == "es":
        return texto
    
    # Para otros idiomas, usar translate-shell
    if os.system("which trans > /dev/null 2>&1") != 0:
        return texto
    
    # Buscar en caché
    if os.path.exists(texto_file):
        with open(texto_file, "r") as f:
            for line in f:
                match = re.match(r"texto\['(.*?)'\]='(.*)'", line.strip())
                if match and match.group(1) == texto:
                    return match.group(2)
    
    # Traducir
    try:
        result = subprocess.run(
            ["trans", "-e", "bing", "-b", f"es:{linguage}", texto],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            traduccion = result.stdout.strip()
            with open(texto_file, "a") as f:
                escaped = traduccion.replace("'", "\\'")
                f.write(f"texto['{texto}']='{escaped}'\n")
            return traduccion
        else:
            return texto
    except Exception:
        return texto

def funcao_idioma():
    # Array de idiomas (33 idiomas)
    idioma = {
        1: "ar Arabic",
        2: "zh Chinese",
        3: "en English",
        4: "fr French",
        5: "de German",
        6: "it Italian",
        7: "ja Japanese",
        8: "hi Hindi",
        9: "pt Portuguese",
        10: "ru Russian",
        11: "es Español",
        12: "es-mx Barrio V.",
        13: "tr Turkish",
        14: "sv Swedish",
        15: "da Danish",
        16: "no Norwegian",
        17: "fi Finnish",
        18: "nl Dutch",
        19: "el Greek",
        20: "he Hebrew",
        21: "ko Korean",
        22: "th Thai",
        23: "vi Vietnamese",
        24: "pl Polish",
        25: "uk Ukrainian",
        26: "cs Czech",
        27: "hu Hungarian",
        28: "ro Romanian",
        29: "ms Malay",
        30: "id Indonesian",
        31: "fa Persian",
        32: "bn Bengali",
        33: "sw Swahili",
    }

    total = 33
    columnas = 3
    filas = total // columnas

    # Calcular ancho máximo
    max_len = 0
    for i in range(1, total + 1):
        nombre = idioma[i].split(" ", 1)[1]
        largo = 6 + len(nombre)
        if largo > max_len:
            max_len = largo
    ancho_celda = max_len + 3

    os.system("clear")
    print(f"{RED}[{GREEN}~{RED}]{GREEN} \033[3m{fun_trans('Traductor')} {YELLOW}VPS-BARBA{RESET}")
    print(BARRA)

    for l in range(filas):
        linea = ""
        for c in range(columnas):
            idx = l + c * filas + 1
            if idx <= total:
                nombre = idioma[idx].split(" ", 1)[1]
                opcion_num = f"{RED}[{GREEN}{idx:02d}{RED}]\033[93m⇨\033[96m{nombre}{RESET}"
                largo_actual = 6 + len(nombre)
                padding = ancho_celda - largo_actual
                if padding < 0:
                    padding = 0
                espacios = " " * padding
                linea += opcion_num + espacios
            else:
                espacios = " " * ancho_celda
                linea += espacios
        print(linea)

    print(BARRA)
    opcion = input(f"{GREEN}{fun_trans('Seleccione una opción')}: {RESET}")
    sys.stdout.write("\033[1A\033[K")
    sys.stdout.flush()

    if opcion.isdigit():
        idx_op = int(opcion)
        if 1 <= idx_op <= total:
            codigo_seleccionado = idioma[idx_op].split(" ")[0]
            with open(".idioma", "w") as f:
                f.write(codigo_seleccionado)
            if os.path.exists(".texto"):
                os.remove(".texto")
            print(f"{GREEN}{fun_trans('Idioma cambiado correctamente')}{RESET}")
        else:
            print(f"{RED}{fun_trans('Opción inválida')}{RESET}")
            input(f"{PURPLE}{fun_trans('Enter para Continuar')}{RESET}")
            sys.stdout.write("\033[1A\033[K")
            sys.stdout.flush()
    else:
        print(f"{RED}{fun_trans('Opción inválida')}{RESET}")
        input(f"{PURPLE}{fun_trans('Enter para Continuar')}{RESET}")
        sys.stdout.write("\033[1A\033[K")
        sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        if comando == "traducir" and len(sys.argv) > 2:
            texto = " ".join(sys.argv[2:])
            print(fun_trans(texto))
        elif comando == "idioma":
            funcao_idioma()
        else:
            print("Uso: python3 translator.py traducir \"texto\"")
            print("     python3 translator.py idioma")
