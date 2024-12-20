Padrão criacionais - Prototype
O Prototype é um padrão de projeto criacional que permite copiar objetos existentes sem fazer seu código ficar dependente de suas classes.
PROBLEMAS
As vezes, precisamos copiar um objeto, mas nem sempre é fácil. Se o objeto tiver campos privados, não podemos acessá-los diretamente para copiá-los. Além disso, em algumas situações, a única informação que temos sobre o objeto é sua interface, sem saber sua classe exata. Isso complica ainda mais a tarefa de criar uma cópia. 
SOLUÇÃO
O padrão Prototype resolve o problema de copiar objetos de maneira flexível. Ele define uma interface comum para todos os objetos que suportam clonagem, permitindo que qualquer objeto que a implemente seja clonável. O método clone é o único método dessa interface e é implementado de forma semelhante em todas as classes, criando uma nova instância do objeto atual e copiando seus valores de campo para essa nova instância. Isso é útil porque evita a necessidade de saber a classe exata do objeto ao clonar, tornando o código menos acoplado. Além disso, protótipos pré-construídos permitem a reutilização de objetos configurados de diversas maneiras, economizando tempo e recursos ao invés de criar novos objetos do zero.
EXPLICANDO MEU CÓDIGO:
Interface Prototype: Define o método clone() que é comum a todos os objetos que podem ser clonados.
Classe Shape: Implementa a interface Prototype e fornece uma implementação genérica para o método clone(). Usa deepcopy() para garantir que qualquer subclasse que a herde e a clone crie uma cópia profunda do objeto.
Subclasses Rectangle e Circle: Cada uma estende Shape e implementa o método clone() para retornar uma nova instância da mesma classe.
Classe Application: Serve como o cliente que utiliza o padrão Prototype. Ela cria instâncias de Rectangle e Circle, adiciona cópias desses objetos à lista de shapes, e depois clona todos eles para criar uma lista de shapes_copy.
Método business_logic(): Itera sobre a lista de shapes_copy e imprime o tipo de cada shape, mostrando como o método clone() é utilizado para criar cópias exatas dos objetos originais.
## O diagrama principal encontra-se na pasta imagem.png

Padrão comportamental - Command
padrão Command transforma uma solicitação em um objeto independente, permitindo a parametrização de métodos com diferentes comandos, adiando ou colocando a execução do comando em uma fila, e proporcionando suporte para operações que não podem ser realizadas diretamente.
PROBLEMAS
 O padrão resolve a necessidade de decoupage entre o que deve ser feito e como é feito, promovendo flexibilidade e facilidade na adição de novos comandos. Ele também oferece controle sobre a execução dos comandos, permitindo que sejam executados em diferentes momentos e de diferentes formas. Além disso, encapsula todos os detalhes da execução dentro do comando, o que facilita a manutenção do código.
SOLUÇÃO
envolve encapsular as operações que precisam ser realizadas em objetos comando, que possuem a responsabilidade de executar essas operações. Esses comandos são independentes e podem ser utilizados em diferentes contextos sem acoplamento direto ao código da lógica do negócio. A ideia é criar uma abstração que represente uma ação ou pedido e permitir que esse comando seja manipulado como um objeto. código e promove 
EXPLICANDO MEU CÓDIGO:
 A interface Command define um método execute() que qualquer comando deve implementar. A classe Invoker mantém uma referência para um comando e chama o método execute() para realizar a operação.modularidade.
Como apliquei esses comandos em python? Primeiro, criei uma interface Command usando a classe abstrata ABC do Python, que define o método execute(). Depois, Criei a classe RemoteControl que serve como o invocador. Ela mantém uma referência para um comando e chama o método execute() para realizar a operação e para demonstrar o uso do padrão, criei uma instância de Light e configurei comandos para ligar e desligar a luz.
## O diagrama principal encontra-se na pasta novaimagem.png


