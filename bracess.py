string=input()

def check_bracess(string):
    str1=[]
    for i in range(len(string)):
        if string[i]=='(' or string[i]=='{' or string[i]=='[':
            str1.append(string[i])
        elif string[i]==')' and len(str1)!=0:
            print str1
            val=str1.pop()
            if val=='(':
                pass
            else:
                return 0
        elif string[i]=='}' and len(str1)!=0:
            print str1
            val=str1.pop()
            if val=='{':
                pass
            else:
                return 0
        elif string[i]==']' and len(str1)!=0:
            print str1
            val=str1.pop()
            if val=='[':
                pass
            else:
                return 0
        else:
            return 0
    if len(str1)==0:
        return 1
    else:
        return 0

if check_bracess(string)==1:
    print "valid"
else:
    print "invalid"







