# Decode the glyph-scrambled text layer of Scribd doc 521374064 (NptelQuizzes.pdf).
# usage: pdftotext -enc UTF-8 -layout NptelQuizzes.pdf raw.txt && python nq_decode.py raw.txt > decoded.txt
# shortcut: mapping inferred by hand from known phrases; rare symbols may stay wrong.
import sys
sys.stdout.reconfigure(encoding="utf-8")
M = {
 'a':'m','b':'b','c':'f','d':'j','e':'o','f':'i','g':'k','h':'d','i':'g','j':'n','k':'l','l':'c','m':'h',
 'o':'a','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z','`':'e',
 'X':'T','L':'C','E':'O','O':'A','A':'M','M':'H','H':'D','D':'J','J':'N','F':'I','C':'F','K':'L','R':'R',
 'Y':'W','U':'_',chr(92):'S','^':'P','@':'E','B':'B','V':'Y','P':'U','S':'V','I':'G','G':'K','W':'"','Q':"'",
 '?':'1','>':'0','2':'2','<':'3','8':'4','0':'5','3':'6','9':'7','7':'8','6':'9','1':'=','4':':','5':'?',
 '\ufb0f':'fi','\ufb0e':'fl','\u25e3':'°',
}
M['='] = '8'
assert ''.join(M.get(c, c) for c in 'Xm` Dey ec Leaputfji usfji ^ytmej') == 'The Joy of Computing using Python'
t = open(sys.argv[1], encoding='utf-8', errors='replace').read()
sys.stdout.write(''.join(M.get(c, c) for c in t))
