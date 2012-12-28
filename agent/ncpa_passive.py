#!/usr/bin/env python
import daemons
import platform
import optparse
import passive.handlers

def parse_args():
    
    usage = '%prog [start|stop|reload]'
    
    parser = optparse.OptionParser()
    
    parser.add_option('-c', '--config', help='Config file to use.', default='etc/ncpa.cfg')
    
    options, args = parser.parse_args()
    
    if not len(args) == 1 or args[0] not in ['start', 'stop', 'reload']:
        parser.error('Must only give either start, stop or reload.')
    
    return options, args

if __name__ == "__main__":
    
    options, args = parse_args()
    
    if not platform.system() == 'Windows':
        daemon = daemons.posix.PassiveDaemon(config_filename=options.config)
    else:
        daemon = daemons.windows.PassiveDaemon(config_filename=options.config)
    
    gen_daemon = getattr(daemon, args[0])
    gen_daemon()
