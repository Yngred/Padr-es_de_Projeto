Padrões criacionais - Prototype
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


