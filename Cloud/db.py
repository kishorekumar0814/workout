from sqlite3 import connect
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dnx69836;PWD=KtlyLJbGZ2LGdcfa",'','')
print(connect)
print("Connection Successfull...")