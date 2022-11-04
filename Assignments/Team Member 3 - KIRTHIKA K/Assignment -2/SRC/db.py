import ibm_db_dbi
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
  conn = ibm_db_dbi.pconnect(dsn,"","")
  print("Connected")
except:
  print(ibm_db_dbi.conn_errormsg())