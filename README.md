# SearchTech

Esse site foi desenvolvido como requisito da matéria Análise e Projeto de Software no Instituto Federal do Rio Grande do Sul Campus Ibirubá. 
O seu intuito é agregar os projetos desenvolvidos pela Nasa e permitir criar uma comunidade ao redor deles. Bem como, futuramente, recomendar noticias e atualizações conforme os interesses das pessoas

![image](https://user-images.githubusercontent.com/52550134/212673527-0bfa682e-946a-4e44-82ef-3109972c597d.png)


## Como executar localmente

Instale a versão mais atualizada do python conforme o seu sistema operacional demandar;

Clone o projeto para sua pasta de preferência;

```
git clone https://github.com/gusgewehr/SearchTech.git
```

Vá para a pasta raiz do projeto;
```
cd SearchTech
```

Instale os requisitos;
```
pip install -r requirements.txt
```

Inicie o servidor local;
```
python manage.py runserver 0.0.0.0:8080
```

Se necessário crie um superusuário;
```
python manage.py createsuperuser $USUARIO
```
