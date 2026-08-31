program CalculadoraSimples;

uses sysutils;

var
  num1, num2, resultado : real;
  operacao : char;

begin
  writeln('--- CALCULADORA EM PASCAL ---');
  writeln;

  { Entrada dos dados }
  write('Digite o primeiro numero: ');
  readln(num1);

  write('Digite a operacao (+, -, *, /): ');
  readln(operacao);

  write('Digite o segundo numero: ');
  readln(num2);

  { Processamento e Estrutura Condicional }
  case operacao of
    '+': resultado := num1 + num2;
    '-': resultado := num1 - num2;
    '*': resultado := num1 * num2;
    '/': 
      begin
        if num2 <> 0 then
          resultado := num1 / num2
        else
        begin
          writeln('Erro: Divisao por zero nao e permitida!');
          halt(1); { Encerra o programa se houver erro }
        end;
      end;
  else
    begin
      writeln('Erro: Operacao invalida!');
      halt(1);
    end;
  end;

  { Saida do Resultado }
  writeln;
  writeln('Resultado: ', num1:0:2, ' ', operacao, ' ', num2:0:2, ' = ', resultado:0:2);

  writeln;
  writeln('Pressione ENTER para sair...');
  readln;
end.