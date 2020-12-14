import unittest, os, sys,sqlite3,time
from code import create_db, add_user, add_room, get_users, get_rooms,delete_user,delete_room


conn = sqlite3.connect('quick_chat.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

db_path = 'quick_chat.db'

class TestDB(unittest.TestCase):
	def test_1_init(self):
		c.execute('DROP TABLE IF EXISTS Rooms;')
		c.execute('DROP TABLE IF EXISTS Users;')
		#os.remove(db_path)
		create_db(db_path)
		sql = "select * from Users;"
		table_name = ''
		for row in c.execute(sql).fetchall():
			table_name = row[0]
		self.assertEqual(table_name,'')

		sql = "select * from Rooms;"
		table_name = ''
		for row in c.execute(sql).fetchall():
			table_name = row[0]
		self.assertEqual(table_name,'')
 
	def test_2_add_user(self):
		add_user(db_path,'yann.c',0,0,'password')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')

		add_user(db_path,'yann.c',0,0,'password0')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')

		add_user(db_path,'yann.c',0,0,'password.')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')


		add_user(db_path,'yann.c',0,0,'password0.')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'yann.c')

	def test_3_get_users(self):
		self.assertEqual(get_users(db_path),['yann.c'])

	def test_4_delete_user(self):
		delete_user(db_path,'yann.c')
		sql = "select user_name from Users where user_name = 'yann.c';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
	

	def test_5_add_room(self):


		add_room(db_path,'room1','public')
		sql = "select room_name from Rooms where room_name = 'room1';"
		for row in c.execute(sql):
			room_name = row[0]
		self.assertEqual(room_name,'room1')

		add_room(db_path,'room0','unknown')
		sql = "select room_name from Rooms where room_name = 'room0';"
		res = ''
		for row in c.execute(sql):
			res = row[0]
		self.assertEqual(res,'')



	def test_6_get_rooms(self):
		self.assertEqual(get_rooms(db_path),['room1'])

	def test_7_delete_room(self):
		delete_room(db_path,'room1')
		sql = "select room_name from Rooms where room_name = 'room1';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
	




if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()

# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))
