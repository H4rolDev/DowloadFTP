from ftplib import FTP_TLS
import os

# Datos de conexión
ftp_host = "ftp-harol.alwaysdata.net" 
ftp_user = "harol"         
ftp_pass = "12345!Harol"   

archivo_remoto = "prueba.xlsx"  
archivo_local = "pruebaDescarga.xlsx" 

def descargar_archivo_ftp(ftp_host, ftp_user, ftp_pass, archivo_remoto, archivo_local):
    try:
        ftp = FTP_TLS(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_pass)
        ftp.prot_p()
        ftp.set_pasv(True)

        with open(archivo_local, 'wb') as archivo:
            ftp.retrbinary(f'RETR {archivo_remoto}', archivo.write)

        print(f"Archivo {archivo_remoto} descargado correctamente como {archivo_local}")

    except Exception as e:
        print(f"Error al descargar el archivo: {e}")

    finally:
        ftp.quit()

descargar_archivo_ftp(ftp_host, ftp_user, ftp_pass, archivo_remoto, archivo_local)