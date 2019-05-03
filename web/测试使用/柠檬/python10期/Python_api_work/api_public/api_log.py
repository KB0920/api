import logging
from Python_api_work.api_public import api_path
#日志类
class Logger:
    def logger(self,level,msg):
        logger=logging.getLogger('测试使用')#设置一个日志收集器
        logger.setLevel('DEBUG')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        #输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        #输出到文件
        sh=logging.FileHandler(api_path.log_path,encoding='utf-8')
        sh.setLevel('DEBUG')
        sh.setFormatter(formatter)
        #建立连接
        logger.addHandler(ch)
        logger.addHandler(sh)

        if level=='DEBUG':
            logger.debug(msg)

        if level == 'INFO':
            logger.info(msg)

        if level == 'WARNING':
            logger.warning(msg)

        if level == 'ERROR':
            logger.error(msg)

        if level == 'CRITICAL':
            logger.critical(msg)

            # 每次使用之后要移除掉
        logger.removeHandler(ch)
        logger.removeHandler(sh)

    def debug(self, msg):
        self.logger('DEBUG', msg)

    def info(self, msg):
        self.logger('INFO', msg)

    def warning(self, msg):
        self.logger('WARNING', msg)

    def error(self, msg):
        self.logger('ERROR', msg)

    def critical(self, msg):
        self.logger('CRITICAL', msg)
