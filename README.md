<h1>Projeto 2 - Tecnologias Web</h1>

Gabriel Onishi e Lucas Oliveira

<h2>Imports</h2>
<ul>
<li>Django v4.0.4</li>
<li>Django REST Framework v3.13.1</li>
<li>Markdown v3.3.7</li>
<li>Django-filter v21.1</li>
<li>psycopg2 v2.9.3</li>
<li>Django CORS headers v3.12.0</li>
<li>gunicorn v20.1.0</li>
<li>dj-database-url v0.5.0</li>
</ul>

<h2>Para rodar o back-end</h2>
```
$ ./nowyouknow> python manage.py runserver
```

<h2>Endpoints Utilizadas</h2>
 - Para publicar uma tentativa (POST): /api/nome_do_artista/tries
 - Para ver informações do artista (GET): /api/nome_do_artista