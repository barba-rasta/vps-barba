#!/bin/bash
Redhat=$(echo -e '\e[38;5;196m'
cat << 'EOF'
                          _____
                   _.+sd$$$$$$$$$bs+._
               .+d$$$$$$$$$$$$$$$$$$$$$b+.
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$;
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$;
  $$$b       `T$b+                        :$$$$$$$BUG$$
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;
   \                            `*TP*     d$$P*******$
    \                                    :$$P'      /
     \                                  :dP'       /
      `.                               d$P       .'
        `.                             `'      .'
          `-.                               .-'
             `-.                         .-'
                `*+-._             _.-+*'
                      `"*-------*"'
EOF
echo -e '\e[0m'
)
declare -A cor=( [0]="\033[1;37m" [1]="\033[1;34m" [2]="\033[1;33m" [3]="\033[1;36m" [4]="\033[1;31m" )
barra="\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
barra="\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
spin () {
local pid=$!
local delay=0.25
local spinner=( '█■■■■' '■█■■■' '■■█■■' '■■■█■' '■■■■█' )

while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do

for i in "${spinner[@]}"
do
	tput civis
	echo -ne "\033[31m\r[\e[0;50;32m~\033[31m] \e[0;50;37m DESCARGANDO .....\e[33m\033[31m[\033[33m$i\033[31m]\033[0m   ";
	sleep $delay
	printf "\b\b\b\b\b\b\b\b";
done
done
printf "   \b\b\b\b\b"
tput cnorm
printf "\e[0;50;91m [\e[0;50;32mInstalado\e[0;50;91m]${FORT}";
echo "";

}
i="[Instalado]"
fun_bar () {
comando[0]="$1"
comando[1]="$2"
 (
[[ -e $HOME/fim ]] && rm $HOME/fim
${comando[0]} -y > /dev/null 2>&1
${comando[1]} -y > /dev/null 2>&1
touch $HOME/fim
 ) > /dev/null 2>&1 &
echo -ne "\033[1;33m ["
while true; do
   for((i=0; i<18; i++)); do
   echo -ne "\033[1;31m##"
   sleep 0.1s
   done
   [[ -e $HOME/fim ]] && rm $HOME/fim && break
   echo -e "\033[1;33m]"
   sleep 1s
   tput cuu1
   tput dl1
   echo -ne "\033[1;33m ["
done
echo -e "\033[1;33m]\033[1;31m -\033[1;32m 100%\033[1;37m"
}
clear
echo -e "$barra"
text="Instalando"
echo -e "${cor[2]} Update"
apt-get install -y screen &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y python &> /dev/null & spin
echo -e "${cor[2]} Upgrade" 
apt-get install -y lsof &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y python3-pip &> /dev/null & spin
echo -e "${cor[2]} $text Lsof"
apt-get install -y  python &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y unzip &> /dev/null & spin
echo -e "${cor[2]} $text Python3" 
apt-get install -y zip &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y apache2 &> /dev/null & spin
echo -e "${cor[2]} $text Unzip"
apt-get install -y ufw &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y nmap  &> /dev/null & spin
echo -e "${cor[2]} $text Screen" 
apt-get install -y figlet &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y  bc &> /dev/null & spin
echo -e "${cor[2]} $text Figlet" 
apt-get install -y  lynx &> /dev/null & spin
tput cuu1 && tput dl1
apt-get install -y  curl &> /dev/null & spin 
echo -e "${cor[2]} $text &> Complementos" 
apt-get install -y  ruby &> /dev/null & spin
echo -e "${cor[2]} $text &> Traductor"
apt-get install -y  translate-shell &> /dev/null & spin 
tput cuu1 && tput dl1
apt install -y cowsay &> /dev/null & spin
tput cuu1 && tput dl1
gem install lolcat  &> /dev/null & spin
apt install -y netstat &> /dev/null & spin
sed -i "s;Listen 80;Listen 81;g" /etc/apache2/ports.conf
service apache2 restart > /dev/null 2>&1
echo -e "$barra"
echo "VPS-BARBA"  |lolcat
echo -e "$Redhat" 
echo -e "$barra"

tput setaf 1 ; tput bold ; echo -e "\t INSTALANDO MENU"; tput sgr0
wget https://raw.githubusercontent.com/barba-rasta/vps-barba/refs/heads/main/menu -O /bin/menu 1> /dev/null 2> /dev/stdout
chmod +777  /bin/menu
sleep 2
tput setaf 2 ; tput bold ; echo -e "\t INSTALANDO HERRAMIENTAS"; tput sgr0
wget https://raw.githubusercontent.com/barba-rasta/vps-barba/refs/heads/main/herramientas -O /bin/herramientas 1> /dev/null 2> /dev/stdout
chmod +777  /bin/herramientas
sleep 2
tput setaf 3 ; tput bold ; echo -e "\t INSTALANDO USER-CODES"; tput sgr0
wget https://raw.githubusercontent.com/barba-rasta/vps-barba/refs/heads/main/user  -O /bin/user 1> /dev/null 2> /dev/stdout
chmod +777  /bin/user
sleep 2
tput setaf 4 ; tput bold ; echo -e "\t INSTALANDO SERVICIOS"; tput sgr0
wget https://raw.githubusercontent.com/barba-rasta/vps-barba/refs/heads/main/servicios -O /bin/servicios 1> /dev/null 2> /dev/stdout
chmod +777  /bin/servicios
tput setaf 1 ; tput bold ; echo -e "\t INSTALANDO TRADUCTOR"; tput sgr0
wget https://raw.githubusercontent.com/barba-rasta/vps-barba/refs/heads/main/translator.py  -O /bin/translator.py 1> /dev/null 2> /dev/stdout
chmod +777  /bin/translator.py
sleep 2
rm -irf vps-barba
echo -e "$barra"
cowthink -f tux para entrar escriba menu mas enter |lolcat
