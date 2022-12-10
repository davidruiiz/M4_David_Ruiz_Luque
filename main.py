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
    print('Los 10 titulos más comunes son: \n', titulos['title'].value_counts().head(10), '\n')

    #Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
    print('La primer pelicula hecha titulada "Romeo and Juliet" es: \n', titulos[titulos['title'] == 'Romeo and Juliet'].sort_values('year').head(1), '\n')

    #Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
    print('Las peliculas que contienen la palabra "Exorcist" ordenadas de la más vieja a la más reciente son: \n', titulos[titulos['title'].str.contains('Exorcist')].sort_values('year'), '\n')

    #Mostrar cuantas peliculas fueron hechas en el año 1950
    print('Las peliculas que fueron hechas en el año 1950 son: \n', titulos[titulos['year'] == 1950], '\n')

    #Mostrar cuantas peliculas fueron hechas de 1950 a 1959
    print('Las peliculas que fueron hechas de 1950 a 1959 son: \n', titulos[(titulos['year'] >= 1950) & (titulos['year'] <= 1959)], '\n')

    #Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
    print('Los roles o papeles que hubo en la pelicula "The Godfather" son: \n', elenco[elenco['title'] == 'The Godfather']['category'], '\n')

    #Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
    print('El elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958 es: \n', elenco[(elenco['title'] == 'Dracula') & (elenco['year'] == 1958)].sort_values('n'), '\n')

    #Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
    print('Los papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas: \n', len(elenco[elenco['character'] == 'Bruce Wayne']), '\n')

    #Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
    print('Los papeles que ha hecho "Robert De Niro" en su carrera son: \n', len(elenco[elenco['name'] == 'Robert De Niro']), '\n')

    #Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
    print('Los papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60\'s, ordenado por año de forma descendente son: \n', elenco[(elenco['name'] == 'Charlton Heston') & (elenco['n'] == 1) & (elenco['year'] >= 1960) & (elenco['year'] <= 1969)].sort_values('year', ascending=False), '\n')

    #Mostrar cuantos papeles para actores hubo en la década de los 50's
    print('Los papeles para actores hubo en la década de los 50\'s son: \n', len(elenco[(elenco['category'] == 'actor') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)]), '\n')

    #Mostrar cuantos papeles para actrices hubo en la década de los 50's
    print('Los papeles para actrices hubo en la década de los 50\'s son: \n', len(elenco[(elenco['category'] == 'actress') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)]), '\n')

if __name__ == '__main__':
    main()
