#!/bin/python
import subprocess, shlex

for rev in range(6685, 10830):
        eargs = "/cygdrive/c/Progra~2/Subversion/bin/svnadmin verify -r %d c:/SvnRepo" % rev
        e_args = shlex.split(eargs)
        print e_args
        p = subprocess.Popen(e_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        print "out %s" % out
        print err
        if ("Verified revision %d." % rev) not in err:
                print ("FUCKED %d C:\SvnRepo" % rev)
                f = open('corrupt_revisions.txt', 'a')
                f.write("%d\n" % rev)
                f.close()
        else:
                f = open('good_revisions.txt', 'a')
                f.write("%d\n" % rev)
                f.close()



