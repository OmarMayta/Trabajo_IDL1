# logica.py

class Trabajador:
    def __init__(self, nombre, estado="Activo"):
        # Atributos privados con getters y setters
        self._nombre = nombre
        self._estado = estado
        self._jefe = None  # Apunta a otro Trabajador o None

    # ============ Getters y Setters ============
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_jefe(self):
        return self._jefe

    def set_jefe(self, jefe):
        self._jefe = jefe

    # ============ Métodos requeridos ============
    def def_resumen(self):
        """
        Retorna el puesto/rango del trabajador.
        (Las subclases lo personalizan.)
        """
        return "Resumen genérico de trabajador"

    def def_jefe_inmediato(self):
        """
        Retorna el nombre del jefe inmediato
        (Si no tiene jefe, retorna 'No tiene jefe').
        """
        if self._jefe:
            return self._jefe.get_nombre()
        return "No tiene jefe"

    def def_estado(self):
        """
        Retorna el estado del trabajador.
        (TC, D, R o Activo)
        """
        return self._estado


class Gerente(Trabajador):
    def __init__(self, nombre, estado="Activo"):
        super().__init__(nombre, estado)
        self._puesto = "Gerente"

    def def_resumen(self):
        return f"{self.get_nombre()} - {self._puesto}"


class JefeArea(Trabajador):
    def __init__(self, nombre, area, estado="Activo"):
        super().__init__(nombre, estado)
        self._area = area
        self._puesto = f"Jefe de {area}"

    def def_resumen(self):
        return f"{self.get_nombre()} - {self._puesto}"


class Asistente(Trabajador):
    def __init__(self, nombre, area, estado="Activo"):
        super().__init__(nombre, estado)
        self._area = area
        self._puesto = f"Asistente de {area}"

    def def_resumen(self):
        return f"{self.get_nombre()} - {self._puesto}"


class Tecnico(Trabajador):
    def __init__(self, nombre, area, anios_experiencia, estado="Activo"):
        super().__init__(nombre, estado)
        self._area = area
        self._puesto = f"Técnico de {area}"
        self._anios_experiencia = anios_experiencia

    def def_resumen(self):
        """
        Además de puesto/rango, muestra los años de experiencia.
        """
        return f"{self.get_nombre()} - {self._puesto} ({self._anios_experiencia} años de experiencia)"


def crear_trabajadores():
    """
    Crea y retorna una lista (array) de objetos Trabajador:
      - 1 Gerente
      - 5 Jefes de área
      - 1 o 2 Asistentes por cada Jefe de área
      - 3 o 5 Técnicos por cada Jefe de área
    """

    # 1) Creamos el Gerente
    gerente = Gerente("Carlos Gerente")

    # 2) Creamos 5 jefes de área
    #    (Marketing, Sistemas, Producción, Logística, y un extra, p.ej. Finanzas)
    lista_areas = ["Marketing", "Sistemas", "Producción", "Logística", "Finanzas"]
    jefes = []

    # 3) Asistentes y Técnicos
    asistentes = []
    tecnicos = []

    for area in lista_areas:
        # Crear un Jefe de área
        jefe_area = JefeArea(f"{area} - Jefe", area)
        jefe_area.set_jefe(gerente)
        jefes.append(jefe_area)

        # Crear 1 o 2 asistentes (ejemplo: 2 asistentes por área)
        asistente1 = Asistente(f"Asistente 1 de {area}", area)
        asistente1.set_jefe(jefe_area)
        asistentes.append(asistente1)

        asistente2 = Asistente(f"Asistente 2 de {area}", area)
        asistente2.set_jefe(jefe_area)
        asistentes.append(asistente2)

        # Crear 3 o 5 técnicos (ejemplo: 3 técnicos por área)
        for i in range(1, 4):
            # anios_experiencia arbitrarios
            tecnico = Tecnico(f"Técnico {area} {i}", area, anios_experiencia=i + 1)
            tecnico.set_jefe(jefe_area)
            tecnicos.append(tecnico)

    # 4) Unir todo en una sola lista
    trabajadores = [gerente] + jefes + asistentes + tecnicos
    return trabajadores
