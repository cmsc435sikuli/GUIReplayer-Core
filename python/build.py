
import os, sys, subprocess

def main(argv):
    # Find destination directory based on current file location
    destdir = os.path.abspath(os.path.join(__file__, '..', '..', '..'))

    modules = [x for x in argv if x.strip()]
    for module in reduce(lambda x, y: x + y.split(','), modules, []):
        print 'building module %s' % module
        antfile = os.path.join(destdir, module, 'install', 'build.xml')
        if subprocess.call(['ant', '-f', antfile, 'dist']) != 0:
            raise Exception('Build Failed for module %s' % module)

if __name__ == '__main__':
    main(sys.argv[1:])
