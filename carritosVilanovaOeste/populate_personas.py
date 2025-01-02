import os
import django

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carritosVilanovaOeste.settings')  # Cambia esto por tu archivo de settings
django.setup()  # Esto inicializa el entorno de Django y carga las apps

# Importación de los modelos
from turnos.models import Persona

# Datos de las personas
personas_data = [
    {"nombre": "Rubén Vilas", "email": "ruben.vilas@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Juani de Vilas", "email": "juani.vilas@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Alexis Pasco", "email": "alexis.pasco@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Pili de Pasco", "email": "pili.pasco@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Carmen Torres", "email": "carmen.torres@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Dalia Pleguezuelos", "email": "dalia.pleguezuelos@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Olga de Vilas", "email": "olga.vilas@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Juana Siles", "email": "juana.siles@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Pilar de Téllez", "email": "pilar.tellez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Isidro Téllez", "email": "isidro.tellez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Ramón Balague", "email": "ramon.balague@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Manoli de Balague", "email": "manoli.balague@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Marc Balague", "email": "marc.balague@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Alex Balague", "email": "alex.balague@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Luis David Peña", "email": "luisdavid.pena@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Aurelia de Jorge", "email": "aurelia.jorge@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mari de García", "email": "mari.garcia@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Enrique Requeni", "email": "enrique.requeni@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Anna de Requeni", "email": "anna.requeni@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Manuel Villa", "email": "manuel.villa@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Inma Mimbrero", "email": "inma.mimbrero@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Loli Luna", "email": "loli.luna@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Pilar Montero", "email": "pilar.montero@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Bianca de Boada", "email": "bianca.boada@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Alejandro Boada", "email": "alejandro.boada@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Matías Trasante", "email": "matias.trasante@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Marisol de Trasante", "email": "marisol.trasante@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Javier Loaiza", "email": "javier.loaiza@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Tatiana de Loaiza", "email": "tatiana.loaiza@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Richard Vilches", "email": "richard.vilches@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Paola de Vilches", "email": "paola.vilches@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Alberto Torres", "email": "alberto.torres@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Jair Gutierrez", "email": "jair.gutierrez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Milady de Gutierrez", "email": "milady.gutierrez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Carlos Gutierrez", "email": "carlos.gutierrez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Nury de Gutierrez", "email": "nury.gutierrez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Rubén Ponce", "email": "ruben.ponce@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Sara de Ponce", "email": "sara.ponce@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Teresa Calzada", "email": "teresa.calzada@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mariana Sandoval", "email": "mariana.sandoval@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Angheluca Duca", "email": "angheluca.duca@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Nicoleta de Duca", "email": "nicoleta.duca@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Vasile Rumaniuc", "email": "vasile.rumaniuc@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mª Dolores de Zambruno", "email": "dolores.zambruno@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "María de Mojada", "email": "maria.mojada@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Leticia de Muñoz", "email": "leticia.munoz@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Diego Trasante", "email": "diego.trasante@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Julieta de Trasante", "email": "julieta.trasante@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Kevin Dunings", "email": "kevin.dunings@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Emily Dunings", "email": "emily.dunings@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Laureano Trasante", "email": "laureano.trasante@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Laura de Trasante", "email": "laura.trasante@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Antonia de Mejuto", "email": "antonia.mejuto@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Pepi de Torres", "email": "pepi.torres@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Enza de Mingo", "email": "enza.mingo@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Oscar Coitinho", "email": "oscar.coitinho@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Carmen de Coitinho", "email": "carmen.coitinho@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Javier Coitinho", "email": "javier.coitinho@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mila González", "email": "mila.gonzalez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Marcos Morales", "email": "marcos.morales@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Iris de Morales", "email": "iris.morales@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Sara Parra", "email": "sara.parra@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mercedes Fernández", "email": "mercedes.fernandez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "José Franco", "email": "jose.franco@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "María de Franco", "email": "maria.franco@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Lucía Morales", "email": "lucia.morales@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mª Luisa Ramos", "email": "maria.luisa.ramos@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Isabel Sellán", "email": "isabel.sellan@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Montse Carcelén", "email": "montse.carcelen@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Sergio Llopis", "email": "sergio.llopis@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Maria de Llopis", "email": "maria.llopis@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Paco Alonso", "email": "paco.alonso@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Andres Guastavino", "email": "andres.guastavino@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Shirley Guastavino", "email": "shirley.guastavino@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Mirko Pomentale", "email": "mirko.pomentale@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Keylin de Pomentale", "email": "keylin.pomentale@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Eloisa Luna", "email": "eloisa.luna@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Miguel A. Román", "email": "miguel.roman@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Montse de Román", "email": "montse.roman@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Walter Fernández", "email": "walter.fernandez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Luciana de Fernández", "email": "luciana.fernandez@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Gabriel García", "email": "gabriel.garcia@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Norma de García", "email": "norma.garcia@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Belén García", "email": "belen.garcia@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Jose Arques", "email": "jose.arques@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Lorena Arques", "email": "lorena.arques@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Alicia Arques", "email": "alicia.arques@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
    {"nombre": "Montse Fuentes", "email": "montse.fuentes@example.com", "telefono": "", "es_capitan": False, "responsabilidades": []},
]

# Función para poblar la base de datos
def populate_personas():
    for persona_data in personas_data:
        # Crear una persona, si no existe
        persona, created = Persona.objects.get_or_create(
            nombre=persona_data['nombre'],
            email=persona_data['email'],
            telefono=persona_data['telefono'],
            es_capitan=persona_data['es_capitan'],
        )
        if created:
            print(f"{persona.nombre} creado con éxito.")
        else:
            print(f"{persona.nombre} ya existía en la base de datos.")

# Ejecutar la función de población
if __name__ == "__main__":
    populate_personas()
