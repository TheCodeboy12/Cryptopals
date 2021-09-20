from Crypto.Cipher import AES
from challenge1 import PKCS
import random
class Directory():
    class User:
        def __init__(self,uid,password):
            self.id=uid
            self.password=password
            self.role=None
        def Superadmin(self):
            self.role='Admin'
            print('You are now an Admin')
    
    def __init__(self,name:str,key:bytes,admin):
        assert len(key)%16==0,'Key is not the right len'
        self.name=name
        self.cipher=AES.new(key,AES.MODE_ECB)
        self.admin=Directory.User(admin, 'Passi')
        self.db={
            'users':[],
            'uids':[],
            'passwords':[],
            'roles':[]
        }
        return None
    def __dict__(self):
        print('noting')
    def encode(self,uid):

        return f"email={self.db['users'][uid]}@{self.name}.com&uid={self.db['uids'][uid]}&role={self.db['roles'][uid]}"
    
    def check_before_adding_to_db(self,user_id):
        if user_id in self.db['users']:
            return False
        else:
            return True
    
    def encrypt(self,param):
        return self.cipher.encrypt(PKCS(bytes(param,'ascii'),16))
    
    def decrypt(self,param,user):
        assert user.role=='PASSWORD','NOT ADMIN'
        return self.cipher.decrypt(param)
        

    def add_user(self,username,password,role):
        assert username.isalnum() and password.isalnum() and role.isalnum(),'You are not allowed to use special charecters!'
        if self.check_before_adding_to_db(username)==True:
            self.db['users'].append(self.encrypt(username))
            self.db['passwords'].append(self.encrypt(password))
            self.db['roles'].append(self.encrypt(role))
            self.db['uids'].append(self.db['users'].index(self.encrypt(username)))
        elif self.check_before_adding_to_db(username)==False:
            print('User already exists!')


sf=Directory('sf415',b'"provide"'+ b' that to the '+ b'"attacker"','admin')
sf.add_user('gabe', 'password', 'LOLITO')

d=sf.User('gabe', 'gggggggg')
d.Superadmin()
