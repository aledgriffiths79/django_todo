import os

os.environ['DEVELOPMENT'] = '1'

os.environ['DATABASE_URL'] = 'postgres://yzlbkestanmzum:9b3e50d78ef70e96920fdd1b05958ed660da5ef813bc93d68f4aa432564860aa@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/denh0pjjkblsd0'

# development secret key here and production secret key is in heroku config vars

os.environ['SECRET_KEY'] = 'g*no1_0zz^0r0x9x1*mw$u4@tydw@sd%b**42h)=l*g!)9ixs'