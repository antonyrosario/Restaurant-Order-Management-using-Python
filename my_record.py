"""
Creator Name: Antony Rosario John Peter
Creation Date: 01/11/2022 
"""

import sys

###################################################################################################
# ---------------------------------User-------------------------------------------------------
###################################################################################################


class User:

    def __init__(self, username='', firstname='', lastname='', usertype=''):
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname
        self.__usertype = usertype
        self.__user_usage = {}

    @property
    def username(self):
        return self.__username

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def usertype(self):
        return self.__usertype

    @username.setter
    def username(self, value):
        self.__username = value

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @usertype.setter
    def usertype(self, value):
        self.__usertype = value

    @property
    def user_usage(self):
        return list(self.__user_usage.values())

    @property
    def get_serviceids(self):
        return list(self.__user_usage.keys())

    def set_user_usage(self, **user_usage):
        for k, v in user_usage.items():
            self.__user_usage[k] = v

    def display_info(self):
        print(self.username)


###################################################################################################
# ---------------------------------Services-------------------------------------------------------
###################################################################################################


class Services:

    def __init__(self, service_id='', service_name='', service_type='', service_price=''):
        self.__service_id = service_id
        self.__service_name = service_name
        self.__service_type = service_type
        self.__service_price = service_price

    @property
    def service_id(self):
        return self.__service_id

    @property
    def service_name(self):
        return self.__service_name

    @property
    def service_type(self):
        return self.__service_type

    @property
    def service_price(self):
        return self.__service_price

    @service_id.setter
    def service_id(self, value):
        self.__service_id = value

    @service_name.setter
    def service_name(self, value):
        self.__service_name = value

    @service_type.setter
    def service_type(self, value):
        self.__service_type = value

    @service_price.setter
    def service_price(self, value):
        self.__service_price = value

    def display_info(self):
        print(self.service_id, self.service_name, self.service_type, self.service_price)


###################################################################################################
# ---------------------------------Records-------------------------------------------------------
###################################################################################################

class Records:
    # ------------------------------------------------------------------------------------------
    user_list = []
    user_serv = []
    user_serviceid_list = []
    user_usage_list = []
    usage_sep = []
    user_service_details = []
    unique_serviceids = []
    serviceids_obj = []
    # ------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------
    service_list = []
    price_list = {}
    user_file_list = []

    # ------------------------------------------------------------------------------------------

    def read_records(self, filename):
        records_file = open(filename, 'r')
        line = records_file.readline()
        while line != '':
            line_field = line.strip().split(", ")
            temp1 = []
            usernames = line_field[0]
            userid = User(usernames)
            self.user_list.append(userid)
            temp1.append(line_field[1:])
            temp1 = temp1[0]
            service_ids = temp1[0::2]
            service_values = temp1[1::2]
            self.user_usage_list.append(service_values)
            res = dict(zip(service_ids, service_values))
            tes = dict(zip(service_ids, service_values))
            self.user_service_details.append(tes)
            for i in range(len(self.serviceids_obj)):
                if self.serviceids_obj[i].service_id not in res.keys():
                    res[self.serviceids_obj[i].service_id] = '--'
            userid.set_user_usage(**res)
            line = records_file.readline()
        for sublist in self.user_usage_list:
            self.usage_sep.extend(sublist)
        records_file.close()

    def read_records1(self, filename):
        records1_file = open(filename, 'r')
        line1 = records1_file.readline()
        while line1 != '':
            line_field1 = line1.strip().split(", ")
            temp = []
            temp.append(line_field1[1:])
            temp = temp[0]
            service_ids = temp[0::2]
            self.user_serv.append(service_ids)
            line1 = records1_file.readline()
        for item in self.user_serv:
            self.unique_serviceids = sorted(list(set(self.unique_serviceids) | set(item)))
        for item in self.unique_serviceids:
            services = Services(item)
            self.serviceids_obj.append(services)
        records1_file.close()

    def read_services(self, filename):
        services_file = open(filename, 'r')
        line = services_file.readline()
        while line != '':
            line_field = line.strip().split(", ")
            service_ids = line_field[0]
            service_names = line_field[1]
            service_types = line_field[2]
            s_price = float(line_field[3])
            self.price_list[service_ids] = s_price
            prices = float(line_field[3])
            if service_types == 'Premium':
                pricess = str(prices)
                rate = str(round(prices*0.8,2))
                service_prices = pricess+'/'+rate
                services_obj = Services(service_ids, service_names, service_types, service_prices)
            else:
                service_prices = str(line_field[3])
                services_obj = Services(service_ids, service_names, service_types, service_prices)

            self.service_list.append(services_obj)
            line = services_file.readline()

    def read_users(self,filename):
        user_file = open(filename, 'r')
        line = user_file.readline()
        while line != '':
            line_field = line.strip().split(", ")
            user_names = line_field[0]
            first_names = line_field[1]
            last_names = line_field[2]
            user_type = line_field[3]
            users_obj = User(user_names, first_names, last_names, user_type)
            self.user_file_list.append(users_obj)
            line = user_file.readline()



###################################################################################################
# ---------------------------------Main Class-------------------------------------------------------
###################################################################################################

