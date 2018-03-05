# _*coding:utf-8 _*_

from set_logbook import setup_logger


from logbook import Logger

conf = {
    "LOGBOOK_CONSOLE": True,
    "LOGBOOK_CONSOLE_LEVEL": 'DEBUG',   #'DEBUG','INFO','NOTICE','WARNING','ERROR','CRITICAL'
    "LOGBOOK_FILE": True,
    "LOGBOOK_FILE_LEVEL": 'NOTICE',  #'DEBUG','INFO','NOTICE','WARNING','ERROR','CRITICAL'
    "LOGBOOK_LOG_FILE": 'logs/log.log',
    "LOGBOOK_BACKUP_COUNT": 5,
    "LOGBOOK_MAX_SIZE": 1024,
    "LOGBOOK_FORMAT_STRING":'({record.time:%Y-%m-%d %H:%M:%S}),{record.level_name},[{record.thread_name}],{record.channel}[{record.lineno}]: {record.message}'
    #simple version: format_string = '({record.time:%m-%d %H:%M:%S}){record.level_name},channel:{record.channel},line_{record.lineno}: {record.message}'
}

setup_logger(conf)

log = Logger("USE_LOGBOOK")

def print_log():
    log.debug("log.debug")
    log.info("log.info")
    log.notice("log.notice")
    log.warning("log.warning")
    log.error("log.error")
    log.critical("log.critical")
    

if __name__ == "__main__":
    print_log()
