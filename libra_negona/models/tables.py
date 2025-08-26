# _*_ coding: utf-8 _*_
Filmes= db.define_table('filmes',
    Field('titulo','string',label = 'Título'),
    Field('lancamento','integer',label= 'Lamçamento'),
    Field('duracao','integer', label= 'Duraçao'),
    Field('genero','list:string',label='Genero'),
    Field('diretor','string',label= 'Diretor'),
    Field('capa','upload',label='capa'),
    Field('data_cadastro','datetime',label= 'Data de cadatros')
)