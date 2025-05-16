
import rsa


def generar_llaves_rsa():
    # Generar par de llaves RSA (2048 bits)
    print("Generando par de llaves RSA de 2048 bits...")
    (public_key, private_key) = rsa.newkeys(2048)

    # Guardar llave privada
    with open("private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1())

    # Guardar llave pública en el formato adecuado para la página web
    with open("files/public_key.txt", "wb") as f:
        f.write(public_key.save_pkcs1())

    print("Llaves generadas con éxito:")
    print(f"- Llave privada guardada en: private_key.pem")
    print(f"- Llave pública guardada en: files/public_key.txt")
    print("\nIMPORTANTE: Guarda tu llave privada en un lugar seguro.")
    print("La llave pública ya está disponible para su descarga desde tu página web.")

    # Mostrar la llave pública en formato legible
    print("\nContenido de la llave pública:")
    print(public_key.save_pkcs1().decode('utf-8'))


if __name__ == "__main__":
    # Verificar que exista la carpeta files
    import os

    if not os.path.exists("files"):
        os.makedirs("files")
        print("Carpeta 'files' creada exitosamente.")

    generar_llaves_rsa()

