import sys
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
import os.path
#['htdocs', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-linux2', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PIL', '/usr/lib/pymodules/python2.7']
#import cgi
#print sys.path
sys.path.append("/data/web/78/9c/80/kansaslinuxfest.tuxfamily.org/php-include/zookeepr_git/")
sys.path.append("/data/web/78/9c/80/kansaslinuxfest.tuxfamily.org/php-include/install/lib/python2.7/site-packages/")


def test1():
    import pyramid
    from paste.deploy import appconfig

def test():

    config_file = '/path_to_config_file/configname.ini'

    name = 'app_name'
    config_name = 'config:%s' % config_file
    here_dir = os.getcwd()

    conf = appconfig(config_name, name, relative_to=here_dir)

    from main_package import main
    app = main(conf.global_conf, **conf.local_conf)

try :
    test1()
except Exception as e:
    print e
