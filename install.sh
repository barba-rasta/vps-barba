#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# VPS-BARBA - Script de Instalación Mejorado
# Autor: Barba-Rasta
# Versión: 2.0
# ═══════════════════════════════════════════════════════════════

set -e
set -o pipefail

# ───────────────────────────────────────────────────────────────
# COLORES Y ESTILOS
# ───────────────────────────────────────────────────────────────
R=$'\e[0m'
BOLD=$'\e[1m'
DIM=$'\e[2m'
ITALIC=$'\e[3m'
UNDERLINE=$'\e[4m'

BLACK=$'\e[30m'
RED=$'\e[38;5;196m'
GREEN=$'\e[38;5;82m'
YELLOW=$'\e[38;5;220m'
BLUE=$'\e[38;5;33m'
MAGENTA=$'\e[38;5;201m'
CYAN=$'\e[38;5;45m'
WHITE=$'\e[38;5;255m'

DARK_RED=$'\e[38;5;88m'
DARK_GREEN=$'\e[38;5;22m'
ORANGE=$'\e[38;5;208m'
PINK=$'\e[38;5;213m'
LIGHT_BLUE=$'\e[38;5;81m'

# ───────────────────────────────────────────────────────────────
# CONFIGURACIÓN
# ───────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="/tmp/vps-barba-install.log"
REPO_URL="https://raw.githubusercontent.com/barba-rasta/vps-barba/refs/heads/main"
TELEGRAM_BOT_TOKEN=""
TELEGRAM_CHAT_ID=""
LANG_DEFAULT="es"

# ───────────────────────────────────────────────────────────────
# FUNCIÓN DE TRADUCCIÓN (fun_trans)
# ───────────────────────────────────────────────────────────────
declare -A TRANSLATIONS=(
    ["es_update"]="Actualizando sistema"
    ["en_update"]="Updating system"
    ["pt_update"]="Atualizando sistema"

    ["es_upgrade"]="Actualizando paquetes"
    ["en_upgrade"]="Upgrading packages"
    ["pt_upgrade"]="Atualizando pacotes"

    ["es_installing"]="Instalando"
    ["en_installing"]="Installing"
    ["pt_installing"]="Instalando"

    ["es_installed"]="Instalado"
    ["en_installed"]="Installed"
    ["pt_installed"]="Instalado"

    ["es_downloading"]="Descargando"
    ["en_downloading"]="Downloading"
    ["pt_downloading"]="Baixando"

    ["es_done"]="Completado"
    ["en_done"]="Done"
    ["pt_done"]="Concluído"

    ["es_error"]="Error"
    ["en_error"]="Error"
    ["pt_error"]="Erro"

    ["es_menu"]="Instalando Menú"
    ["en_menu"]="Installing Menu"
    ["pt_menu"]="Instalando Menu"

    ["es_tools"]="Instalando Herramientas"
    ["en_tools"]="Installing Tools"
    ["pt_tools"]="Instalando Ferramentas"

    ["es_user"]="Instalando Gestor de Usuarios"
    ["en_user"]="Installing User Manager"
    ["pt_user"]="Instalando Gerenciador de Usuários"

    ["es_services"]="Instalando Servicios"
    ["en_services"]="Installing Services"
    ["pt_services"]="Instalando Serviços"

    ["es_translator"]="Instalando Traductor"
    ["en_translator"]="Installing Translator"
    ["pt_translator"]="Instalando Tradutor"

    ["es_complements"]="Instalando Complementos"
    ["en_complements"]="Installing Complements"
    ["pt_complements"]="Instalando Complementos"

    ["es_banner_title"]="VPS-BARBA"
    ["en_banner_title"]="VPS-BARBA"
    ["pt_banner_title"]="VPS-BARBA"

    ["es_enter_menu"]="Para entrar escriba: menu"
    ["en_enter_menu"]="To enter type: menu"
    ["pt_enter_menu"]="Para entrar digite: menu"

    ["es_welcome"]="Bienvenido a VPS-BARBA"
    ["en_welcome"]="Welcome to VPS-BARBA"
    ["pt_welcome"]="Bem-vindo ao VPS-BARBA"

    ["es_install_complete"]="Instalación Completada"
    ["en_install_complete"]="Installation Complete"
    ["pt_install_complete"]="Instalação Concluída"

    ["es_check_root"]="Este script debe ejecutarse como root"
    ["en_check_root"]="This script must be run as root"
    ["pt_check_root"]="Este script deve ser executado como root"

    ["es_check_debian"]="Este script solo funciona en Debian/Ubuntu"
    ["en_check_debian"]="This script only works on Debian/Ubuntu"
    ["pt_check_debian"]="Este script funciona apenas em Debian/Ubuntu"

    ["es_cleaning"]="Limpiando archivos temporales"
    ["en_cleaning"]="Cleaning temporary files"
    ["pt_cleaning"]="Limpando arquivos temporários"

    ["es_apache_port"]="Configurando Apache en puerto 81"
    ["en_apache_port"]="Configuring Apache on port 81"
    ["pt_apache_port"]="Configurando Apache na porta 81"

    ["es_progress"]="Progreso"
    ["en_progress"]="Progress"
    ["pt_progress"]="Progresso"
)

