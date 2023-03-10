#A가 B보다 큰 경우에는 '>'를 출력한다.
#A가 B보다 작은 경우에는 '<'를 출력한다.
#A와 B가 같은 경우에는 '=='를 출력한다.

input_num=input().split(' ')
A = int(input_num[0])
B = int(input_num[1])

if (A > B):
    print('>')
    
if (A < B) :
    print('<')
    
if (A == B):
    print('==')


#하루에 하나씩이지만, 벌써 python에 자신감이 붙고 있다. '꾸준히'의 힘을 보여주자