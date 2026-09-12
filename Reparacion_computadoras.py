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


# P = Hay electricidad en la red general
# Q = El tomacorriente entrega energía
# R = El LED de carga se enciende
# S = El equipo enciende (luces/ventiladores)
# T = El interruptor trasero de la fuente está encendido
# U = Muestra imagen/texto en pantalla
# V = Se ve imagen al fondo con linterna
# W = Emite pitidos de error al encender
# X = Presenta artefactos o distorsión visual
# Y = El sistema operativo inicia hasta el escritorio
# Z = La BIOS detecta el disco duro/SSD
# A = Muestra pantalla azul/negra de error de arranque
# B = Presenta sobrecalentamiento crítico
# C = Tiene acceso a red/internet
# D = Conector de red/Wi-Fi desconectado
# E = Teclado/mouse/USB responden correctamente
# F = Rendimiento general es fluido
# G = Uso de disco/RAM al 100% en Administrador de Tareas
# H = Cuenta con garantía vigente

# Evaluamos P
P = input("¿Hay suministro eléctrico general en el inmueble/zona? (s/n): ").strip().lower() == "s"

# Evaluamos ¬P
if not P:
    diagnostico = "Corte general de energía eléctrica. Esperar a que se restablezca el servicio en la zona."
else:
    # Evaluamos P ∧ Q
    Q = input("¿El tomacorriente o regulador entrega energía a otros aparatos? (s/n): ").strip().lower() == "s"
    
    # Evaluamos P ∧ ¬Q
    if not Q:
        diagnostico = "Falla en la fuente de alimentación externa (falla en el tomacorriente, regulador o UPS)."
    else:
        if tipo_equipo in ["Laptop", "Tablet"]:
            # Evaluamos R
            R = input("¿El LED indicador de carga en el equipo se enciende al conectar el cargador? (s/n): ").strip().lower() == "s"
            # Evaluamos ¬R
            if not R:
                detalles_adicionales.append("El equipo no detecta la conexión del cargador o el cargador está defectuoso.")

        # Evaluamos S
        S = input("¿Enciende el equipo (emite luces, pitidos o sonidos de ventiladores)? (s/n): ").strip().lower() == "s"
        
        # Evaluamos (P ∧ Q) ∧ ¬S
        if not S:
            if tipo_equipo == "PC":
                # Evaluamos T
                T = input("¿El interruptor trasero de la fuente de poder (I/O) está encendido? (s/n): ").strip().lower() == "s"
                # Evaluamos (P ∧ Q ∧ ¬S) ∧ ¬T
                if not T:
                    diagnostico = "La fuente de poder está apagada físicamente desde el switch trasero."
                else:
                    diagnostico = "Falla total de encendido. Posible daño en fuente de poder, botón de encendido o tarjeta madre."
            else:
                diagnostico = "Falla total de encendido. Posible daño en la placa base o batería completamente agotada/dañada."
        
        # Evaluamos (P ∧ Q) ∧ S
        else:
            # Evaluamos U
            U = input("¿Muestra alguna imagen o texto en la pantalla al encender? (s/n): ").strip().lower() == "s"
            
            # Evaluamos (P ∧ Q ∧ S) ∧ ¬U
            if not U:
                # Evaluamos V
                V = input("¿Se ve la pantalla muy al fondo con una linterna o tiene el brillo al mínimo? (s/n): ").strip().lower() == "s"
                # Evaluamos (P ∧ Q ∧ S ∧ ¬U) ∧ V
                if V:
                    diagnostico = "Falla en la retroiluminación (Inverter/Backlight) de la pantalla."
                else:
                    # Evaluamos W
                    W = input("¿El equipo emite una serie de pitidos al encender? (s/n): ").strip().lower() == "s"
                    # Evaluamos (P ∧ Q ∧ S ∧ ¬U ∧ ¬V) ∧ W
                    if W:
                        diagnostico = "Falla POST detectada por BIOS (posible error en memoria RAM o procesador)."
                    else:
                        diagnostico = "El equipo enciende pero no da vídeo. Revisar RAM, tarjeta gráfica o cable interno de vídeo (Flex)."
            
            # Evaluamos (P ∧ Q ∧ S) ∧ U
            else:
                # Evaluamos X
                X = input("¿La pantalla presenta líneas, parpadeos, colores distorsionados o manchas? (s/n): ").strip().lower() == "s"
                
                # Evaluamos (P ∧ Q ∧ S ∧ U) ∧ X
                if X:
                    diagnostico = "Falla física en el panel de pantalla o en el chip de video (GPU)."
                else:
                    # Evaluamos Y
                    Y = input("¿El sistema operativo inicia hasta llegar al escritorio? (s/n): ").strip().lower() == "s"
                    
                    # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X) ∧ ¬Y
                    if not Y:
                        # Evaluamos Z
                        Z = input("¿El disco duro/SSD es detectado correctamente en la BIOS/UEFI? (s/n): ").strip().lower() == "s"
                        
                        # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ ¬Y) ∧ ¬Z
                        if not Z:
                            diagnostico = "Falla de reconocimiento de almacenamiento. Disco duro/SSD desconectado o dañado."
                        else:
                            # Evaluamos A
                            A = input("¿Muestra pantalla azul/negra con mensaje de error de arranque? (s/n): ").strip().lower() == "s"
                            # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ ¬Y ∧ Z) ∧ A
                            if A:
                                diagnostico = "Sistema operativo dañado o archivos de arranque corruptos. Requiere reparación de BCD/SO."
                            else:
                                diagnostico = "El equipo se queda congelado durante el arranque. Posible falla de sectores en disco o drivers."
                    
                    # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X) ∧ Y
                    else:
                        # Evaluamos B
                        B = input("¿El equipo se apaga repentinamente o los ventiladores suenan extremadamente fuerte? (s/n): ").strip().lower() == "s"
                        
                        # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y) ∧ B
                        if B:
                            diagnostico = "Sobrecalentamiento crítico. Requiere mantenimiento térmico (limpieza y cambio de pasta térmica)."
                        else:
                            # Evaluamos C y E
                            C = input("¿Tiene acceso a red local o internet? (s/n): ").strip().lower() == "s"
                            E = input("¿Teclado, mouse/touchpad y puertos USB responden correctamente? (s/n): ").strip().lower() == "s"
                            
                            # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y ∧ ¬B) ∧ ¬C
                            if not C:
                                # Evaluamos D
                                D = input("¿El cable de red o la red Wi-Fi aparecen desconectados totalmente? (s/n): ").strip().lower() == "s"
                                # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y ∧ ¬B ∧ ¬C) ∧ D
                                if D:
                                    diagnostico = "Falla de conectividad física o tarjeta de red (Wi-Fi/Ethernet) deshabilitada."
                                else:
                                    diagnostico = "Falla de configuración de red, DNS o controladores de red corruptos."
                            
                            # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y ∧ ¬B ∧ C) ∧ ¬E
                            elif not E:
                                diagnostico = "Falla en controladoras USB o controladores de periféricos de entrada."
                            
                            # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y ∧ ¬B ∧ C ∧ E)
                            else:
                                # Evaluamos F
                                F = input("¿El rendimiento general del sistema es fluido sin congelamientos? (s/n): ").strip().lower() == "s"
                                
                                # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y ∧ ¬B ∧ C ∧ E) ∧ ¬F
                                if not F:
                                    # Evaluamos G
                                    G = input("¿El uso del disco o memoria RAM se mantiene al 100% en el administrador de tareas? (s/n): ").strip().lower() == "s"
                                    # Evaluamos (P ∧ Q ∧ S ∧ U ∧ ¬X ∧ Y ∧ ¬B ∧ C ∧ E ∧ ¬F) ∧ G
                                    if G:
                                        diagnostico = "Saturación de hardware. Se recomienda migrar a SSD o ampliar memoria RAM."
                                    else:
                                        diagnostico = "Lentitud general por malware o procesos en segundo plano. Requiere optimización."
                                else:
                                    diagnostico = "El equipo se encuentra en óptimas condiciones operativas."

    # Evaluamos H
    H = input("\n¿El equipo cuenta con garantía vigente con el fabricante? (s/n): ").strip().lower() == "s"

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

if H:
    print("\n[!] NOTA: El equipo tiene garantía vigente. Se sugiere canalizar con el centro de servicio autorizado.")