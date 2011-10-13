from __future__ import division
from scipy import *
import pylab

outcomes = array([1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])
trials = arange(1, len(outcomes)+1)

print r"\begin{tabular}"
cols = 4
rows = len(trials)//cols
for i in range(rows):
    print ' & '.join(['%2i & '%(trials[i+col*rows]) + ['T','H'][outcomes[i+col*rows]] + ' & %i'%cumsum(outcomes)[i+col*rows] + ' & %.2f'%(cumsum(outcomes)[i+col*rows]/trials[i+col*rows]) for col in range(cols)]) + r'\\'
print r"\end{tabular}"

pylab.plot(trials, cumsum(outcomes)/trials, 'o-')
pylab.plot([0, len(trials)+1], [0.5,0.5], 'k--')
pylab.axis([0, len(trials)+1, -0.05, 1.05])
pylab.xlabel('t')
pylab.ylabel('f')
pylab.savefig('coin_toss_trials.pdf')

pylab.show()