class Operations:

    def run_Operations(self, record_filename='',service_filename='',user_filename=''):
        records_obj = Records()
        self.recordname=record_filename
        self.servicename=service_filename
        self.username=user_filename


        if len(sys.argv)==2:
            print("Welcome to the RMIT Service Provider Dashboard!\n")
            print("############################################################")
            print("You can choose from the following options: ")
            print("1: Display records")
            print("0: Exit the program")
            print("############################################################")
            records_obj.read_records1(self.recordname)
            records_obj.read_records(self.recordname)

        elif len(sys.argv)==3:
            print("Welcome to the RMIT Service Provider Dashboard!\n")
            print("############################################################")
            print("You can choose from the following options: ")
            print("1: Display records")
            print("2: Display services")
            print("0: Exit the program")
            print("############################################################")
            records_obj.read_services(self.servicename)
            records_obj.read_records1(self.recordname)
            records_obj.read_records(self.recordname)

        elif len(sys.argv)==4:
            print("Welcome to the RMIT Service Provider Dashboard!\n")
            print("############################################################")
            print("You can choose from the following options: ")
            print("1: Display records")
            print("2: Display services")
            print("3: Display users")
            print("0: Exit the program")
            print("############################################################")
            records_obj.read_services(self.servicename)
            records_obj.read_records1(self.recordname)
            records_obj.read_records(self.recordname)
            records_obj.read_users(self.username)

        choose_option = int(input("Choose one option:\n "))
        start = True
        while start:
            if choose_option == 1:
                self.records_display()
            elif choose_option == 2:
                self.services_display()
            elif choose_option == 3:
                self.user_display()
            elif choose_option == 0:
                exit()
            choose_option = int(input("Choose one option:\n "))

    def records_display(self):
        records_obj = Records()
        len1 = len(records_obj.user_list)
        len2 = len(records_obj.serviceids_obj)
        len3 = len(records_obj.usage_sep)
        total = len1 * len2
        value = f"{len3 / total:.2%}"
        print('RECORDS')
        print('-' * 120)
        print('Usernames'.ljust(11), end='\t\t')
        for items in records_obj.serviceids_obj:
            print(items.service_id.rjust(5), end='\t\t')
        print()
        print('-' * 120)
        for userid in records_obj.user_list:
            print(userid.username.ljust(13), end='\t\t')
            for service in records_obj.serviceids_obj:
                for i in range(0, len(userid.get_serviceids)):
                    if service.service_id == userid.get_serviceids[i]:
                        print(userid.user_usage[i].rjust(5), end='\t\t')
            print()

        print('\nRECORDS SUMMARY')
        print('There are', len1, 'users and', len2, 'services.')
        print('The usage percentage is', value)

    def services_display(self):

        records_obj1 = Records

        for item in records_obj1.user_service_details:
            for key in item:
                item[key] = float(item[key])

        Nuser = sum(records_obj1.user_serv,[])
        occurence = {item: Nuser.count(item) for item in Nuser}
        num_user = {}
        for items in records_obj1.service_list:
            for n in Nuser:
                num_user[items.service_id] = occurence.get(items.service_id)

        max_user = max(num_user, key=num_user.get)
        m_exp = max(records_obj1.price_list, key=records_obj1.price_list.get)
        max_user_name = ''
        most_exp = ''
        for items in records_obj1.service_list:
            if max_user == items.service_id:
                max_user_name = items.service_name

        for items in records_obj1.service_list:
            if m_exp == items.service_id:
                most_exp = items.service_name

        print('SERVICE INFORMATION')
        print('-' * 130)
        print('ServiceID'.ljust(10), end='\t\t')
        print('Name'.ljust(10), end='\t\t')
        print('Type'.ljust(10), end='\t\t')
        print('Price'.ljust(10), end='\t\t')
        print('Nuser'.ljust(10), end='\t\t')
        print('Usage'.ljust(10), end='\t\t')
        print()
        print('-' * 130)
        for items in records_obj1.service_list:
            print(items.service_id.ljust(12), end='\t\t')
            print(items.service_name.ljust(15), end='\t\t')
            print(items.service_type.ljust(8), end='\t')
            print(items.service_price.rjust(13), end='\t\t')
            print(str(occurence.get(items.service_id)).rjust(13), end='\t\t')
            n_usage = [d[items.service_id] for d in records_obj1.user_service_details if items.service_id in d]
            usage = round(sum(n_usage),1)
            print(str(usage).rjust(13))
        print()
        print('\nRECORDS SUMMARY')
        print('The most popular service is',max_user,'(',max_user_name,')')
        print('The most expensive service (per unit) is',m_exp,'(',most_exp,')')

    def user_display(self):
        records_obj = Records()
        for item in records_obj.user_service_details:
            for key in item:
                item[key] = float(item[key])

        print('USER INFORMATION')
        print('-' * 130)
        print('Username'.ljust(10), end='\t\t')
        print('First name'.ljust(10), end='\t\t')
        print('Last name'.ljust(10), end='\t\t')
        print('Type'.ljust(10), end='\t\t')
        print('Spent'.ljust(10), end='\t\t')
        print('Nservice'.ljust(10), end='\t\t')
        print()
        print('-' * 130)
        for items in records_obj.user_file_list:
            print(items.username.ljust(12), end='\t\t')
            print(items.firstname.ljust(15), end='\t\t')
            print(items.lastname.ljust(15), end='\t\t')
            print(items.usertype.ljust(10))
        print()
        print('\nUSER SUMMARY')
        print('The most valuable user is .')
        print('The user used the most service is')


for i in range(len(sys.argv)):
    if len(sys.argv) <= 1:
        print('[Usage:] python', sys.argv[i], '<records file>')
    elif len(sys.argv) == 2:
        operations_obj = Operations()
        operations_obj.run_Operations(sys.argv[1])
    elif len(sys.argv) == 3:
        operations_obj = Operations()
        operations_obj.run_Operations(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 4:
        operations_obj = Operations()
        operations_obj.run_Operations(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        exit()


