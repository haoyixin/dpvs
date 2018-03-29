#!/usr/bin/python

import re
import sys
import os

deps_dir = sys.argv[1]

h_src_pat = re.compile(r'(?<=[^.])/[^.][^ ]+\.h')
h_grp_pat = re.compile(r'(include)(?P<dir>.*)(?P<file>/[A-z_0-9-]+\.h)$')
h_ex_pat = re.compile(r'.*dpvs.*')
h_val_pat = re.compile(r'^/.*include.*')

cnt_not_val = cnt_ex = cnt_ok = cnt_fail = 0

for h_line in set(h_src_pat.findall("\n".join(sys.stdin.readlines()))):
    if h_ex_pat.match(h_line):
        cnt_ex += 1
        #print "[INFO] (excluded)", h_line
        continue
    elif not h_val_pat.match(h_line):
        cnt_not_val += 1
        print "[INFO] (invalid)", h_line
        continue
    else:
        sg = h_grp_pat.search(h_line)
        if sg == None:
            cnt_fail += 1
            print "[ERROR] (parsing failed)", h_line
        d = deps_dir + sg.group("dir")
        f = d + sg.group("file")
        if not os.path.exists(d):
            os.makedirs(d)
        with open(h_line, 'r') as f_src:
            with open(f, 'w') as f_dst:
                for l in f_src:
                    f_dst.write(l)
        cnt_ok += 1
        #print "[OK]", h_line, "->", f

print "OK:", cnt_ok, " ERROR:", cnt_fail, " NO_VAL:", cnt_not_val, " EX:", cnt_ex
