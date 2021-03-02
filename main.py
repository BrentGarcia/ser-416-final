from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "abc123"

@app.route('/redir')
def redir():
    return redirect('/')

@app.route('/')
def home():
    if "user" in session and "password" in session:
        if "admin" in session:
            return render_template("admin.html")
        return render_template('index.html')
    return redirect(url_for("login"))

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        password = request.form['pw']
        session["user"] = user
        session["password"] = password
        if (user == "Brent"):
            session['admin'] = True
        return redirect(url_for("home"))
    else:
        if "user" in session and "password" in session:
            return redirect(url_for("home"))
        return render_template("login.html");

@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("password", None)
    session.pop("admin", None)
    return redirect(url_for("login"))

@app.route("/class-signup")
def classSignup():
    return render_template("class-signup.html")

#Internal Services
@app.route("/catering")
def catering():
    return render_template("catering.html")

@app.route("/rental")
def rental():
    return render_template("rental.html")


#External Services
@app.route("/homecare")
def homecare():
    return render_template("homecare.html")

@app.route("/shuttle")
def shuttle():
    return render_template("shuttle.html")

#Admin Backoffice
@app.route("/payroll")
def payroll():
    return render_template("payroll.html")

@app.route("/toggle-services")
def toggle():
    return render_template("toggle-services.html")

@app.route("/create-new-user")
def newUser():
    return render_template("create-new-user.html")

if __name__ == '__main__':
    app.run(debug=True)
