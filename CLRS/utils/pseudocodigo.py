ident = "    " # 4 espacos de identacao
texto = '<ol style="font-family: monospace;">\n'

f = open("texto.txt")
titulo = f.readline().split("(")
texto += '<li><span style="font-variant: small-caps;">'+titulo[0]+'</span>('+titulo[1]+'</li>\n'

for s in f:
	k = s.count(ident)
	texto += '<li style="padding-left: '+str(k*len(ident))+'em;">'+s.strip()+'</li>\n'

texto += "</ol>"

print texto