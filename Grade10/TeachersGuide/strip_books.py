#!/usr/bin/env python

import sys, os





def make_solutions(number):
    solution = '''\n\n \\begin{solutions}
\\begin{enumerate}[itemsep=5pt, label=\\textbf{(\\alph*)}]

\LARGE Enter solutions here!!!!!

\\end{enumerate}
\\end{solutions}\n\n
'''
    return solution

def strip_file(lines):
    inside_ex = False
    inside_first_enumerate = False 
    no_of_questions = 0
    stripped = []

    for line in lines:
        if (len(line.strip()) > 0):
            if (line.strip()[0] != '%'):
                
                # count solutions
                if inside_ex:
                    if ('\\begin{enumerate}' in line) and (inside_first_enumerate == False):
                        inside_first_enumerate = True
                    
                    if ('\\begin{enumerate}' in line) and (inside_first_enumerate == True):
                        inside_first_enumerate = False

                    if ('\\end{enumerate}' in line) and (inside_first_enumerate == True):
                        pass

                    if ('\\end{enumerate}' in line) and (inside_first_enumerate == False):
                        inside_first_enumerate = True

                    
                if inside_first_enumerate:
                    if '\\item' in line:
                        no_of_questions += 1 

                if '\\begin{exercises}' in line:
                    inside_ex = True

                if '\\end{exercises}' in line:
                    stripped.append(line)
                    inside_ex = False
                    stripped.append(make_solutions(no_of_questions))
                    no_of_questions = 0

                if any([r in line for r in ['\\section{', '\\subsection{', '\\chapter{']]):
                    stripped.append(line)

                if inside_ex:
                    stripped.append(line)

    return stripped




if __name__ == "__main__":
    mathsfiles = [f.strip() for f in os.listdir(os.curdir) if 'Gr10-' == f[0:5]]
    for f in mathsfiles:
        outfile = open('TG_' + f, 'w')
        print f
        text = open(f, 'r').readlines()
        # strip out everything that is not an exercise or eocexercise
        stripped = strip_file(text)
        outfile.write(''.join(stripped))
        outfile.close()


