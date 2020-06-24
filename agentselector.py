import math
import random


def is_available(i):
    root=math.sqrt(i);
    if int(root)**2==i:
        return False;
    else:
        return True;


def all_available(lst,i,x):
     print('available agents are:');
     for i in range(x):
             if is_available(i)==False:
                 p=lst
                 p.remove('agent'+str(i));
     return p;


def availability(i):
    if i%2==0:
        return 2;
    elif i%3==0:
        return 3;
    elif i%5==0:
        return 8;
    elif i%7==0:
        return 6;
    else:
        return 0;


def least_busy(i,x):
   print('agents available in least busy mode are:');
   max=availability(0);
   i=1;
   for i in range(x):
       if is_available(i)==True:
           if availability(i)>max:
               max=availability(i);
               temp=i;
   return 'agent'+str(temp);


def rand(i,x):
    for i in range(x):
     i=random.randint(0,x)
     if is_available(i)==True:
        break;
    print('agent'+str(i));



def default():
    return "invalid choice"


n=input("enter the number of agents:");
x=int (n);
lst=[];
for i in range(x):
    lst.append('agent'+str(i));
print(lst);
i=0;
for agent in lst:
    a=0;
    if is_available(i)==True:
        print('Available agent:agent'+str(i));
        roles=[];
        if i%7==0:
            print('Available from 6 months');
            roles.append('spanish speaker, sales man');
            print('Roles:',roles);
        elif i%5==0:
            print('Available from 8 months');
            roles.append('sales man, marketing');
            print('Roles:',roles);
            a==1;
        elif i%2==0:
            print('Available from 2 months');
            roles.append('french speaker');
            print('Roles:',roles);
        elif i%10==0:
            print('Availble from 3 days');
            roles.append('sales man');
            print('Roles:',roles);
        else:
            print('Available from 3 months');
            roles.append('sales man, french speaker');
            print('Roles:',roles);
    else:
        print('Not available:agent'+str(i));
    i=i+1;

print('\n');
print('If issue is present:');
print('Different modes of selection:');
b=0;
while (b!=1):
    print('1.All available\n2.Least busy\n3.Random\n');
    c=int(input('enter choice:\n'))
    if(c==1):
        fun=[];
        fun=all_available(lst,i,x);
        print(fun);
    elif(c==2):
        fun1=0;
        fun1=least_busy(i,x);
        print(fun1);
    elif (c==3):
        rand(i,x);

    else:
            b=1;
            print("invalid choice");
