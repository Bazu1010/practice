from flask import Flask,render_template,request,redirect
from dbservice import get_data, add_sale, insert_f
import psycopg2

app = Flask (__name__)


@app.route("/")
def index1():
    return render_template("index.html")



## Get Data from fruits Table
@app.route("/fruits")
def products():
    myfruits = get_data("fruits")
    return render_template("fruits.html", myfruits = myfruits)

## Add a new fruit in the fruits list

@app.route("/add_fruits", methods=["POST"])
def insert_fruit():
   fruits_name   = request.form["fruit_name"]
   buying_price = request.form["buying_price"]
   selling_price = request.form["selling_price"]
   quantity     = request.form["quantity"]
    
   values =(fruits_name,buying_price, selling_price, quantity)

   insert_f(values)

   return redirect("/fruits")


## Get data from the sales Table
@app.route("/sales")
def sales():
    get_sales = get_data("sales")
    my_fruits = get_data("fruits")
    return render_template("sales.html", mysales = get_sales, my_fruits= my_fruits)

## Inserting new sale

@app.route("/add_sales", methods=["POST"])
def insert_sale():
    sale_quantity = request.form["sale_quantity"]

    values = (sale_quantity)

    add_sale(values)

    return redirect("/sales")

    
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

app.run(debug=True)