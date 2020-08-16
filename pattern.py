
print("first pattern")
k=(5,4,3,2,1)
m=(1,2,3,4,5)
for p in k:
    pass
for n in m:
    print(" " * p, '* ' * n)
#for p in k:
#    print(n)
#    print(" "*p,'* '*n)

'''
print("first pattern")
m=(1,2,3,4,5)
for n in m:
    print('* '*n)


_____*_____
____*_*____
___*_*_*___
__*_*_*_*__
_*_*_*_*_*_

'''


print("second pattern")
for z in m:
 #   pass
#for x in k:

    if 1==z:
        print('     *     ')
    elif 2==z:
        print('    * *    ')
    elif 3==z:
        print('   * * *   ')
    elif 4==z:
        print('  * * * *  ')
    else:
        print(' * * * * * ')
