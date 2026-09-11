import random
from datetime import datetime

numero = random.randint(1000, 9999)
numero_reporte = "R" + str(numero)

fecha_hora = datetime.now()
fecha = fecha_hora.strftime("%Y-%m-%d")
hora = fecha_hora.strftime("%H:%M:%S")

print("=" * 60)
print("   SISTEMA DE DIAGNÓSTICO Y SOPORTE TÉCNICO AVANZADO")
print("=" * 60)
print("Bienvenido al sistema. Por favor, ingresa los datos solicitados.\n")

usuario = input("Ingrese nombre de usuario: ").strip()
nombre = input("Ingrese nombre completo: ").strip()
direccion = input("Ingrese dirección: ").strip()

print("\nSeleccione el tipo de equipo:")
print("1. PC")
print("2. Laptop")
print("3. Servidor")
print("4. Tablet")

opciones_equipo = {"1": "PC", "2": "Laptop", "3": "Servidor", "4": "Tablet"}
opcion = input("Opción (1-4): ").strip()
tipo_equipo = opciones_equipo.get(opcion, "Equipo Desconocido")

print("\n" + "-" * 60)
print(f"INICIO DE DIAGNÓSTICO PARA: {tipo_equipo.upper()}")
print("-" * 60)

diagnostico = ""
detalles_adicionales = []

electricidad_red = input("¿Hay suministro eléctrico general en el inmueble/zona? (s/n): ").strip().lower() == "s"

if not electricidad_red:
    diagnostico = "Corte general de energía eléctrica. Esperar a que se restablezca el servicio en la zona."
