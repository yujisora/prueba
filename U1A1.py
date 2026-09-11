# Crea un programa en Python que incluya los siguientes elementos:
# Declaración de variables: define y utiliza variables dentro del programa.
# Conversión de tipos de datos: convierte datos de un tipo a otro cuando sea necesario.
# Lista de elementos: crea y utiliza una lista para guardar varios elementos.
# Diccionario: crea un diccionario con la información de un dispositivo.
# Estructura condicional: utiliza una condición para que el programa tome una decisión.
# Manejo de archivos: guarda un reporte generado por el programa en un archivo.

device_name = input("Insert device name: ")
device_ip = input("Insert IP address: ")

open_ports = []
open_ports_input = input("Insert active ports (comma-separated): ")
for ports in open_ports_input.split(","):
    open_ports.append(int(ports.strip()))

active_input = input("Is the device active? (Y/N): ").strip().lower()
if active_input in ("y", "yes", "1"):
    is_active = True
    uptime_hours = float(input("Insert device uptime (in hours): "))
elif active_input in ("n", "no", "0"):
    is_active = False
    uptime_hours = 0

uptime_days = round(uptime_hours / 24, 2)

device_info = {
    "name": device_name,
    "ip": device_ip,
    "active": is_active,
    "uptime_hours": uptime_hours,
}

device_info["uptime_days"] = uptime_days
device_info["ports"] = open_ports

if device_info["active"] is True:
    status_msg = "ACTIVE"
elif device_info["active"] is False:
    status_msg = "DISCONNECTED"
else:
    status_msg = "UNKNOWN"

filename = "device_report.txt"
with open(filename, "w") as report:
    report.write(
        "Network Device Report\n"
        f"Name  : {device_info['name']}\n"
        f"IP    : {device_info['ip']}\n"
        f"Ports : {device_info['ports']}\n"
        f"Uptime: {device_info['uptime_hours']} h ({device_info['uptime_days']} days)\n"
        f"Status: {status_msg}"
    )

print("Network Device Report:")
print(f"Name  : {device_info['name']}")
print(f"IP    : {device_info['ip']}")
print(f"Ports : {device_info['ports']}")
print(f"Uptime: {device_info['uptime_hours']} h ({device_info['uptime_days']} days)")
print(f"Status: {status_msg}")
print("A file with the report has also been saved.")