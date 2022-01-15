import re
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

class Description :
    x = 0
    y = 0
    desc = ''
    def __init__(self, para) :
        self.desc = para
        self._words = self.desc.split()
        self._len = len(self._words)
        self._xcount = 0
        self._ycount = 0
    def gen_dot(self) :
        self.x = self._xcount / self._len
        self.y = self._ycount / self._len
    def parse(self) :
        for word in self._words :
                if word in ['project', 'space', 'group', 'crowd', 'user', 'field', 
                'jira', 'confluence', 'bitbucket', 'workflow', 'dashboard', 'epics', 'stories'] : #subject of request on x
                    self._xcount += 1
                elif word in ['repository', 'page'] :
                    self._xcount -= 3

                elif word in ['admin', 'permisson', 'jenkins', 'access'] : #nature of request on y
                    self._ycount -= 3
                elif word in ['create', 'delete', 'archive', 'new', 'error', 'thanks', 'see'] : 
                    self._ycount += 1
            


class Seperator :
    doc = 'test.txt'
    model = svm.SVC(kernel='linear', C=1.0)
    def __init__(self, doc, model) :
        self.doc = doc
        self.model = model
    def parse_text(self) :
        try :
            des = open(self.doc)
        except :
            print('Nonexisting File')
            exit()
        out = open(self.doc[:self.doc.find('.txt')] + '_parsed.txt', 'w')
        descriptions = des.read()           # file size expected to be small
        descriptions = descriptions.lower()
        descriptions = descriptions.rstrip()
        descriptions = re.sub(r'[^\w\s]','',descriptions)
        splitdes = descriptions.split("\n\n")
        for paragraph in splitdes :
            para = Description(paragraph)
            para.parse()
            para.gen_dot()
            out.write('%g, %g\n' % (para.x, para.y))
            #print('%g, %g\n' % (para.x, para.y))
        out.close()
        
    def yay_or_nay(self, parsed_doc) :
        parsed = open(parsed_doc)
        out = open(parsed_doc[:parsed_doc.find('.txt')] + '_results.txt', 'w')
        for pair in parsed :
          pair = re.sub(r',','',pair)
          xval = float(pair.split()[0])
          yval = float(pair.split()[1])
          if ((-model.coef_[0][0] / model.coef_[0][1]) * xval - model.intercept_[0] / model.coef_[0][1]) > yval :
              out.write('SKIP\n')
          else : out.write('DO\n')
        out.close()
    
#data from test.txt
x = np.array([0.2,0.0434783,0.33333,0.0652174,0.1111111,0,0.1666667,-0.0909091,0,-0.25,0.0294118,0.04])
y = np.array([0.1,0.0434783,-0.33333,0,0,0.22222,-0.375,-0.136364,-0.25,0.125,-0.323529,-0.08])
                
train_x = np.vstack((x, y)).T
train_y = [1,1,1,1,1,1,0,0,0,0,0,0]

model = svm.SVC(kernel='linear', C=1.0)
model.fit(train_x, train_y)

#console
if len(sys.argv) :
    for arg in sys.argv :
        sep = Seperator(arg, model)
        sep.parse_text()
        sep.yay_or_nay(arg[:arg.find('.txt')] + '_parsed.txt')
    