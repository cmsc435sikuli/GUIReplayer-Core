
import os, sys
from mercurial import commands, ui, hg

def main(argv):
    # Find destination directory based on current file location
    destdir = os.path.abspath(os.path.join(__file__, '..', '..', '..'))

    # Read the configuration file for the shared repository to get the pull path
    repo = hg.repository(ui.ui(), os.path.join(destdir, 'shared'))
    path = repo.ui.config('paths', 'default',
                          'http://localhost/hg/guitar/hgweb.cgi/')[:-len('shared')]
    print 'using %s as remote repository path' % path[:-1]

    for module in argv:
        if not os.path.exists(os.path.join(destdir, module)):
            # Attempt to clone the repository to the destination
            url = '%s%s' % (path, module)
            print 'checking out %s to %s' % (url, destdir)
            commands.clone(ui.ui(), url, os.path.join(destdir, module))
        else:
            # Repository already exists, skip
            print '%s already exists (skipping)' % module

if __name__ == '__main__':
    main(sys.argv[1:])
