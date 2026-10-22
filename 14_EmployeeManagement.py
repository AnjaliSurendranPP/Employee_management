from mysql import connector
from datetime import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection =connector.connect(
                host="localhost",
                user="root",
                password="Anjali94!",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None

class EmployeeManager(DbConnect):
    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into employee(name,place,mobile,email,department,salary,joining_date) values(%s,%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print( "Employee Added Successfully.")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            self.cursor.execute("select * from employee")
            datas=self.cursor.fetchall()
            for data in datas:
                print(data)
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            # print(record)
            return record
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id)
            if record!=None:
                self.cursor=self.connect.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s, "
                placeholder=placeholder.rstrip(", ")
                query=f"update employee set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("employee updated successfully")
            else:
                print("employee not found")

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            if record != None:
                query = "delete from employee where id=%s"
                values = (id,)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("employee deleted successfully")
            else:
                print("employee not found")
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            record = self.get_object(id=id)
            if record == None:
                print("employee not found")
            print(record)
        except Exception as e:
            print(e)

connection_instance=DbConnect()
employee_instance=EmployeeManager()
# employee_instance.post(name="Anjali",place="Kannur",mobile="8547403112",email="anjali@gmail.com",department="Developer",salary=50000,joining_date=datetime.today())
# employee_instance.post(name="Anju",place="Payyannur",mobile="9495900638",email="anju@gmail.com",department="Developer",salary=30000,joining_date=datetime.today())
employee_instance.get()
employee_instance.put(1,salary=60000)
employee_instance.retrieve(1)
employee_instance.delete(3)