fun_trans() {
    local key="${LANG_DEFAULT}_${1}"
    local text="${TRANSLATIONS[$key]}"
    if [[ -z "$text" ]]; then
        text="${TRANSLATIONS["es_${1}"]}"
    fi
    echo "${text:-$1}"
}

# ───────────────────────────────────────────────────────────────
# BANNER ART
# ───────────────────────────────────────────────────────────────
banner_art() {
    echo -e "${CYAN}.     .       .  .   . .   .  . .    ${RED}+  .${R}"
    echo -e "${CYAN}  .     .  :     .    .. :. .___-----${RED}----___.${R}"
    echo -e "${CYAN}   .   .  .   .    .  :.:. _\".^ .^ ^${RED}.   .. :\"-_. .${R}"
    echo -e "${CYAN}    .  :       .  .  .:../:          ${RED}  . .^  :.:\\${R}"
    echo -e "${CYAN}        .   . :: +. :.:/: .   .    . ${RED}       . . .:\\${R}"
    echo -e "${CYAN} .  :    .     . _ :::/:             ${RED}  .  ^ .  . .:\\${R}"
    echo -e "${CYAN}  .. . .   . - : :.:./.               ${RED}         .  .:\\${R}"
    echo -e "${CYAN}  .      .     . :..|:               ${RED}     .  .  ^. .:|${R}"
    echo -e "${CYAN}    .       . : : ..||        .      ${RED}          . . !:|${R}"
    echo -e "${CYAN}  .     . . . ::. ::\\(               ${RED}            . :)/${R}"
    echo -e "${CYAN}  :.. .  :-  : .:  ::|.${GREEN}#######${CYAN}           ${RED}..${GREEN}########${RED}:|${R}"
    echo -e "${CYAN} .  .  .  ..  .  .. :\\ ${GREEN}########${CYAN}          ${RED}:${GREEN}########${RED} :/${R}"
    echo -e "${CYAN}  .        .+ :: : -.:\\ ${GREEN}########${CYAN}       ${RED}. ${GREEN}########${RED}.:/${R}"
    echo -e "${CYAN}    .  .+   . . . . :.:\\. ${GREEN}#######${CYAN}       ${GREEN}#######${RED}..:/${R}"
    echo -e "${CYAN}      :: . . . . ::.:..:.\\           ${RED}.   .   ..:/${R}"
    echo -e "${CYAN}   .   .   .  .. :  -::::.\\.       | ${RED}|     . .:/${R}"
    echo -e "${CYAN}     .  :  .  .  .-:.\\\".:.::.\\        ${RED}     ..:/${R}"
    echo -e "${CYAN} .      -.   . . . .: .:::.:.\\.      ${RED}     .:/${R}"
    echo -e "${CYAN}.   .   .  :      : ....::_:..:\\   __${RED}_.  :/${R}"
    echo -e "${CYAN}   .   .  .   .:. .. .  .: :.:.:\\    ${RED}   :/${R}"
    echo -e "${CYAN}     +   .   .   : . ::. :.:. .:.|\\  ${RED}.:/|${R}"
    echo -e "${CYAN}     .         +   .  .  ...:: ..|  -${RED}--.:|${R}"
    echo -e "${CYAN}.      . . .   .  .  . ... :..:..\"(  ${RED}..)\"${R}"
    echo -e "${R}"
}

