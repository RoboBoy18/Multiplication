number=int(input('Enter the number whose multiplication table you want to print up to 10 multiples:'))
i=1
while(i<=10):
    t=number*i
    print('\n{} * i = {}'.format(number,t))
    i+=1
