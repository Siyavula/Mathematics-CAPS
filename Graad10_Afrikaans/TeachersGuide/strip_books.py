#!/usr/bin/env python

import sys, os





def make_solutions(number):
    items = ''.join(['\\item solution %s\n'%(i+1) for i in range(number)])
    solution = '''\n\n \\begin{solutions}{}{
\\begin{enumerate}[itemsep=5pt, label=\\textbf{\\arabic*}. ] 


%s
\\end{enumerate}}
\\end{solutions}\n\n
'''%(items)
    return solution

def strip_file(lines):
    inside_ex = False
    no_enumi = 0 
    no_of_questions = 0
    stripped = []

    for line in lines:
        if (len(line.strip()) > 0):
            if (line.strip()[0] != '%'):
                
                if ('\\begin{exercises}' in line) or ('\\begin{eocexercises}' in line):
                    no_of_questions = 0
                    no_enumi = 0
                    inside_ex = True


                if any([r in line for r in ['\\section{', '\\subsection{', '\\chapter{']]):
                    stripped.append(line)

                if inside_ex:
                    stripped.append(line)

                # count solutions
                    if '{enumerate}' in line:
                        no_enumi += 1

                    if '\\item' in line:
                        if no_enumi % 2 > 0:
                            no_of_questions += 1
                
                    if ('\\end{exercises}' in line) or ('\\end{eocexercises}' in line):
                        inside_ex = False
                        stripped.append(make_solutions(no_of_questions))
    
    
    return stripped




if __name__ == "__main__":
    #mathsfiles = [f.strip() for f in os.listdir(os.curdir) if 'Gr10-' == f[0:5]]
    #for f in mathsfiles:
        #outfile = open('Temp_' + f, 'w')
        #print f
        #text = open(f, 'r').readlines()
        # strip out everything that is not an exercise or eocexercise
        #stripped = strip_file(text)
        #outfile.write(''.join(stripped))
        #outfile.close()
    print '\n\nDo not run this if you do not know what you are doing\n\n'

