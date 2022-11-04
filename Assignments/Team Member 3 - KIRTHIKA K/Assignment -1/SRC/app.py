from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db

app = Flask(__name__)

dsn_hostname = "8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "mvg77822"
dsn_pwd = "XOk7hJ5iGB6Dzgtx"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_port = "30120"
dsn_security = "SSL"
dsn = ("DRIVER={0};"
"DATABASE={1};"
"HOSTNAME={2};"
"PORT={3};"
"UID={4};"
"PWD={5};"
"SECURITY={6};").format(dsn_driver,dsn_database,dsn_hostname,dsn_port,dsn_uid,dsn_pwd,dsn_security)
print(dsn)
try:
  conn = ibm_db.pconnect(dsn,"","")
  print("success")
except:
  print(ibm_db.conn_errormsg())

@app.route("/" , methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    sql_stmt = "insert into USERTBL values(?,?,?)"
    stmt = ibm_db.prepare(conn, sql_stmt)
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    ibm_db.bind_param(stmt, 1, username)
    ibm_db.bind_param(stmt, 2, email)
    ibm_db.bind_param(stmt, 3, password)
    try:
      ibm_db.execute(stmt)
      return redirect('/')
    except:
      print(ibm_db.stmt_errormsg())

  return render_template('index.html')


@app.route("/login",methods=('GET','POST'))
def loginpage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = "select COUNT(*) from usertbl where username='"+username+"' and password='"+password+"'"
        stmt5 = ibm_db.exec_immediate(conn,query)
        row = ibm_db.fetch_tuple(stmt5)
        if(row[0] ==1 ):
            return redirect("/shop/")
    return render_template("index.html")


@app.route("/shop/" , methods=['GET', 'POST'])
def shop():
  sql = "SELECT * FROM PROTBL"
  pro_name = []
  pro_price = []
  pro_image = []
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_assoc(stmt)
  while dictionary != False:
    pro_name.append(f'{dictionary["PRO_NAME"]}')
    pro_price.append(f'{dictionary["PRO_PRICE"]}')
    pro_image.append(f'{dictionary["PRO_IMAGE"]}')
    dictionary = ibm_db.fetch_assoc(stmt)
  return render_template('shop.html', len = len(pro_name), pro_name = pro_name, pro_image = pro_image, pro_price = pro_price)


if __name__ == "__main__":
    app.run(debug=True)