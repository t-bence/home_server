# -*- coding: utf-8 -*-
import os

series_root = b'/home/pi/media/sorozatok'
films_root = b'/home/pi/media/filmek'

def get_immediate_subdirectories(a_dir):
    files = [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
    return sorted(files)
            

def get_films_and_series():
    byte_films = get_immediate_subdirectories(films_root)
    films = [film.decode('utf8','replace') for film in byte_films]

    series_names = get_immediate_subdirectories(series_root)
    series = []
    for s in series_names:
        byte_sub_dirs = get_immediate_subdirectories(os.path.join(series_root, s))
        sub_dirs = [dir.decode('utf8','replace') for dir in byte_sub_dirs]
        series += [{'title': s.decode('utf8','replace'), 
            'seasons': sub_dirs}]
        
    return films, series