# ───────────────────────────────────────────────────────────────
# BARRA DE SEPARACIÓN
# ───────────────────────────────────────────────────────────────
barra() {
    echo -e "${BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬${R}"
}

# ───────────────────────────────────────────────────────────────
# MOSTRAR BANNER COMPLETO (se mantiene visible durante toda la instalación)
# ───────────────────────────────────────────────────────────────
show_full_banner() {
    clear
    barra
    banner_art
    echo -e "${BOLD}${YELLOW}$(fun_trans banner_title)${R}" | lolcat 2>/dev/null || echo -e "${BOLD}${YELLOW}$(fun_trans banner_title)${R}"
    barra
    echo ""
}

# ───────────────────────────────────────────────────────────────
# SPINNER ANIMADO
# ───────────────────────────────────────────────────────────────
spin() {
    local pid=$1
    local msg="$2"
    local delay=0.15
    local spinner=('⠋' '⠙' '⠹' '⠸' '⠼' '⠴' '⠦' '⠧' '⠇' '⠏')

    tput civis 2>/dev/null || true
    while kill -0 "$pid" 2>/dev/null; do
        for i in "${spinner[@]}"; do
            printf "\r${CYAN}[${GREEN}%s${CYAN}] ${WHITE}%s...${R}   " "$i" "$msg"
            sleep $delay
        done
    done
    printf "\r${GREEN}[✓]${R} ${WHITE}%s${GREEN} %s${R}%-20s\n" "$msg" "$(fun_trans installed)" ""
    tput cnorm 2>/dev/null || true
}

# ───────────────────────────────────────────────────────────────
# BARRA DE PROGRESO
# ───────────────────────────────────────────────────────────────
fun_bar() {
    local comando="$1"
    local msg="$2"
    local total=40

    eval "$comando" > /dev/null 2>&1 &
    local pid=$!

    tput civis 2>/dev/null || true
    echo -ne "${CYAN}[${R}"

    local progress=0
    while kill -0 "$pid" 2>/dev/null; do
        if [[ $progress -lt $total ]]; then
            progress=$((progress + 1))
        fi
        local filled=$progress
        local empty=$((total - filled))
        local bar=""
        for ((i=0; i<filled; i++)); do bar+="${GREEN}█${R}"; done
        for ((i=0; i<empty; i++)); do bar+="${DIM}░${R}"; done
        local percent=$((progress * 100 / total))
        printf "\r${CYAN}[${R}%s${CYAN}]${R} ${WHITE}%s ${CYAN}%3d%%${R}" "$bar" "$msg" "$percent"
        sleep 0.1
    done

    # Completar barra
    local bar=""
    for ((i=0; i<total; i++)); do bar+="${GREEN}█${R}"; done
    printf "\r${CYAN}[${R}%s${CYAN}]${R} ${WHITE}%s ${GREEN}%3d%%${R} ${GREEN}✓${R}\n" "$bar" "$msg" "100"
    tput cnorm 2>/dev/null || true

    wait $pid
    return $?
}

# ───────────────────────────────────────────────────────────────
# INSTALAR PAQUETE CON SPINNER
# ───────────────────────────────────────────────────────────────
install_pkg() {
    local pkg="$1"
    local msg="$2"

    if dpkg -l | grep -q "^ii  $pkg " 2>/dev/null; then
        printf "${GREEN}[✓]${R} ${WHITE}%s${R} ${DIM}(ya instalado)${R}\n" "$msg"
        return 0
    fi

    apt-get install -y "$pkg" > /dev/null 2>&1 &
    spin $! "$msg"
    return $?
}

# ───────────────────────────────────────────────────────────────
# DESCARGAR ARCHIVO CON PROGRESO
# ───────────────────────────────────────────────────────────────
download_file() {
    local url="$1"
    local dest="$2"
    local msg="$3"

    wget -q "$url" -O "$dest" &
    local pid=$!
    spin $pid "$msg"

    if [[ -f "$dest" ]]; then
        chmod +x "$dest" 2>/dev/null || chmod 777 "$dest" 2>/dev/null || true
        return 0
    else
        printf "${RED}[✗]${R} ${WHITE}%s${R} ${RED}%s${R}\n" "$msg" "$(fun_trans error)"
        return 1
    fi
}

