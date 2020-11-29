    
def AFD():
    
    d = {}
    efe = {''}
    
    # function find character
    def find(string, character):
        index = 0
        while (index < len(string)):
            if string[index] == character:
                return index
            index += 1
        return -1

    program = open('ProgramaAFD.txt')
    for line in program:
        a,b,c = line.split()
        ifFind = find(c, '-')
        if ifFind != -1:
            efe.add(c.rstrip('-accept'))
        d[a,b]=c.rstrip('-accept')
    program.close()

    def AFD_d(d, q0, F, tape):
        q = q0
        for simbol in tape:
            q = d[q, simbol]
        return q in F

    # file definition
    entry = open('Entrada.txt')
    output = open('Salida.txt','w')
    output = open('Salida.txt','a')
    lines = entry.readlines()

    for i in lines:
        writeOutput = 'La entrada ' + i.rstrip('\n') + ' es '
        definition = {True:'aceptada', False:'rechazada'}
        writeOutput = writeOutput + definition[AFD_d(d, '0', efe, i.rstrip('\n'))]
        output.write(writeOutput + '\n')
    entry.close
    output.close()
    
def MT():
    
    # definition of loop stop
    N = 1000 
 
    class TuringMachine:
    
        def __init__(self, entry, input, state=0):
            self.trf = {}
            self.state = str(state)
            self.tape = ''.join(['_']*N)
            self.head = N // 2   # head is positioned in the middle
            self.tape = self.tape[:self.head] + input + self.tape[self.head:]
            for line in entry.splitlines():
                    s, a, r, d, s1 = line.split(' ')
                    self.trf[s,a] = (r, d, s1)
    
        def step(self):
            if self.state != 'H':
                a = self.tape[self.head]
                action = self.trf.get((self.state, a))
                if action:
                    r, d, s1 = action
                    self.tape = self.tape[:self.head] + r + self.tape[self.head+1:]
                    if d != '*':
                        self.head = self.head + (1 if d == 'r' else -1)
                    self.state = s1
                    print(self.tape.replace('_', ''), self.state)
    
        def run(self, max_iter=9999):
            iter = 0
            while self.state != 'H' and iter < max_iter: # prevent infinite loop
                self.step()
                iter += 1
            print(self.tape.replace('_', ''), self.state)

    input = '110110_1'
    entry = open('ProgramaMT.txt').read()
    tm = TuringMachine(entry, input)
    tm.run()

content = open('Entrada.txt', 'r')
sizeFile = len(content.readlines())
if content=='':
    print("Error: no input file");
if sizeFile > 2:
    AFD()
if sizeFile <= 1:
    MT()

