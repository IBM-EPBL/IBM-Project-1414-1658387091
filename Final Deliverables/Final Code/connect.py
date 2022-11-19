import ibm_db
#conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=lzl34218;PWD=3XYDnCQAbEBZIDLb",'','')
dsn_hostname = "19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
dsn_uid = "lzl34218"
dsn_pwd = "3XYDnCQAbEBZIDLb"
dsn_driver = "{IBMDB2CL1}"
dsn_database = "bludb"            # e.g. "BLUDB"
dsn_port = "30699"                
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              #i.e. "SSL
dsn_cert="DigiCertGlobalRootCA.crt"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
    "SSLServerCertificate={8};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security,dsn_cert)
print(dsn)
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print("Unable to connect: ", ibm_db.conn_errormsg())
# sql = "insert into user values('105','sahana@gmail.com','1234','sahanaparveen')"
# ibm_db.exec_immediate(conn, sql)
