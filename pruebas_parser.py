from AFDs import *
from parser import *
from lexer import * 
print("-----------------------------------------------------prueba 1-----------------------------------------------------")
parser(traduccionParser(lexer('a:=3+5#')))
print("-----------------------------------------------------prueba 2-----------------------------------------------------")
parser(traduccionParser(lexer('var a; #')))
print("-----------------------------------------------------prueba 3-----------------------------------------------------")
parser(traduccionParser(lexer('const perro = 10 ;#')))
print("-----------------------------------------------------prueba 4-----------------------------------------------------")
parser(traduccionParser(lexer("var x, aux; procedure id; const perro = 10;;#")))
print("-----------------------------------------------------prueba 5-----------------------------------------------------")
parser(traduccionParser(lexer("""
begin id:=2 ; end#
""")))
print("-----------------------------------------------------prueba 6-----------------------------------------------------")
parser(traduccionParser(lexer("""
var x, aux;

procedure cuadrado;
begin
    aux := x*x
end;

begin
    x:=1;
end#
""")))
print("-----------------------------------------------------prueba 7-----------------------------------------------------")
parser(traduccionParser(lexer('if perro > gato then gato:=4#')))
print("-----------------------------------------------------prueba 8-----------------------------------------------------")
parser(traduccionParser(lexer('abc:=a+b+c#')))
print("-----------------------------------------------------prueba 9-----------------------------------------------------")
parser(traduccionParser(lexer("call gato #")))
print("-----------------------------------------------------prueba 10-----------------------------------------------------")
parser(traduccionParser(lexer("while x<y do x:=y#")))
print("-----------------------------------------------------prueba 11-----------------------------------------------------")
parser(traduccionParser(lexer("""
procedure whileYcall;
while x>y do call perro;
#
""")))