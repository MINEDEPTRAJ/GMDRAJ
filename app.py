from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# ---- Product catalogue -----------------------------------------------
# Edit this list to add, remove, or reprice products. No database needed
# for a small static catalogue like this.
PRODUCTS = [
    {
        "name": "CHOKHOPANI Sip",
        "size": "200 ML",
        "pack": "Pack of 48",
        "desc": "Single-serve bottle for functions, offices and travel.",
    },
    {
        "name": "CHOKHOPANI Everyday",
        "size": "500 ML",
        "pack": "Pack of 24",
        "desc": "The everyday size — desk, gym bag, car door pocket.",
    },
    {
        "name": "CHOKHOPANI Family",
        "size": "1 LITRE",
        "pack": "Pack of 12",
        "desc": "For the dining table and the family fridge.",
    },
    {
        "name": "CHOKHOPANI Home",
        "size": "2 LITRE",
        "pack": "Pack of 9",
        "desc": "Fewer bottles to restock, same eleven-stage process.",
    },
    {
        "name": "CHOKHOPANI Jar",
        "size": "20 LITRE",
        "pack": "Returnable jar",
        "desc": "For office and home water coolers — refill and return.",
    },
]


@app.context_processor
def inject_globals():
    """Values every template can use without passing them explicitly."""
    return {"year": datetime.now().year}


@app.route("/")
def index():
    return render_template("index.html", active="home", products=PRODUCTS)


@app.route("/products")
def products():
    return render_template("products.html", active="products", products=PRODUCTS)


@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted = False
    name = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # TODO: replace this with a real integration — e.g. send an email,
        # save to a spreadsheet/CRM, or post to a Slack/WhatsApp webhook.
        app.logger.info("New enquiry: name=%s phone=%s email=%s message=%s",
                         name, phone, email, message)
        submitted = True

    return render_template("contact.html", active="contact",
                            submitted=submitted, name=name)


if __name__ == "__main__":
    app.run(debug=True)
