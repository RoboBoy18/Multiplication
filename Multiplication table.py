number=int(input('Enter the number whose table you want to print up to 10 multiples: '))
i=1
while(i<=10):
    t=number*i
    print(f'\n{number} * i = {t}')
    i=i+1
