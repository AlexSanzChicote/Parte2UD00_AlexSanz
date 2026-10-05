from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


# Base para definir los modelos
Base = declarative_base()


# Tabla de asociación para la relación muchos a muchos
alumno_asignatura = Table(
   'alumno_asignatura',
   Base.metadata,
   Column('alumno_id', Integer, ForeignKey('alumnos.id'), primary_key=True),
   Column('asignatura_id', Integer, ForeignKey('asignaturas.id'), primary_key=True)
)


# Modelo para la tabla de asignaturas
class Asignatura(Base):
   __tablename__ = 'asignaturas'


   id = Column(Integer, primary_key=True, autoincrement=True)
   nombre = Column(String(100), nullable=False)
   alumnos = relationship("Alumno", secondary=alumno_asignatura, back_populates="asignaturas")


# Modelo para la tabla de alumnos
class Alumno(Base):
   __tablename__ = 'alumnos'


   id = Column(Integer, primary_key=True, autoincrement=True)
   nombre = Column(String(50), nullable=False)
   apellidos = Column(String(100), nullable=False)
   email = Column(String(100), unique=True, nullable=False)
   asignaturas = relationship("Asignatura", secondary=alumno_asignatura, back_populates="alumnos")


# Conexión a SQLite y creación de las tablas
engine = create_engine('sqlite:///escuela.db', echo=False)
Base.metadata.create_all(engine)


# Gestor de sesiones para interactuar con la BD
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
   # Consulta para comprobar si ya hay alumnos guardados
   alumnos = session.query(Alumno).all()


   if not alumnos:
       # La primera vez crea y guarda los datos
       asig1 = Asignatura(nombre="Acceso a Datos")
       asig2 = Asignatura(nombre="Desarrollo de Interfaces")


       nuevo_alumno = Alumno(
           nombre="Marc",
           apellidos="Giménez Pérez",
           email="marc.gimenez@email.com",
           asignaturas=[asig1, asig2]
       )


       session.add(nuevo_alumno)
       session.commit()
       print("Datos guardados en la base de datos.")
   else:
       # Recupera los datos guardados en el archivo
       print("Datos recuperados de la base de datos:")
       for a in alumnos:
           print(f"Alumno: {a.nombre} {a.apellidos} - Email: {a.email}")
           for asig in a.asignaturas:
               print(f"  - Asignatura: {asig.nombre}")


   session.close()
