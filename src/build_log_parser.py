import os
import textwrap

class error_type_object:
    # The type of error as reported by the compiler
    compiler_readable = ''
    # Something more useful to the user (eg "unknown variable" instead of "X was not declared in this scope")
    detection_string = ''
    # Something used to determine which error occurred
    human_readable = ''
    
    # The color used for this error
    color = '\033[0m'
    
    # How many times this error is seen
    counter = 0
    
    def __init__(self, compiler_readable, detection_string, human_readable, color):
        self.compiler_readable = compiler_readable
        self.detection_string  = detection_string
        self.human_readable    = human_readable
        self.color = color
    def print_summary(self):
        if self.counter==0:
            return
        print '%s%d "%s" errors%s'%(self.color, self.counter, self.human_readable, text_colors['reset'])

class error_object:
    # The statement where the error took place
    statement = ''
    # The specific word that caused the error
    word = ''
    # The arrow line that points to the word
    arrow = ''
    # The path of the file where the error took place
    path = ''
    # The directory of the file
    dir = ''
    # The filename
    file = ''
    # The line number where the error took place
    lineNumber = ''
    # The character number where the error took place
    charNumber = ''
    
    def __init__(self, type, line1, line2, line3):
        self.type = type
    
        # Remove excess line breaks at the end of lines and very long paths
        line1 = line1.replace('\n','').replace(pwd, '$pwd')
        line2 = line2.replace('\n','').replace(pwd, '$pwd')
        line3 = line3.replace('\n','').replace(pwd, '$pwd')
        
        # Start to extract information
        self.path       = line1.split(':')[0]
        self.lineNumber = line1.split(':')[1]
        self.charNumber = line1.split(':')[2]
        self.word       = ''
        if self.type.human_readable=='Undefined variable' or self.type.human_readable=='Undefined type':
             self.word = line1.split(':')[4].split("'")[1].split("'")[0]
             # Format the statement
             self.statement = self.statement.replace(self.word, '%s%s%s'%(text_colors['reset'],self.word,self.type.color))
        self.statement  = line2
        self.arrow      = line3
        
        self.file = self.path.split('/')[-1]
        self.dir  = '/'.join(self.path.split('/')[0:-2])
        
        self.type.counter += 1
    
    def print_output(self, settings):
        print ''
        print self.type.color
        print settings.horizontalRule1
        paddingCenterLength = settings.width-2-2*settings.paddingLength-len(self.type.human_readable)-len(self.lineNumber)-1
        paddingCenter = settings.paddingChar*paddingCenterLength
        print_formatted_line('%s%sL%s'%(type.human_readable, paddingCenter, self.lineNumber), settings)
        
        print settings.horizontalRule1
        print_formatted_line(self.dir+'/'+text_colors['reset']+self.file+self.type.color, settings)
        print_formatted_line('  At line %s [character %s]'%(self.lineNumber,self.charNumber), settings)
        print_formatted_line(line1.split(':')[4], settings)
        print_formatted_line(self.statement, settings)
        print_formatted_line('%s%s%s'%(text_colors['reset'],self.arrow,self.type.color), settings)
        print settings.horizontalRule1
        
        print text_colors['reset']
        
file = open('build.log')

pwd = os.getcwd()
print 'Current directory: %s'%pwd

class settings:
    lineStart = '+'
    lineStop  = '+'
    
    width = 80
    paddingLength = 1
    paddingChar = ' '
    paddingString   = paddingChar*paddingLength
    horizontalRule1 = lineStart+'-'*(width-2)+lineStop
    horizontalRule2 = '-'*width

# Taken from http://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
text_colors = {}
text_colors['purple'   ] = '\033[95m'
text_colors['cyan'     ] = '\033[96m'
text_colors['darkcyan' ] = '\033[36m'
text_colors['blue'     ] = '\033[94m'
text_colors['green'    ] = '\033[92m'
text_colors['yellow'   ] = '\033[93m'
text_colors['red'      ] = '\033[91m'
text_colors['bold'     ] = '\033[1m'
text_colors['underline'] = '\033[4m'
text_colors['reset'    ] = '\033[0m'

