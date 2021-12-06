from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)
app.secret_key = "pyblog"

#MYSQL Configration

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flaskblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

#MYSQL Configration End

#User Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Please login to view this page!","danger")
            return redirect(url_for("login"))
    return decorated_function
#User Login Required Decorator End


#Classes

#SignUp Form
class Sign_Up_Form(Form):
    name = StringField("Name :",validators = [validators.Length(min = 3, max = 25)])
    username = StringField("Username :",validators = [validators.Length(min = 5, max = 35)])
    email = StringField("Email :",validators = [validators.Email(message = "Enter a valid email!")])
    password = PasswordField("Password :",validators = [
        validators.DataRequired(message = "Please set a password!"),
        validators.EqualTo(fieldname = "confirm_password",message = "Passwords do not match!")
    ])
    confirm_password = PasswordField("Verfiy Password :")

#Login Form
class Login_Form(Form):
    username = StringField("Username :",validators = [validators.DataRequired(message = "Please enter your username!")])
    password = PasswordField("Password :",validators = [validators.DataRequired(message = "Please enter your password!")])

#Article Form
class Article_Form(Form):
    title = StringField("Title :",validators = [
        validators.DataRequired(message = "Please enter your article title!"),
        validators.Length(min = 5,max = 100)])
    content = TextAreaField("Content :",validators = [
        validators.DataRequired(message = "Please enter your article content!"),
        validators.Length(min = 10)])
    imgurl = TextAreaField("Image Url :")

#Classes End

#Routes

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/about")
def about():

    return render_template("about_us.html")

@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM ARTICLES"

    result = cursor.execute(query)

    if result > 0:
        articles = cursor.fetchall()
        return render_template("article/articles.html",articles = articles)
    else:
        return render_template("article/articles.html")
        cursor.close()

@app.route("/article/<string:id>")
def details_article(id):
    cursor =  mysql.connection.cursor()
    query = "SELECT * FROM ARTICLES WHERE ID = %s"

    result = cursor.execute(query,[id,])

    if result > 0:
        article = cursor.fetchone()

        query = "SELECT * FROM ARTICLES"
        cursor.execute(query)
        articles = cursor.fetchall()

        return render_template("article/details_article.html",article = article,articles = articles)
    else:
        return render_template("article/details_article.html")

@app.route("/articles/search",methods = ["GET","POST"])
def search_article():
    if request.method == "POST":
        keyword = request.form.get("keyword")

        cursor = mysql.connection.cursor()
        query =  "SELECT * FROM ARTICLES WHERE TITLE LIKE '%" + keyword + "%'"

        result = cursor.execute(query)

        if  result > 0:
            articles = cursor.fetchall()

            return render_template("article/articles.html",articles = articles)
        else:
            flash("No article found matching the search term!","danger")
            return redirect(url_for("articles"))
        

@app.route("/addarticle",methods = ["GET","POST"])
@login_required
def add_article():
    form = Article_Form(request.form)

    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data
        imgurl = form.imgurl.data

        cursor = mysql.connection.cursor()
        query = "INSERT INTO ARTICLES(TITLE,AUTHOR,CONTENT,IMGURL) VALUES(%s,%s,%s,%s)"

        cursor.execute(query,[title,session["username"],content,imgurl])
        mysql.connection.commit()

        cursor.close()

        flash("Article successfully added!","success")
        return redirect(url_for("dashboard"))
    else:
        return render_template("article/add_article.html",form = form)

@app.route("/article/edit/<string:id>",methods = ["GET","POST"])
@login_required
def update_article(id):
    if request.method == "POST":
        form = Article_Form(request.form)

        new_title = form.title.data
        new_content = form.content.data
        new_imgurl = form.imgurl.data

        cursor = mysql.connection.cursor()
        query = "UPDATE ARTICLES SET TITLE = %s,CONTENT = %s,IMGURL = %s WHERE ID = %s"

        cursor.execute(query,[new_title,new_content,new_imgurl,id])
        mysql.connection.commit()

        cursor.close()

        flash("The article has been successfully updated!","success")
        return redirect(url_for("dashboard"))
    else:
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM ARTICLES WHERE ID = %s AND AUTHOR = %s"

        result = cursor.execute(query,[id,session["username"]])

        if result > 0:
            article = cursor.fetchone()
            form = Article_Form()

            form.title.data = article["title"]
            form.content.data = article["content"]
            form.imgurl.data = article["imgurl"]

            return render_template("article/update_article.html",form = form)
        else:
            flash("There is no such article or you are not authorized to update this article!","warning")
            return redirect(url_for("index"))

@app.route("/article/delete/<string:id>")
@login_required
def delete_article(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM ARTICLES WHERE ID = %s AND AUTHOR = %s"

    result = cursor.execute(query,[id,session["username"]])

    if result > 0:
        query = "DELETE FROM ARTICLES WHERE ID = %s"

        cursor.execute(query,[id,])
        mysql.connection.commit()
        
        cursor.close()

        flash("The article has been successfully deleted.","success")
        return redirect(url_for("dashboard"))
    else:
        flash("There is no such article or you are not authorized to delete this article!","warning")
        return redirect(url_for("index"))
        cursor.close()

@app.route("/signup",methods = ["GET","POST"])
def signup():
    form = Sign_Up_Form(request.form)
    if request.method == "POST" and form.validate():
        #Database Insert Process
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        query = "INSERT INTO USERS(NAME,USERNAME,EMAIL,PASSWORD) VALUES(%s,%s,%s,%s)"

        cursor.execute(query,[name,username,email,password])
        mysql.connection.commit()

        cursor.close()
        #Database Insert Process End

        flash(" Successfully Registered...","success")

        return redirect(url_for("login"))
    else:
        return render_template("entry/sign_up.html",form = form)

@app.route("/login",methods = ["GET","POST"])
def login():
    form = Login_Form(request.form)

    if request.method == "POST" and form.validate():
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM USERS WHERE USERNAME = %s"
        result = cursor.execute(query,[username,])

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]

            if sha256_crypt.verify(password_entered,real_password):
                flash("You have successfully logged in! Welcome {0}.".format(data["name"]),"success")

                session["logged_in"] = True
                session["username"] = username

                return redirect(url_for("index"))
        else:
            flash("Username or password is incorrect!","danger")
            return redirect(url_for("login"))
    else:
        return render_template("entry/login.html",form = form)

@app.route("/logout")
def logout():
    session.clear()

    flash("Successfully logged out! Bye Bye...","success")

    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM ARTICLES WHERE AUTHOR = %s"

    result = cursor.execute(query,[session["username"],])

    if result > 0:
        articles = cursor.fetchall()
        return render_template("dashboard.html",articles = articles)
    else:
        return render_template("dashboard.html")


# Routes End







if(__name__ == "__main__"):
    app.run(debug=True)