class expressionEval:
    def __init__(self):
        self.precedence = {'^':12,'*':11,'/':11,'//':11,'%':11,'+':10,'-':10,'<<':9,'>>':9,'&':8,'~':7,'|':6,';':5,':':5,'=':5,'>':5,'<':5,',':5,'.':5,'@':4,'#':3,'$':2}
        self.operator = ['date_diff','^','*','/','//','%','+','-','<<','>>','&','~','|',';',':','>','<',',','.','@','#','$','>=','<=','==','!=',')','(']
    def postfixEval(self,expression):
        stack=[]

        for l,i in enumerate(expression):
            print(i)
            print(stack)

            if i not in self.operator:
                stack.append(i)
                print(stack)

            elif '@' in expression:
                #a=expression.find('@')
                ex=expression[:l]
                res=not int(ex)
                return res

            elif '~' in expression:
                #a=expression.find('~')
                ex=expression[:l]
                res=~int(ex)
                return res

            else:
                a=stack.pop()
                if stack:
                   b=stack.pop()
                else:
                   return "value required"

                if i=='+':
                   res=int(b)+int(a)
                elif i=='-':
                   res=int(b)-int(a)
                elif i=='*':
                   res=int(b)*int(a)
                elif i=='%':
                   res=int(b)%int(a)
                elif i=='/':
                   res=int(b)/int(a)
                elif i=='^':
                   res=int(b)**int(a)
                elif i=='>=':
                   res=int(b)>=int(a)
                elif i=='==':
                   res=int(b)==int(a)
                elif i=='!=':
                   res=int(b)!=int(a)
                elif i=='<=':
                   res=int(b)<=int(a)
                elif i=='>':
                   res=int(b)>int(a)
                elif i=='<':
                   res=int(b)<int(a)
                elif i=='#':
                   res=int(b) and int(a)
                elif i=='$':
                   res=int(b) or int(a)
                elif i=='&':
                   res=int(b)&int(a)
                elif i=='|':
                   res=int(b)|int(a)
                stack.append(res)

        return res

    def logical(self,ex):
        if 'not' in ex:
            ex=ex.replace('not','@')
        if 'and' in ex:
            ex=ex.replace('and','#')
        if 'or' in ex:
            ex=ex.replace('or','$')
        return ex

    def stringEqual(self,ex):
        if '=' in ex:
            a=ex.find('=')
            ex=ex[a+1:]
        return ex
    def consts(self,ex):
        if 'c:' in ex:
            ex=ex.replace('c:','')
        return ex

    def inToPost(self,ex):
        ex=self.consts(ex)
        ex=ex.split()
        ex=self.logical(ex)
        #ex=comparision(ex)
        ex=self.stringEqual(ex)

        stack = []
        output = []
        for ch in ex:

           if ch not in self.operator:
                output.append(ch)

           elif ch=='(':
                stack.append('(')

           elif ch==')':
                while stack and stack[-1]!= '(':
                    output.append(stack.pop())
                stack.pop()

           else:
                while stack and stack[-1]!='(' and self.precedence[ch]<=self.precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append(ch)

        while stack:
            output.append(stack.pop())
        return output


c=expressionEval()

ex = input('Enter infix ex')

postfix=c.inToPost(ex)
print('postfix ex',postfix)

res=c.postfixEval(postfix)
print('Evaluation result: ',res)




