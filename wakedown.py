from wakeonlan import send_magic_packet
from cfg.config import dst_mac
from cfg.config import ssh
from cfg.config import log as log
import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def wakeup():
    send_magic_packet(dst_mac)
    log.info('send magick packet')
    return 'magick packet send'


def shutdown():
    client.connect(hostname=ssh['host'], username=ssh['user'], password=ssh['secret'], port=ssh['port'])

    # Выполнение команды
    client.exec_command('shutdown -h now')
    log.info('shutdown')

    # Читаем результат
    client.close()
    return 'shutdown command send'


def about():
    client.connect(hostname=ssh['host'], username=ssh['user'], password=ssh['secret'], port=ssh['port'])
    stdin, stdout, stderr = client.exec_command('uname -a ;uptime -p')
    data = stdout.read() + stderr.read()
    log.info('get about')
    client.close()

    return data
