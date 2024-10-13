#!/usr/bin/env python3

# sudo mv /home/guille/Escritorio/flojo/flojo.py /usr/local/bin/flojo
import argparse
import sys
import pyperclip


def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Enrolamiento de personal OK")
    print("2. Enrolamiento de Empresa OK")
    print("3. Enrolamiento de Personal y Empresa OK")
    print("4. Reporte Enviado")
    print("5. Error en Rut de Personal")
    print("6. Error en Rut de Empresa")
    print("7. Salir")


def main():
    parser = argparse.ArgumentParser(
        description="Programa de consola con flags")
    parser.add_argument('-f', '--female', action='store_true',
                        help='Indica si es femenino')
    parser.add_argument('-n', '--nombre', type=str,
                        help='Nombre de la persona')

    args = parser.parse_args()

    estimado = "Estimada" if args.female else "Estimado"
    nombre = args.nombre if args.nombre else "Usuario"

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                mensaje = f"{estimado} {
                    nombre}, Junto con saludarle, y desearle una excelente jornada le informo que el Enrolamiento de personal ha sido exitoso.\nSaludos.\nGuillermo Torres Renner"
                pyperclip.copy(mensaje)
                print(mensaje)
            case '2':
                mensaje = f"{estimado} {
                    nombre}, Junto con saludarle, y desearle una excelente jornada, le comento que la empresa XXXXXXX ha sido creada y los servicios asignados correctamente.\nSaludos.\nGuillermo Torres Renner"
                pyperclip.copy(mensaje)
                print(mensaje)
            case '3':
                mensaje = f"{estimado} {
                    nombre}, Junto con saludarle, y desearle una excelente jornada, le comento que la empresa XXXXXXX ha sido creada, los servicios asignados y el personal enrolado correctamente.\nSaludos.\nGuillermo Torres Renner"
                pyperclip.copy(mensaje)
                print(mensaje)
            case '4':
                mensaje = f"{estimado} {
                    nombre}, Adjunto reporte solicitado.\nSaludos.\nGuillermo Torres Renner"
                pyperclip.copy(mensaje)
                print(mensaje)
            case '5':
                mensaje = f"{estimado} {nombre}, Juntamente con saludarle, le informo que los siguientes trabajadores no pudieron ser enrolados por tener error en su RUT.\nFavor de revisar, corregir y reenviar los datos correspondientes para poder finalizar el enrolamiento.\nSaludos.\nGuillermo Torres Renner"
                pyperclip.copy(mensaje)
                print(mensaje)
            case '6':
                mensaje = f"{estimado} {nombre}, Juntamente con saludarle, le informo que los siguientes trabajadores no pudieron ser enrolados por tener error en su RUT.\nFavor de revisar, corregir y reenviar los datos correspondientes para poder finalizar el enrolamiento.\nSaludos.\nGuillermo Torres Renner"
                pyperclip.copy(mensaje)
                print(mensaje)
            case '7':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