def format_text(text, settings):
    wrapped_lines = textwrap.wrap(text, settings.width-2-2*settings.paddingLength)
    results = []
    for wl in wrapped_lines:
        paddingLeft = settings.paddingChar*settings.paddingLength
        paddingRightLength = settings.width-2-settings.paddingLength-len(wl)
        
        for tc in text_colors:
            if text_colors[tc] in wl:
                paddingRightLength += len(text_colors[tc])
        
        
        paddingRight = settings.paddingChar*paddingRightLength
        results.append(settings.lineStart + paddingLeft + wl + paddingRight + settings.lineStop)
    return results
def print_formatted_line(line, settings):
    formatted_lines =  format_text(line, settings)
    for fl in formatted_lines:
        print fl



# The "normal" error CMSSW throws when compilation fails.
escapeText = 'In file included from /cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/clhep/2.1.4.1-cms/include/CLHEP/Vector/RotationX.icc:11:0,'

error_types = []
error_types.append(error_type_object('Not declared in this scope',
                                     'was not declared in this scope',
                                     'Undefined variable',
                                     text_colors['cyan']))
error_types.append(error_type_object('Expected primary-expression',
                                     'expected primary-expression before',
                                     'Undefined type',
                                     text_colors['red']))
                                     
error_types.append(error_type_object('Template argument invalid',
                                     'template argument 1 is invalid',
                                     'Template error (unknown type)',
                                     text_colors['blue']))

error_types.append(error_type_object('Invalid type',
                                     'invalid type in declaration before',
                                     'Invalid type (unknown type)',
                                     text_colors['darkcyan']))
                                     
error_types.append(error_type_object('Does not name a type',
                                     'does not name a type',
                                     'Unnamed type',
                                     text_colors['purple']))

error_types.append(error_type_object('Expected unqualified-id',
                                     'expected unqualified-id before',
                                     'unqualified-id (^ related to previous error ^)',
                                     text_colors['purple']))
                                     
error_types.append(error_type_object('Function is not a member of namespace',
                                     'is not a member of',
                                     'Unknown function or method',
                                     text_colors['red']))

error_types.append(error_type_object('Method is not a member of class',
                                     'member function declared in class',
                                     'Unknown method in class',
                                     text_colors['red']))
                                     
error_types.append(error_type_object('Method is not a member of class',
                                     'has no member named',
                                     'Method is not a member of this class',
                                     text_colors['red']))

error_types.append(error_type_object('Expected declaration',
                                     'expected declaration before',
                                     'Syntax error',
                                     text_colors['yellow']))
                                     
error_types.append(error_type_object('No return statement in non void function or method',
                                     'no return statement',
                                     'Function or method missing a return statement',
                                     text_colors['yellow']))

error_types.append(error_type_object('Control reaches end of non-void function',
                                     'control reaches end of non-void function',
                                     'Non void function or method does not return a value',
                                     text_colors['yellow']))
                                     
error_types.append(error_type_object('Method argument mismatch',
                                     'does not match any in class',
                                     'Class method has the wrong arguments',
                                     text_colors['red']))

error_types.append(error_type_object('No matching function call',
                                     'no matching function for call',
                                     'No matching function call',
                                     text_colors['red']))

error_types.append(error_type_object('Statement has no effect',
                                     'statement has no effect',
                                     'This statement has no effect',
                                     text_colors['purple']))

error_types.append(error_type_object('Type/value mismatch',
                                     'type/value mismatch',
                                     'Type/value mismatch',
                                     text_colors['purple']))





print
print
print 'And here is the log file:'

while True:
    line = file.readline().replace('\n','')
    if line == '':
        break
        
    if escapeText in line:
        break
        
    success = False
    for type in error_types:
        if type.detection_string in line:
            line1 = line
            line2 = file.readline()
            line3 = file.readline()
            
            error = error_object(type, line1, line2, line3)
            error.print_output(settings)
            
            success = True
            break
    if success==False:
        line = line.replace('\n','').replace(pwd,'$pwd')
        wrapped_lines = textwrap.wrap(line, settings.width)
        for wl in wrapped_lines:
            print wl
    

print
print 'Sumamry:'
for type in error_types:
    type.print_summary()
print 'The raw compiler report is saved in build.log'



