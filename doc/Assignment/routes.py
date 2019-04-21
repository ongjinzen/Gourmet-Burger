from flask import abort, redirect, render_template, request, url_for

from errors import *
from order import Order
from server import app, system


'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

@app.route('/', methods=["GET", "POST"])
def home():

    if request.method == 'POST':
        
        if request.form.get('action') == 'search':
            try:
                status = system.Check_Status(int(request.form.get('ID')))
            except SystemError as err:
                status = err.message
            except:
                status = 'Order not found.'

            return render_template('home.html', status=status)
        
        elif request.form.get('action') == 'order':
            order = system.Create_Order()
            system.Current_Order = order
            return redirect(url_for('order'))

    
    return render_template('home.html')

@app.route('/order', methods=["GET", "POST"])
def order():

    if request.method == 'POST':
        if request.form.get('action') == 'order':
            system.Delete_Order(system.Current_Order)
            return redirect(url_for('home'))
        elif request.form.get('action') == 'item':
            try:
                item_no = int(request.form['item_no'])
            except:
                return render_template('order.html', order=system.Current_Order, message='Please enter a valid item number.')
            else:
                if item_no > len(system.Current_Order.Items) or item_no < 1:
                    return render_template('order.html', order=system.Current_Order, message='Please enter a valid item number.')
                else:
                    system.Current_Order.Remove_From_Order(system.Current_Order.Items[item_no - 1])
        elif request.form.get('action') == 'submit':
            try:
                system.Submit_Order(system.Current_Order)
            except OrderError as err:
                return render_template('order.html', order=system.Current_Order, message=err.message)
            except SystemError as err:
                system.Delete_Order(system.Current_Order)
                return redirect(url_for('home'))
            else:
                return render_template('order_complete.html', order=system.Current_Order)

    return render_template('order.html', order=system.Current_Order)

@app.route('/menu/<menu>', methods=["GET", "POST"])
def menu(menu):

    if menu == 'main':
        Menu = system.Main_Menu
    elif menu == 'side':
        Menu = system.Side_Menu
    elif menu == 'drink':
        Menu = system.Drink_Menu

    return render_template('menu.html', menu=menu, Menu=Menu, order=system.Current_Order)

