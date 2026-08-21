#### To reverse three - digit number

N = int(input("Enter a three digit number:" ))

A =( N //100 )
B = ( N//10) % 10
C = (N % 10)

reverse = (N % 10 ) * 100 + ((N//10)) % 10 * 10 +(N//100)
print("reverse:", reverse)















