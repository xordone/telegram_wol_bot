import cfg.cred as cred
import logging

time_format = '%Y-%m-%d %H:%M'
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO, datefmt=time_format)
log = logging.getLogger('My_Logger')
token = cred.telegram_token
authorized_users = cred.auth_list
dst_mac = 'b4:2e:99:bc:c5:d6'
ssh = cred.ssh
