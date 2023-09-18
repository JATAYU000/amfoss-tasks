s=input().strip()
if "h" in s and "h" in s and "e" in s and "l" in s and "o" in s:
    ind=s.index('h')
    if 'e' in s[ind+1:]:
        ind=s.index('e',ind+1)
        if "l" in s[ind+1:] and ind !=0:
            ind=s.index('l',ind+1)
            if "l" in s[ind+1:] and ind !=0:
                ind=s.index('l',ind+1)
                if 'o' in s[ind+1:] and ind !=0:
                    ind=s.index('o',ind+1)
                    print("YES") if ind !=0 else print("NO")
                else:print("NO")
            else:print("NO")
        else:print("NO")
    else:print("NO")
else:print("NO")
            
