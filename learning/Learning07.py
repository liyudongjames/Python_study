L = ['Hello', 'World', 18, 'Apple', None]
W = [s.lower() for s in L if(isinstance(s, str))]
print(W)
