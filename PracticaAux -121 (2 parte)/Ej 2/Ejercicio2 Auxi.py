#Nivel 0 (Clase Base Raíz): SerVivo
#   Nivel 1: Planta
#       Nivel 2: Flor
#   Nivel 1: Animal
#       Nivel 2: Humano
#           Nivel 3: Niño
#           Nivel 3: Adulto
#           Nivel 3: Anciano
#       Nivel 2: Felino
#           Nivel 3: Gato
#           Nivel 3: León
#       Nivel 2: Roedor
#           Nivel 3: Ratón
#           Nivel 3: Conejo
#       Nivel 2: Reptil
#           Nivel 3: Vívora
#       Nivel 2 (Específico): Rana (Es un anfibio no entra en categoria reptil)
#                           
#                           +-------------------+
#                           |      SerVivo      |
#                           +-------------------+
#                                 /       \
#                                /         \
#            +------------------+           +-------------------+
#            |      Planta      |           |      Animal       |
#            +------------------+           +-------------------+
#                     |                       /   |      |    \      \
#           +------------------+             /    |      |     \      \
#           |       Flor       |            /     |      |      \      \
#            +-----------------+           S/      |      |       \      \
#                                         /       |      |        \      \
#               +------------------------+  +--------+ +--------+ +------+ +------+
#               |        Humano          |  | Felino | | Roedor | |Reptil| | Rana |
#               +------------------------+  +--------+ +--------+ +------+ +------+
#               /        |         \          /    \     /    \      |
#              /         |          \        /      \   /      \     |
#      +------+      +--------+     +-------+ +----+ +----+ +-----++------++------+
#      | Niño |      | Adulto |     |Anciano| |Gato| |León| |Ratón||Conejo||Vívora|
#      +------+      +--------+     +-------+ +----+ +----+ +----+ +------++------+
#
#b) Clases con sus Atributos Significativos (1 a 3 atributos)
# SerVivo
#   - edad: int
#   - habitat: str
# Planta
#   - tipeFotosintesis: str
#   - alturaMts: float
# Flor
#   - colorPetalos: str
#   - Aroma: bool
# Animal
#   - tipoAlimentacion: str
#   - desplazaPor: str
# Humano
#   - nombre: str
#   - identificacion: str
# Niño
#   - gradoEscolar: str
#   - tutor: str
# Adulto
#   - profesion: str
#   - estadoCivil: str
# Anciano
#   - jubilation: str
#   - Cuidados: bool
# Felino
#   - longGarras: float
#   - CazadorNocturno: bool
# Gato
#   - raza: str
#   - estaEsterilizado: bool
# León
#   - tamanoMelena: str
#   - LiderManada: bool
# Roedor
#   - longitudDientes: float
#   - tipeMadriguera: str
# Ratón
#   - colorPelaje: str
#   - Domestico: bool
# Conejo
#   - longitudOrejas: float
#   - tipoSalto: str
# Reptil
#   - tipoEscamas: str
#   - esVenenoso: bool
# Vívora
#   - longitudCuerpo: float
#   - tipoVeneno: str
# Rana
#   - tipoPiel: str
#   - distanciaSalto: float