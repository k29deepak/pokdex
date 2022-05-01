# pokdex
App based on REST API to provide Pokemen information  

## Setting up env to run the app
1. Clone repo to your system.
2. Run docker-compose up to start the container.

## API endpoints 
1. Get pokemon data - https://localhost:8000/pokemon/<pokemon_name>
2. Get pokemon data with Transalated Descreption - https://localhost:8000/pokemon/translated/<pokemon_name>



#### Note:
Funtranslations API not working somehow. For Yoda translations replaced spaces with `_` and for Shakespeare translation converted spaces into `-`. 
