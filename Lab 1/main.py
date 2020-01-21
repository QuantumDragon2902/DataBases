from peewee import (SqliteDatabase, Model,CharField, BooleanField, IntegerField, FloatField, InternalError)
db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Client(BaseModel):
    surname = CharField()
    name = CharField()
    sex = CharField()
    age = IntegerField()
    status = CharField()


class Credit(BaseModel):
    summ = IntegerField()
    period = IntegerField()
    percent = IntegerField()
    credit_type = CharField()


db.create_tables([Client, Credit])

exit_value = True
while exit_value:
    print('       Menu\n'
          '1 - Our clients\n'
          '2 -   Credits\n'
          '3 -     Exit')
    command = int(input())

    if command == 1:
        print('     *Our clints*\n'
              '1 - Show all our clients\n'
              '2 -     Add client\n'
              '3 -  Change information\n'
              '4 -   Delete client\n'
              '5 -   Exit to main page')
        command = int(input())

        if command == 1:
            print('Show all our clients')
            for client_ in Client.select():
                print(client_.surname,
                      client_.name,
                      client_.age,
                      client_.sex,
                      client_.status)

        elif command == 2:
            print('Add information')
            add_surname = input('Surname - ')
            add_name = input('Name - ')
            add_age = int(input('Age - '))
            add_sex = input('Sex - ')
            add_status = input('Status - ')
            add_client = Client(surname=add_surname,
                                    name=add_name,
                                    age=add_age,
                                    sex=add_sex,
                                    status=add_status)
            add_client.save()
            db.commit()
            print('Information has been added')

        elif command == 3:
            print('Input name and surname of client')
            change_surname = input('Surname - ')
            change_name = input('Name - ')
            change_client = Client.get(
                Client.surname == change_surname and
                Client.name == change_name)
            print('Input information')
            change_client.surname = input('Surname - ')
            change_client.name = input('Name - ')
            change_client.age = int(input('Age - '))
            change_client.sex = input('Sex- ')
            change_client.status = input('Status - ')
            change_client.save()
            db.commit()
            print('Information has been changed')

        elif command == 4:
            print('Input name and surname of client')
            delete_surname = input('Surname - ')
            delete_name = input('Name - ')
            delete_client = Client.get(
                Client.surname == delete_surname and
                Client.name == delete_name)
            delete_client.delete_instance()
            db.commit()
            print('Information has been deleted')

        elif command == 5:
            exit_value = True

    elif command == 2:
        print('     *Credits*\n'
              '1 - Show all credits\n'
              '2 -    Add credit\n'
              '3 - Exit to main page')
        command = int(input())

        if command == 1:
            print('Credits')
            for credits_ in Credit.select():
                print(credits_.summ,
                      credits_.period,
                      credits_.percent,
                      credits_.credit_type)

        elif command == 2:
            print('Input new credit')
            add_summ = int(input('Summ - '))
            add_period = int(input('Period - '))
            add_percent = int(input('Percent - '))
            add_type = input('Type - ')
            add_credit = Credit(summ=add_summ,
                                          period=add_period,
                                          percent=add_percent,
                                          credit_type=add_type)
            add_credit.save()
            db.commit()
            print('Information has been added')

        elif coomand == 3:
            exit_value = True

    elif command == 3:
        exit_value = False

db.close()