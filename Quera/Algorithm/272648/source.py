# Name: شبیه‌ساز خودپرداز
# URL: https://quera.org/problemset/272648

from datetime import datetime

def validateCommand(command, *args):
    if command == 'register':
        user = args[0]
        password = args[1]
        role = args[2]
        timestamp = args[3]
        user = Bank(user, password, role, timestamp)
        print(f'[INFO] user registered successfully')
    
    elif command == 'login':
        user = args[0]
        password = args[1]
        timestamp = args[2]
        user = Bank.get(user, password, timestamp)
        print(f'[INFO] user logged in successfully')
    
    elif command == 'logout':
        session_id = int(args[0])
        timestamp = args[1]
        logout = Bank.logout(session_id, timestamp)
        print(f'[INFO] user logged out')
    
    elif command == 'withdraw':
        session_id = int(args[0])
        amount = int(args[1])        
        timestamp = args[2]
        withdraw = Bank.withdraw(session_id, amount, timestamp)
        print(f'[INFO] amount withdrawn successfully')
    
    elif command == 'deposit':
        session_id = int(args[0])
        amount = int(args[1])        
        timestamp = args[2]
        deposit  = Bank.deposit(session_id, amount, timestamp)
        print(f'[INFO] amount deposited successfully')
    
    elif command == 'transfer':
        session_id = int(args[0])
        target_user = args[1]
        amount = int(args[2])
        timestamp = args[3]
        transfer = Bank.transfer(session_id, target_user, amount, timestamp)
        print(f'[INFO] amount transferred successfully') 
    
    elif command == 'log':
        if len(args) == 2:
            level:str = args[0]
            t1 = None
            t2 = None
            timestamp = args[1]
            Bank.logs['DEBUG'][timestamp] = f'get log {level} {timestamp}'
            logs = Bank.logs[level.upper()].values()
            if len(logs) == 0:
                print(f'no logs found')
            else:
                for message in logs:
                    print(f'{timestamp} {level.upper()} {message}')
            print(f'[DEBUG] get log {level}')

        else:
            level:str = args[0]
            t1 = args[1]
            t2 = args[2]
            timestamp = args[3]
            Bank.logs['DEBUG'][timestamp] = f'get log {level} {t1} {t2} {timestamp}'
            t1_time = datetime.strptime(t1, format)
            t2_time = datetime.strptime(t2, format)
            for key, value in Bank.logs[level.upper()].items():
                key_time = datetime.strptime(key, format)
                if not (t1_time <= key_time <= t2_time):
                    continue
                print(f'{key} {level.upper()} {value}')
            print(f'[DEBUG] get log {level} {t1} {t2}')

                


class InvalidUserName(BaseException):
    def __str__(self):
        return '[ERROR] user already registered'

class InvalidCredentials(BaseException):
    def __str__(self):
        return '[ERROR] invalid credentials'

class AlreadyLoggedIn(BaseException):
    def __str__(self):
        return '[INFO] already logged in'

class SessionError(BaseException):
    def __str__(self):
        return f'[ERROR] session expired or invalid'

class SessionExpired(BaseException):
    def __str__(self):
        return f'[ERROR] session expired'
   
class InsufficientFunds(BaseException):
    def __str__(self):
        return f'[ERROR] insufficient funds'

class NotFoundUser(BaseException):
    def __str__(self):
        return f'[ERROR] target user not found'
        