else:
    tomacorriente = input("¿El tomacorriente o regulador entrega energía a otros aparatos? (s/n): ").strip().lower() == "s"
    
    if not tomacorriente:
        diagnostico = "Falla en la fuente de alimentación externa (falla en el tomacorriente, regulador o UPS)."
    else:
        if tipo_equipo in ["Laptop", "Tablet"]:
            led_carga = input("¿El LED indicador de carga en el equipo se enciende al conectar el cargador? (s/n): ").strip().lower() == "s"
            if not led_carga:
                detalles_adicionales.append("El equipo no detecta la conexión del cargador o el cargador está defectuoso.")

        enciende = input("¿Enciende el equipo (emite luces, pitidos o sonidos de ventiladores)? (s/n): ").strip().lower() == "s"
        
        if not enciende:
            if tipo_equipo == "PC":
                interruptor_fuente = input("¿El interruptor trasero de la fuente de poder (I/O) está encendido? (s/n): ").strip().lower() == "s"
                if not interruptor_fuente:
                    diagnostico = "La fuente de poder está apagada físicamente desde el switch trasero."
                else:
                    diagnostico = "Falla total de encendido. Posible daño en fuente de poder, botón de encendido o tarjeta madre."
            else:
                diagnostico = "Falla total de encendido. Posible daño en la placa base o batería completamente agotada/dañada."
        else:
            imagen = input("¿Muestra alguna imagen o texto en la pantalla al encender? (s/n): ").strip().lower() == "s"
            
            if not imagen:
                brillo = input("¿Se ve la pantalla muy al fondo con una linterna o tiene el brillo al mínimo? (s/n): ").strip().lower() == "s"
                if brillo:
                    diagnostico = "Falla en la retroiluminación (Inverter/Backlight) de la pantalla."
                else:
                    pitidos = input("¿El equipo emite una serie de pitidos al encender? (s/n): ").strip().lower() == "s"
                    if pitidos:
                        diagnostico = "Falla POST detectada por BIOS (posible error en memoria RAM o procesador)."
                    else:
                        diagnostico = "El equipo enciende pero no da vídeo. Revisar RAM, tarjeta gráfica o cable interno de vídeo (Flex)."
            else:
                pantalla_artefactos = input("¿La pantalla presenta líneas, parpadeos, colores distorsionados o manchas? (s/n): ").strip().lower() == "s"
                
                if pantalla_artefactos:
                    diagnostico = "Falla física en el panel de pantalla o en el chip de video (GPU)."
                else:
                    sistema = input("¿El sistema operativo inicia hasta llegar al escritorio? (s/n): ").strip().lower() == "s"
                    
                    if not sistema:
                        bios_reconoce_disco = input("¿El disco duro/SSD es detectado correctamente en la BIOS/UEFI? (s/n): ").strip().lower() == "s"
                        
                        if not bios_reconoce_disco:
                            diagnostico = "Falla de reconocimiento de almacenamiento. Disco duro/SSD desconectado o dañado."
                        else:
                            pantalla_azul = input("¿Muestra pantalla azul/negra con mensaje de error de arranque? (s/n): ").strip().lower() == "s"
                            if pantalla_azul:
                                diagnostico = "Sistema operativo dañado o archivos de arranque corruptos. Requiere reparación de BCD/SO."
                            else:
                                diagnostico = "El equipo se queda congelado durante el arranque. Posible falla de sectores en disco o drivers."
                    else:
                        sobrecalienta = input("¿El equipo se apaga repentinamente o los ventiladores suenan extremadamente fuerte? (s/n): ").strip().lower() == "s"
                        
                        if sobrecalienta:
                            diagnostico = "Sobrecalentamiento crítico. Requiere mantenimiento térmico (limpieza y cambio de pasta térmica)."
                        else:
                            internet = input("¿Tiene acceso a red local o internet? (s/n): ").strip().lower() == "s"
                            perifericos = input("¿Teclado, mouse/touchpad y puertos USB responden correctamente? (s/n): ").strip().lower() == "s"
                            
                            if not internet:
                                conector_red = input("¿El cable de red o la red Wi-Fi aparecen desconectados totalmente? (s/n): ").strip().lower() == "s"
                                if conector_red:
                                    diagnostico = "Falla de conectividad física o tarjeta de red (Wi-Fi/Ethernet) deshabilitada."
                                else:
                                    diagnostico = "Falla de configuración de red, DNS o controladores de red corruptos."
                            elif not perifericos:
                                diagnostico = "Falla en controladoras USB o controladores de periféricos de entrada."
                            else:
                                fluido = input("¿El rendimiento general del sistema es fluido sin congelamientos? (s/n): ").strip().lower() == "s"
                                if not fluido:
                                    lento_disco = input("¿El uso del disco o memoria RAM se mantiene al 100% en el administrador de tareas? (s/n): ").strip().lower() == "s"
                                    if lento_disco:
                                        diagnostico = "Saturación de hardware. Se recomienda migrar a SSD o ampliar memoria RAM."
                                    else:
                                        diagnostico = "Lentitud general por malware o procesos en segundo plano. Requiere optimización."
                                else:
                                    diagnostico = "El equipo se encuentra en óptimas condiciones operativas."

    garantia = input("\n¿El equipo cuenta con garantía vigente con el fabricante? (s/n): ").strip().lower() == "s"

print("\n" + "=" * 60)
print("                 RESUMEN DEL REPORTE TÉCNICO")
print("=" * 60)
print(f"Número de Reporte  : {numero_reporte}")
print(f"Fecha de Reporte   : {fecha}")
print(f"Hora de Reporte    : {hora}")
print(f"Usuario Registrante: {usuario}")
print(f"Nombre del cliente  : {nombre}")
print(f"Dirección           : {direccion}")
print(f"Tipo de Equipo      : {tipo_equipo}")
print("-" * 60)
print("     DIAGNÓSTICO FINAL")
print("-" * 60)
print(f"Resultado: {diagnostico}")

if detalles_adicionales:
    print("\nObservaciones secundarias:")
    for detalle in detalles_adicionales:
        print(f" - {detalle}")

if garantia:
    print("\n[!] NOTA: El equipo tiene garantía vigente. Se sugiere canalizar con el centro de servicio autorizado.")