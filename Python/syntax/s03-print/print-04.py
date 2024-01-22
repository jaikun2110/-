formet="{0}, {1}"

hello="hello"
world="world"
helloworld = formet.format(hello, world)

print(helloworld)


#%%

number1 = "더하기: {0} + {1} = {2}"
number2 = "더하기: {2} <- {0} + {1}"
a=10
b=20
c=a+b

print(number1.format(a, b, c))
print(number2.format(a, b, c))