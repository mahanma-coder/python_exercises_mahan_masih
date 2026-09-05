t = input('enter text : ')
characters = len(t)
letters = 0
digits = 0
spaces = 0
uppercase = 0
lowercase = 0
t_l = t.split()
t_w = len(t_l)
longest = t_l[0]
shortest= t_l[0]
m_r_c=t[0]
c = 0
m_r_w=t_l[0]
cw=0
for i in t :
    if i.isalpha():
        letters += 1
    if i.isdigit():
        digits += 1
    if i == ' ':
        spaces += 1
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase +=1
for x in t_l:
    if len(x) > len(longest) :
        longest = x
    if len(x) < len(shortest):
        shortest = x
for m in t :
    n = 0
    for j in t :
        if m == j:
            n += 1
    if n > c :
        c = n
        m_r_c = x
for d in t_l:
    w = 0
    for s in t_l:
        if d==s:
            w += 1
    if w > cw:
        cw = w
        m_r_w = d

print("Total characters:", characters)
print("Total words:", t_w)
print("Total letters:", letters)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total uppercase:", uppercase)
print("Total lowercase:", lowercase)
print("Longest word:", longest)
print("Shortest word:", shortest)
print("Most repeated character:", m_r_c)
print("Most repeated word:", m_r_w)      
    
    
    
    
    
    
    
    
    
    
        
