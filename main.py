#Importa pandas y usa un alias para poder utilizar sus recursos
import pandas as pd
def main():
    #Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
    titulos = pd.read_csv('imdb_titulos.csv')
    print(titulos.head(), '\n')
    #Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
    elenco = pd.read_csv('imdb_elenco.csv')
    print(elenco.head(), '\n')
    #Mostrar el número de registros del dataframe de titulos
    print('Número de registros del dataframe de titulos: ', len(titulos), '\n')
    #Mostrar el número de registros del dataframe de elenco
    print('Número de registros del dataframe de elenco: ', len(elenco), '\n')
    #Mostrar las 5 peliculas más antiguas del listado de titulos
    print('Las 5 peliculas más antiguas son: \n', titulos.sort_values('year').head(), '\n')
    #Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
    print('Las peliculas que en el titulo tienen la palabra "Dracula" son: \n', titulos[titulos['title'].str.contains('Dracula')], '\n')
    print('El número total de peliculas que coinciden con este requisito es: ', len(titulos[titulos['title'].str.contains('Dracula')]), '\n')
    #Mostrar los 10 titulos más comunes (que más se repiten)
    
    #Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
    #Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
    #Mostrar cuantas peliculas fueron hechas en el año 1950
    #Mostrar cuantas peliculas fueron hechas de 1950 a 1959
    #Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
    #Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
    #Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
    #Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
    #Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
    #Mostrar cuantos papeles para actores hubo en la década de los 50's
    #Mostrar cuantos papeles para actrices hubo en la década de los 50's

