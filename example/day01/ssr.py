# Server Side Rendering
# Carregar dados

dados = [
    {'nome': 'Vitor', 'cidade': 'Curitiba'},
    {'nome': 'Bruno', 'cidade': 'Viana'},
    {'nome': 'Guido', 'cidade': 'Amsterdan'}
]
# Processar
template = """\
<html>
<body>
    <ul>
        <li> Nome: {dados[nome]} </li>
        <li> Cidade: {dados[cidade]}</li>
    </ul>
</body>
</html>

"""
# \r\n\r\n
# Renderizar 
for item in dados:
    print(template.format(dados=item))