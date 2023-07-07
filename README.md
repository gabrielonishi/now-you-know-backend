# Now You Know - O quanto você conhece seu artista favorito?

> And if you don't know, now you know!

Backend para a aplicação web Now You Know, um simples jogo de trivia com um simples objetivo: testar o seu conhecimento a respeito de seu artista favorito! Escolha um artista e tente adivinhar as 5 músicas mais populares deles na plataforma Genius

O frontend foi construído com React e o backend utiliza Django e uma API pública do Genius para funcionar. O backend está disponível em https://github.com/gabrielonishi/now-you-know-backend

## Como rodar

<h2>Acesso remoto via</h2>
https://serene-peak-43585.herokuapp.com/ <br>
<b>Nota</b>: É possível que o seu navegador/provedor de internet bloqueie o backend por razões de segurança. Caso isso aconteça, tente alimentar a internet via roteador do celular

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
 - Para publicar uma tentativa (POST): /api/nome_do_artista/tries<br>
 - Para ver informações do artista (GET): /api/nome_do_artista
