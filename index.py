from ftplib import FTP_TLS, error_perm, error_temp

ftp_host = 'ftp-harol.alwaysdata.net'  
ftp_user = 'harol'   
ftp_pass = '12345!Harol'  

archivo_local = './prueba.xlsx' 
archivo_remoto = 'FTP/guardadoPrueba.xlsx'  

ftp = FTP_TLS(ftp_host)

try:
    ftp.connect(ftp_host, 21)
    ftp.login(ftp_user, ftp_pass)

    try:
        ftp.set_pasv(True)
        print("Modo pasivo activado.")
    except Exception as e:
        print("Error al activar modo pasivo, cambiando a modo activo:", e)
        ftp.set_pasv(False)

    ftp.prot_p()

    with open(archivo_local, 'rb') as file:
        ftp.storbinary(f'STOR {archivo_remoto}', file)

    print(f'Archivo {archivo_local} subido correctamente a {ftp_host}')

except error_perm as e:
    print(f"Error de permiso: {e}")
except error_temp as e:
    print(f"Error temporal: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    ftp.quit()