class Bank():
    users = {}
    logs = {'ERROR':{}, 'INFO':{}, 'DEBUG':{}}
    session_ID = 1
    
    def __init__(self, user, password, role, timestamp):
        Bank.validate(user, timestamp)
        self.user = user
        self.password = password
        self.role = role
        self.timestamp = timestamp
        Bank.logs['INFO'][timestamp] = 'user registered successfully'
        Bank.users[self.user] = {'amount':0      , 'password': self.password,
                                 'role':self.role, 'timestamp':self.timestamp,
                                'login': {'status':False, 'session_ID':0, 'timestamp':'1970/01/01:00:00:00'}}
    
    @staticmethod
    def validate(user, timestamp):
        if user in Bank.users:
            Bank.logs['ERROR'][timestamp] = 'user already registered' 
            raise InvalidUserName
    
    @classmethod
    def get(cls , user, password, timestamp):
        if user not in cls.users:
            cls.logs['ERROR'][timestamp] = 'invalid credentials'
            raise InvalidCredentials
        selected_user = cls.users[user]
        if password != selected_user['password']:
            cls.logs['ERROR'][timestamp] = 'invalid credentials'
            raise InvalidCredentials
        if selected_user['login']['status'] == True:
            cls.logs['INFO'][timestamp] = 'already logged in'
            datetime1 = datetime.strptime(selected_user['login']['timestamp'], format)
            datetime2 = datetime.strptime(timestamp, format)
            time_difference = datetime2 - datetime1
            difference_in_minutes = time_difference.total_seconds() / 60
            if difference_in_minutes > 10:
                selected_user['login']['session_ID'] = cls.session_ID
                cls.session_ID += 1
            raise AlreadyLoggedIn
        
        selected_user['login']['status'] = True
        selected_user['login']['session_ID'] = cls.session_ID
        cls.session_ID += 1
        selected_user['login']['timestamp'] = timestamp
        cls.logs['INFO'][timestamp] = 'user logged in successfully'
        return selected_user
    
    @classmethod
    def logout(cls, session_id, timestamp):
        user = None
        for value in cls.users.values():
            if session_id == value['login']['session_ID']:
                user = value
        if user == None:
            cls.logs['ERROR'][timestamp] = 'session expired or invalid'
            raise SessionError
        user['login']['status'] = False
        user['login']['session_ID'] = 0
        user['login']['timestamp'] = '1970/01/01:00:00:00'
        cls.logs['INFO'][timestamp] = 'user logged out'
    
    @classmethod
    def withdraw(cls, session_id, amount, timestamp):
        for value in cls.users.values():
            if session_id == value['login']['session_ID']:
                user = value
                break
        datetime1 = datetime.strptime(user['login']['timestamp'], format)
        datetime2 = datetime.strptime(timestamp, format)
        time_difference = datetime2 - datetime1
        difference_in_minutes = time_difference.total_seconds() / 60
        if difference_in_minutes > 10:
            cls.logs['ERROR'][timestamp] = 'session expired'
            raise SessionExpired
        if user['amount'] < amount:
            cls.logs['ERROR'][timestamp] = 'insufficient funds'
            raise InsufficientFunds
        
        user['amount'] -= amount
        cls.logs['INFO'][timestamp] = 'amount withdrawn successfully'
    
    @classmethod
    def deposit(cls, session_id, amount, timestamp):
        for value in cls.users.values():
            if session_id == value['login']['session_ID']:
                user = value
                break
        datetime1 = datetime.strptime(user['login']['timestamp'], format)
        datetime2 = datetime.strptime(timestamp, format)
        time_difference = datetime2 - datetime1
        difference_in_minutes = time_difference.total_seconds() / 60
        if difference_in_minutes > 10:
            cls.logs['ERROR'][timestamp] = 'session expired'
            raise SessionExpired
        
        user['amount'] += amount
        cls.logs['INFO'][timestamp] = 'amount deposited successfully'
    
    @classmethod
    def transfer(cls, session_id, target_user, amount, timestamp):
        for value in cls.users.values():
            if session_id == value['login']['session_ID']:
                user = value
                break
        datetime1 = datetime.strptime(user['login']['timestamp'], format)
        datetime2 = datetime.strptime(timestamp, format)
        time_difference = datetime2 - datetime1
        difference_in_minutes = time_difference.total_seconds() / 60
        if difference_in_minutes > 10:
            cls.logs['ERROR'][timestamp] = 'session expired'
            raise SessionExpired
        
        if target_user not in cls.users:
            cls.logs['ERROR'][timestamp] = 'target user not found'
            raise NotFoundUser
        
        if user['amount'] < amount:
            cls.logs['ERROR'][timestamp] = 'insufficient funds'
            raise InsufficientFunds
        
        user['amount'] -= amount
        cls.users[target_user]['amount'] += amount
        cls.logs['INFO'][timestamp] = 'amount transferred successfully'
            

        


n = int(input())
format = "%Y/%m/%d:%H:%M:%S"
for _ in range(n):
    try:
        command, *data = input().split()
        validateCommand(command, *data)
    except BaseException as e:
        print(e)