# ───────────────────────────────────────────────────────────────
# NOTIFICACIÓN TELEGRAM
# ───────────────────────────────────────────────────────────────
telegram_notify() {
    local message="$1"
    if [[ -n "$TELEGRAM_BOT_TOKEN" && -n "$TELEGRAM_CHAT_ID" ]]; then
        curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
            -d "chat_id=${TELEGRAM_CHAT_ID}" \
            -d "text=${message}" \
            -d "parse_mode=HTML" > /dev/null 2>&1 || true
    fi
}

# ───────────────────────────────────────────────────────────────
# VERIFICACIONES INICIALES
# ───────────────────────────────────────────────────────────────
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${RED}[✗] $(fun_trans check_root)${R}"
        exit 1
    fi
}

check_os() {
    if [[ ! -f /etc/debian_version ]]; then
        echo -e "${RED}[✗] $(fun_trans check_debian)${R}"
        exit 1
    fi
}

# ───────────────────────────────────────────────────────────────
# ACTUALIZAR SISTEMA
# ───────────────────────────────────────────────────────────────
update_system() {
    show_full_banner
    echo -e "${YELLOW}${BOLD}▶ $(fun_trans update)${R}\n"

    apt-get update -y > /dev/null 2>&1 &
    spin $! "$(fun_trans update)"

    echo ""
    echo -e "${YELLOW}${BOLD}▶ $(fun_trans upgrade)${R}\n"

    apt-get upgrade -y > /dev/null 2>&1 &
    spin $! "$(fun_trans upgrade)"

    echo ""
}

# ───────────────────────────────────────────────────────────────
# INSTALAR DEPENDENCIAS
# ───────────────────────────────────────────────────────────────
install_dependencies() {
    show_full_banner
    echo -e "${YELLOW}${BOLD}▶ $(fun_trans installing) $(fun_trans complements)${R}\n"

    local deps=(
        "screen:Screen"
        "python3:Python3"
        "python3-pip:Python3 PIP"
        "lsof:Lsof"
        "unzip:Unzip"
        "zip:Zip"
        "apache2:Apache2"
        "ufw:UFW Firewall"
        "nmap:Nmap"
        "figlet:Figlet"
        "bc:BC Calculator"
        "lynx:Lynx"
        "curl:Curl"
        "ruby:Ruby"
        "translate-shell:Translate Shell"
        "cowsay:Cowsay"
        "net-tools:Netstat"
        "git:Git"
        "jq:JQ"
        "nano:Nano"
        "htop:Htop"
    )

    for dep in "${deps[@]}"; do
        IFS=':' read -r pkg msg <<< "$dep"
        install_pkg "$pkg" "$(fun_trans installing) $msg"
    done

    # Instalar lolcat
    if ! command -v lolcat &> /dev/null; then
        gem install lolcat > /dev/null 2>&1 &
        spin $! "$(fun_trans installing) Lolcat"
    fi

    echo ""
}

# ───────────────────────────────────────────────────────────────
# CONFIGURAR SERVICIOS
# ───────────────────────────────────────────────────────────────
configure_services() {
    show_full_banner
    echo -e "${YELLOW}${BOLD}▶ $(fun_trans apache_port)${R}\n"

    if [[ -f /etc/apache2/ports.conf ]]; then
        sed -i "s/Listen 80/Listen 81/g" /etc/apache2/ports.conf
        sed -i "s/:80/:81/g" /etc/apache2/sites-available/000-default.conf 2>/dev/null || true
        systemctl restart apache2 > /dev/null 2>&1 || service apache2 restart > /dev/null 2>&1 || true
        echo -e "${GREEN}[✓]${R} ${WHITE}$(fun_trans apache_port)${R}"
    fi

    echo ""
}

