from flask import Blueprint, flash, redirect, render_template, request 

from pokemon_shop.models import Product, Customer, Order, db 
from pokemon_shop.forms import ProductForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def shop():
    allprods = Product.query.all() 
    allcustomers = Customer.query.all()
    allorders = Order.query.all()

    shop_stats = {
        'products': len(allprods), 
        'customers': len(allcustomers),
        'sales': sum([order.order_total for order in allorders]) 
    }

    return render_template('shop.html', shop=allprods, stats=shop_stats ) 

@site.route('/shop/create', methods=['GET', 'POST'])
def create():
    createform = ProductForm()
    
    if request.method == 'POST' and createform.validate_on_submit():
        name = createform.name.data
        image = createform.image.data
        description = createform.description.data
        price = createform.price.data 
        quantity = createform.quantity.data 
        
        product = Product(name, price, quantity, image, description)
        
        db.session.add(product)
        db.session.commit()
        
        flash(f"You have successfully created product {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/shop/create')
    
    return render_template('create.html', form=createform)

@site.route('/shop/update/<id>', methods=['GET', 'POST'])
def update(id):
    product = Product.query.get(id)
    updateform = ProductForm()
    
    if request.method == 'POST' and updateform.validate_on_submit():
        product.name = updateform.name.data
        product.image = updateform.image.data
        product.description = updateform.description.data
        product.price = updateform.price.data
        product.quantity = updateform.quantity.data 
        
        db.session.commit()
        
        flash(f"You have successfully updated product {product.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/shop/update/{product.prod_id}')
    
    return render_template('update.html', form=updateform, product=product)

@site.route('/shop/delete/<id>')
def delete(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/')
