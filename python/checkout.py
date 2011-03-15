
import os, sys
from mercurial import commands, ui, hg
from subprocess import call

def main(argv):
    # Find destination directory based on current file location
    destdir = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', '..'))

    # Read the configuration file for the shared repository to get the pull path
    repo = hg.repository(
        ui.ui(), os.path.join(os.path.dirname(__file__), '..'))
    sharedpath = repo.ui.config('paths', 'default', None)
    if sharedpath is None:
        raise Exception('no default path in the shared directory!')

    unstable = sharedpath.endswith('-unstable')
    path = os.path.dirname(sharedpath)
    print 'using %s as remote repository path' % path

    for module in reduce(lambda x, y: x + y.split(','), argv, []):
        if module.endswith('-unstable'):
            module = module[:-len('-unstable')]

        if not os.path.exists(os.path.join(destdir, module)):
            # Attempt to clone the repository to the destination
            if module == "GUIRipper-Plugin-JFC" or module == "GUIRipper-Core" or module == "GUITARModel-Plugin-JFC" or module == "GUITARModel-Core" or module == "GUIReplayer-Plugin-JFC" or module == "GUIReplayer-Core":
				call("git clone git://github.com/cmsc435sikuli/" + module + ".git " + destdir + "/" +  module, shell=True)
            else:
                url = '%s/%s%s' % (path, module, '-unstable' if unstable else '')
                print 'checking out %s to %s' % (url, destdir)
                commands.clone(ui.ui(), url, os.path.join(destdir, module))
        else:
            # Repository already exists, skip
            print '%s already exists (skipping)' % module

if __name__ == '__main__':
    main(sys.argv[1:])