# ───────────────────────────────────────────────────────────────
# DESCARGAR SCRIPTS DEL SISTEMA
# ───────────────────────────────────────────────────────────────
download_scripts() {
    show_full_banner
    echo -e "${YELLOW}${BOLD}▶ $(fun_trans downloading) Scripts${R}\n"

    local scripts=(
        "menu:menu:$(fun_trans menu)"
        "herramientas:herramientas:$(fun_trans tools)"
        "user:user:$(fun_trans user)"
        "servicios:servicios:$(fun_trans services)"
        "translator.py:translator.py:$(fun_trans translator)"
    )

    for script in "${scripts[@]}"; do
        IFS=':' read -r file dest msg <<< "$script"
        download_file "${REPO_URL}/${file}" "/bin/${dest}" "$msg"
        sleep 0.5
    done

    # Crear symlink para menu si no existe
    if [[ ! -f /usr/local/bin/menu ]]; then
        ln -sf /bin/menu /usr/local/bin/menu 2>/dev/null || true
    fi

    echo ""
}

# ───────────────────────────────────────────────────────────────
# LIMPIAR ARCHIVOS TEMPORALES
# ───────────────────────────────────────────────────────────────
cleanup() {
    show_full_banner
    echo -e "${YELLOW}${BOLD}▶ $(fun_trans cleaning)${R}\n"

    rm -rf /tmp/vps-barba* 2>/dev/null || true
    rm -rf ~/vps-barba 2>/dev/null || true
    apt-get autoremove -y > /dev/null 2>&1 &
    spin $! "$(fun_trans cleaning)"

    echo ""
}

# ───────────────────────────────────────────────────────────────
# ANIMACIÓN FINAL - JORGE BAɓBA
# ───────────────────────────────────────────────────────────────
final_animation() {
    clear
    barra

    local colors=($RED $GREEN $YELLOW $BLUE $MAGENTA $CYAN $ORANGE $PINK)
    local text="JORGE BAɓBA"

    # Animación de entrada
    for ((i=0; i<5; i++)); do
        clear
        barra
        echo ""
        local color=${colors[$((i % ${#colors[@]}))]}
        echo -e "${color}${BOLD}"
        figlet -c -f slant "$text" 2>/dev/null || echo -e "          ${BOLD}$text${R}"
        echo -e "${R}"
        barra
        sleep 0.3
    done

    # Mostrar con lolcat
    clear
    barra
    echo ""
    figlet -c -f slant "$text" 2>/dev/null | lolcat 2>/dev/null || echo -e "${BOLD}${CYAN}          $text${R}"
    echo ""
    barra

    sleep 1
}

# ───────────────────────────────────────────────────────────────
# MENSAJE FINAL
# ───────────────────────────────────────────────────────────────
show_final_message() {
    show_full_banner

    echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════╗${R}"
    echo -e "${GREEN}${BOLD}║                                                              ║${R}"
    echo -e "${GREEN}${BOLD}║     $(fun_trans install_complete) ✓                           ║${R}"
    echo -e "${GREEN}${BOLD}║                                                              ║${R}"
    echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════════╝${R}"
    echo ""

    cowthink -f tux "$(fun_trans enter_menu)" 2>/dev/null | lolcat 2>/dev/null || \
        echo -e "${CYAN}$(fun_trans enter_menu)${R}"

    echo ""
    barra

    # Notificar por Telegram
    telegram_notify "✅ <b>VPS-BARBA</b> instalado correctamente en $(hostname -I | awk '{print $1}')"
}

# ───────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL
# ───────────────────────────────────────────────────────────────
main() {
    # Inicializar log
    exec > >(tee -a "$LOG_FILE") 2>&1

    # Verificaciones
    check_root
    check_os

    # Mostrar banner inicial
    show_full_banner
    echo -e "${CYAN}${BOLD}$(fun_trans welcome)${R}\n"
    sleep 1

    # Ejecutar pasos de instalación
    update_system
    install_dependencies
    configure_services
    download_scripts
    cleanup

    # Animación final
    final_animation

    # Mensaje final
    show_final_message

    # Limpiar log
    rm -f "$LOG_FILE"
}

# ───────────────────────────────────────────────────────────────
# EJECUTAR
# ───────────────────────────────────────────────────────────────
main "$@"