@app.route('/item/<item>', methods=["GET", "POST"])
def item(item):

    if request.method == 'GET':
        try:
            system.Current_Item = system.Current_Order.Create_Item(item)
        except ItemError as err:
            if item in ['Burger', 'Wrap', 'Default Burger']:
                menu = 'main'
                Menu = system.Main_Menu
            elif item in ["fries", "nuggets", "chocolate sundae", "strawberry sundae"]:
                menu = 'side'
                Menu = system.Side_Menu
            elif item in ['coke', 'pepsi', "apple juice", "orange juice"]:
                menu = 'drink'
                Menu = system.Drink_Menu

            return render_template('menu.html', menu=menu, Menu=Menu, order=system.Current_Order, message=err.message)
        else:
            if item in ['Default Burger', 'coke', 'pepsi']:
                return render_template('bottled.html', curritem=system.Current_Item, item=item)
            elif item in ['Burger', 'Wrap']:
                return render_template('main.html', curritem=system.Current_Item, item=item)
            elif item in ["apple juice", "orange juice", "fries", "nuggets", "chocolate sundae", "strawberry sundae"]:
                return render_template('sides.html', curritem=system.Current_Item, item=item)

    elif request.method == 'POST':

        if request.form.get('action') == 'add':
            try:
                system.Current_Order.Add_To_Order(system.Current_Item)
            except ItemError as err:
                if item in ['Default Burger', 'coke', 'pepsi']:
                    return render_template('bottled.html', curritem=system.Current_Item, item=item, message=err.message)
                elif item in ['Burger', 'Wrap']:
                    return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
                elif item in ["apple juice", "orange juice", "fries", "nuggets", "chocolate sundae", "strawberry sundae"]:
                    return render_template('sides.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                #return render_template('order.html', order=system.Current_Order)
                return redirect(url_for('order'))
        elif request.form.get('action') =='cancel':
            system.Current_Item.Clear_Ingredients()
            #return render_template('order.html', order=system.Current_Order)
            return redirect(url_for('order'))

        # Custom Burger options
        elif request.form.get('action') in ['white', 'sesame']:
            try:
                system.Current_Item.Bun_Type = request.form.get('action')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'add bun':
            try:
                system.Current_Item.Add_Bun()
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove bun':
            try:
                system.Current_Item.Remove_Bun()
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)


        elif request.form.get('action') in ['beef', 'chicken']:
            try:
                system.Current_Item.Patty_Type = request.form.get('action')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'add patty':
            try:
                system.Current_Item.Add_Patty()
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove patty':
            try:
                system.Current_Item.Remove_Patty()
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        # Custom Wrap options
        elif request.form.get('action') in ['pita', 'tortilla']:
            try:
                system.Current_Item.Wrap_Type = request.form.get('action')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') in ['pork', 'tuna']:
            try:
                system.Current_Item.Filling_Type = request.form.get('action')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        # Main extra options
        elif request.form.get('action') == 'add cheese':
            try:
                system.Current_Item.Add_Other('cheese')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove cheese':
            try:
                system.Current_Item.Remove_Other('cheese')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'add lettuce':
            try:
                system.Current_Item.Add_Other('lettuce')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove lettuce':
            try:
                system.Current_Item.Remove_Other('lettuce')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'add onion':
            try:
                system.Current_Item.Add_Other('onion')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove onion':
            try:
                system.Current_Item.Remove_Other('onion')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'add tomato':
            try:
                system.Current_Item.Add_Other('tomato')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove tomato':
            try:
                system.Current_Item.Remove_Other('tomato')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'add avocado':
            try:
                system.Current_Item.Add_Other('avocado')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        elif request.form.get('action') == 'remove avocado':
            try:
                system.Current_Item.Remove_Other('avocado')
            except ItemError as err:
                return render_template('main.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('main.html', curritem=system.Current_Item, item=item)

        # Fountain drinks and sides options
        elif request.form.get('action') in ['small', 'medium', 'large']:
            try:
                system.Current_Item.Size = request.form.get('action')
            except ItemError as err:
                return render_template('sides.html', curritem=system.Current_Item, item=item, message=err.message)
            else:
                return render_template('sides.html', curritem=system.Current_Item, item=item)

@app.route('/staff', methods=["GET", "POST"])
def staff():

    return render_template('staff.html')

@app.route('/staff/inventory', methods=["GET", "POST"])
def inventory():
    if request.method == 'POST':
        print(f"{request.form}")
        for query in request.form:
            if "update" in query and request.form[query] != '' and int(request.form[query]) > 0 :
                system.Update_Stock(query.replace("_update",''),int(request.form[query]))



    return render_template('inventory.html', system = system)

@app.route('/staff/allOrders', methods=["GET", "POST"])
def allOrders():
    if request.method == 'POST':
        if request.form.get('action') == 'item':
            try:
                deleted = False
                for order in system.Completed_Orders:
                    if order.ID == int(request.form.get('order')):
                        system.Delete_Order(order)
                        deleted = True

                for order in system.Incomplete_Orders:
                    if order.ID == int(request.form.get('order')):
                        system.Delete_Order(order)
                        deleted = True
            except:
                return render_template('all_orders.html', system=system, message='Invalid order number.')
            else:
                if deleted == False:
                    return render_template('all_orders.html', system=system, message='Invalid order number.')
                else:
                    return render_template('all_orders.html', system=system, message='Order deleted.')
        elif request.form.get('action') == 'view':
            try:
                order = system.View_Order(int(request.form.get('order1')))
            except SystemError as err:
                return render_template('all_orders.html', system=system, message=err.message)
            except:
                return render_template('all_orders.html', system=system, message="Invalid order ID.")
            else:
                return render_template('all_orders.html', system=system, order=order)

    return render_template('all_orders.html', system=system)

@app.route('/staff/IncompleteOrders', methods=["GET", "POST"])
def incompleteOrders():
    
    if request.method == 'POST':
        if request.form.get('action') == 'prepare':
            try:
                order = system.View_Order(int(request.form.get('order')))
                system.Preparing_Order(order)
            except SystemError as err:
                return render_template('incomplete.html', system=system, message=err.message)
            except:
                return render_template('incomplete.html', system=system, message="Invalid order ID.")
            else:
                return render_template('incomplete.html', system=system, message="Order status updated.", order=order)
        elif request.form.get('action') == 'complete':
            try:
                order = system.View_Order(int(request.form.get('order1')))
                system.Complete_Order(order)
            except SystemError as err:
                return render_template('incomplete.html', system=system, message=err.message)
            else:
                return render_template('incomplete.html', system=system, message="Order complete.")

    return render_template('incomplete.html', system=system)

@app.route('/staff/CompletedOrders', methods=["GET", "POST"])
def completedOrders():
    if request.method == 'POST':
        if request.form.get('action') == 'view':
            try:
                order = system.View_Order(int(request.form.get('order1')))
            except SystemError as err:
                return render_template('complete.html', system=system, message=err.message)
            except:
                return render_template('complete.html', system=system, message="Invalid order ID.")
            else:
                return render_template('complete.html', system=system, order=order)

    return render_template('complete.html', system=system)
