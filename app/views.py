# -*- coding: utf-8 -*-
from app import app
from flask import render_template, jsonify, request
from .bkk_api import get_trams
from .cinemas import get_screenings
from .movie_list import get_films_and_series
from .lenses import get_lenses
from .status import get_system_data
from .pollution import save_measurement
from .temp_log import parse_temp_log


@app.route('/')
@app.route('/index')
def index():
    filmlist, serieslist = get_films_and_series()
    return render_template('index.html', filmlist=filmlist, serieslist=serieslist, title=u'Filmek és sorozatok')

@app.route('/kozlekedes')    
def jaratok():
    all_data, lines = get_trams()
    #trams = [{'number': '56X', 'mins': '3', 'direction': 'Baba'}]
    return render_template('villamos.html', 
                           title='Villamos', all_data=all_data, lines=lines)
                           
@app.route('/kozlekedes-<int:tram_id>')
def villamos(tram_id):
    try:
        all_data, lines = get_trams(tram_id)
    except IndexError:
        return page_not_found()
        
    return render_template('villamos.html', 
                           title='Villamos', all_data=all_data, lines=lines)
                           
@app.route('/mozimusor')
def mozimusor():
    cinemas, lastupdate = get_screenings()
    return render_template('mozimusor.html', 
                           title=u'Moziműsor', lastupdate=lastupdate, cinemas=cinemas)
                           
@app.route('/objektiv')  
def objektivek():
    lenses, lastupdate = get_lenses()
    return render_template('objektiv.html', 
                           title=u'Objektívek', lastupdate=lastupdate, lenses=lenses)

@app.route('/status')    
def status():
    systemdata = get_system_data()
    return render_template('status.html', 
                           title=u'Státusz', results=systemdata)
                           
#@app.route('/torrent')
#def torrentek():
#    return render_template('torrentek.html', 
#                           title=u'Torrentek')
                           
@app.route('/temperature')
def homerseklet():
    date, temp, cpu = parse_temp_log('/home/pi/bin/temp.log')
    return render_template('homerseklet.html', temp=temp, date=date, cpu=cpu, title=u'Hőmérséklet')
                           
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
                           
@app.route('/pollution')    
def pollution_measurement():
    number = request.args.get('value', 1, type=float)
    save_measurement(number)
    return jsonify( { 'result': 200 } )
                           
