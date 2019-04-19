from flask import render_template, request, redirect, url_for, abort
from server import app, system
from datetime import datetime
from system import *



'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


@app.route('/staff', methods=["GET", "POST"])
def staff():
    
    return render_template('staff.html')

@app.route('/staff/inventory', methods=["GET", "POST"])
def Inventory():
    if request.method == 'POST':
        print(f"{request.form}")
        for query in request.form:
            if "update" in query and request.form[query] != '' and int(request.form[query]) > 0 :
                system.Update_Stock(query.replace("_update",''),int(request.form[query]))



    return render_template('Inventory.html', system = system)

@app.route('/staff/AllOrders', methods=["GET", "POST"])
def allOrders():
    
    return render_template('staff.html')

@app.route('/staff/IncompleteOrders', methods=["GET", "POST"])
def incompleteOrders():
    
    return render_template('staff.html')

@app.route('/staff/CompleltedOrders', methods=["GET", "POST"])
def completedOrders():
    
    return render_template('staff.html')

