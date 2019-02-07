# instance/config.py

# an secret key is needed
SECRET_KEY = 'p9Bv<3Eid9%$i01'

# ADD MYSQL DATABASE LINK HERE
SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@localhost/dreamteam_db'


'''
for root, dirs, files in os.walk("/mnt/Work/EmployeeManagement/"):  
    for filename in files:
        if filename.endswith(".pyc"):
        	ddir = root + "/" + filename
        	print(root, filename)
        	os.remove(ddir)


'''