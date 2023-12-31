from os import system
import os
import hashlib
import subprocess

print("Comenzando Instalacion De Guacamole")
system("sleep 3s")
system("sudo apt install libavcodec-dev libavformat-dev libavutil-dev libswscale-dev freerdp2-dev libpango1.0-dev libssh2-1-dev libtelnet-dev libvncserver-dev libwebsockets-dev libpulse-dev libssl-dev libvorbis-dev libwebp-dev")
system("sudo apt install libcairo2-dev libjpeg-turbo8-dev libjpeg62-dev libpng12-dev libtool-bin libossp-uuid-dev")
system("apt install libavcodec-dev libavformat-dev libavutil-dev libswscale-dev freerdp2-dev libssh2-1-dev libtelnet-dev libvncserver-dev libpulse-dev libssl-dev libvorbis-dev libwebp-dev")
system("sudo apt install systemctl -y")
system("wget https://downloads.apache.org/guacamole/1.5.3/source/guacamole-server-1.5.3.tar.gz")
system("tar -xvf guacamole-server-1.5.3.tar.gz")
nuevo_directorio = "guacamole-server-1.5.3"
os.chdir(nuevo_directorio)
system("./configure --with-init-dir=/etc/init.d")
system("make")
system("make install")
system("ldconfig")
system("cls")
print("Ya Casi Terminamos De Instalar Apache Guacamole")
system("sleep 3s")
system("systemctl daemon-reload")
system("systemctl start guacd && systemctl enable guacd")
system("systemctl status guacd")
system("ss -lnpt | grep guacd")
system("sudo apt install tomcat9 tomcat9-admin tomcat9-common tomcat9-user")
javains = input("TIENES JAVA INSTALADO ? (y/n)")
if (javains == "y"):
    print("siguiendo con la instalacion")
else:
    system("sudo apt install openjdk-17-jdk")
    system("export JAVA_HOME=/usr/lib/jvm/temurin-17-jdk-amd64")
    system("Siguiendo Con la instalacion")
    system("sleep 3s")
system("ss -lnpt | grep java")
system("wget https://downloads.apache.org/guacamole/1.5.3/binary/guacamole-1.5.3.war")
system("mv guacamole-1.5.3.war /var/lib/tomcat9/webapps/guacamole.war")
system("systemctl restart tomcat9 guacd")
system("mkdir /etc/guacamole/")
system("wget -P /etc/guacamole/ https://github.com/ivangabriel21/DependeciaDX/raw/main/guacamole.properties")
system("cls")
contra = input("¿Qué contraseña deseas usar para el Apache Guacamole? ")

# Calcular el hash MD5 de la contraseña
hashed_password = hashlib.md5(contra.encode()).hexdigest()

# Imprimir el hash MD5
print("Hash MD5 de la contraseña:", hashed_password)
print("Copia la contraseña se utilizara mas Adelante en La Configuracion")
system("wget -P /etc/guacamole/ https://github.com/ivangabriel21/DependeciaDX/raw/main/user-mapping.xml")
input(f"Ahora configuras el usuario cambia admin por el usuario que quieras, y En Contraseña MD5 Pon esto: {hashed_password}")
print("sleep 2s")
system("chmod 600 /etc/guacamole/user-mapping.xml")
system("chown tomcat:tomcat /etc/guacamole/user-mapping.xml")
system("systemctl restart tomcat9 guacd")
ip = subprocess.check_call(['curl', 'ifconfig.me'])
print(f"Puedes Entrar a La Web con El puerto 8080: http://{ip}:8080 si es con TLS es https://{ip}:8080")
