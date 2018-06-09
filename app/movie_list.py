# -*- coding: utf-8 -*-
import os

series_root = u'/home/pi/hdd/media/sorozatok'
films_root = u'/home/pi/hdd/media/filmek'

def get_immediate_subdirectories(a_dir):
    files = [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
    return sorted(files)
            

def get_films_and_series():
    films = get_immediate_subdirectories(films_root)

    series_names = get_immediate_subdirectories(series_root)
    series = []
    for s in series_names:
        series += [{'title': s, 'seasons': get_immediate_subdirectories(os.path.join(series_root, s))}]
        
    return films, series 