from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario


# with app.app_context():
#     database.create_all()
# #     database.drop_all()

with app.app_context():
    Usuario.query.all()
    print(Usuario.query.all())
    usuario1 = Usuario.query.filter_by(username='Guilherme').first()
    print(usuario1)
    # meus_usuarios = Usuario.query.first()
    print(usuario1.username)
    print(usuario1.email)
    print(usuario1.senha)
    print(usuario1.cursos)