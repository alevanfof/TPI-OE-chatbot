def chatbot_principal():
    mostrar_cabecera()

    empleados = cargar_empleados()

    while True:

        opcion = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()

        if opcion.lower() not in ["si", "s", "sí", "iniciar"]:
            continue

        solicitud_activa = True

        id_empleado = ""
        nombre_empleado = ""
        dias_disponibles = 0

        while solicitud_activa:

            bot_imprimir("Ingresá tu ID de empleado (ej: EMP002) o '/cancelar':")

            id_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip().upper()

            if id_input == "/CANCELAR":
                bot_imprimir("❌ Solicitud abortada por el usuario.")
                solicitud_activa = False
                break

            elif id_input == "/AYUDA":
                mostrar_ayuda()
                continue

            elif id_input == "/EMPLEADOS":
                mostrar_empleados_consola(empleados)
                continue

            sys_imprimir(f"Validando ID '{id_input}' en empleados.txt...")

            if id_input in empleados:

                id_empleado = id_input
                nombre_empleado = empleados[id_input]["nombre"]
                dias_disponibles = empleados[id_input]["disponibles"]

                bot_imprimir(f"Empleado: {nombre_empleado}")
                bot_imprimir(f"Saldo disponible: {dias_disponibles} días")

                if dias_disponibles <= 0:
                    bot_imprimir("⚠️ Saldo insuficiente.")
                    solicitud_activa = False
                    break

                break

            else:
                bot_imprimir("❌ Error: ID no encontrado.")