def f1():
    N=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"]
    G,l=["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree.",],[]
    for d in range(12):l.extend(["",f"On the {N[d]} day of Christmas","My true love sent to me"]+[g for g in G[11-d:]])
    return "\n".join(l[1:])

def f2():
    N=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"]
    G,l=["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree.",],""
    for d in range(12):l+=f"On the {N[d]} day of Christmas\nMy true love sent to me\n"+"\n".join(G[11-d:])+"\n\n"
    return l[:-2]

def f3():
    N=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"]
    G,l=["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree.",],""
    for d in range(12):l+=f"On the {N[d]} day of Christmas\nMy true love sent to me\n"+"\n".join(G[11-d:])+"\n\n"
    return l[:-2]

def f536():
 N,G=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"],["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree."]
 return "".join(f"On the {d} day of Christmas\nMy true love sent to me\n"+"\n".join(G[11-N.index(d):])+"\n\n"for d in N)[:-2]

def f527():
 D,G=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"],["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree."]
 return"\n\n".join(f"On the {d} day of Christmas\nMy true love sent to me\n"+"\n".join(G[11-D.index(d):])for d in D)

def f527():
 D,G="First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth".split(),["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree."]
 return"\n\n".join(f"On the {d} day of Christmas\nMy true love sent to me\n"+"\n".join(G[11-D.index(d):])for d in D)

def f528():
 N,G=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"],["Twelve drummers drumming,","Eleven pipers piping,","Ten lords a-leaping,","Nine ladies dancing,","Eight maids a-milking,","Seven swans a-swimming,","Six geese a-laying,","Five gold rings,","Four calling birds,","Three French hens,","Two turtle doves, and","A partridge in a pear tree."]
 return"\n\n".join("\n".join([f"On the {d} day of Christmas","My true love sent to me"]+G[11-N.index(d):])for d in N)

def f499():
 D,G="First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth".split(),"Twelve drummers drumming,#Eleven pipers piping,#Ten lords a-leaping,#Nine ladies dancing,#Eight maids a-milking,#Seven swans a-swimming,#Six geese a-laying,#Five gold rings,#Four calling birds,#Three French hens,#Two turtle doves, and#A partridge in a pear tree.".split("#")
 return"\n\n".join(f"On the {d} day of Christmas\nMy true love sent to me\n"+"\n".join(G[-D.index(d)-1:])for d in D)
