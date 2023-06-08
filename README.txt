CONTROLE DE EQUIPAMENTOS
O projeto "Controle de Equipamentos" é um sistema simples para gerenciar equipamentos utilizando as operações CRUD (Create, Read, Update e Delete) em uma base de dados. Ele permite que os usuários criem, leiam, atualizem e excluam informações sobre os equipamentos.

TECNOLOGIAS UTILIZADAS
Python: A linguagem de programação principal para desenvolver o sistema.
SQLite: Um banco de dados leve e embutido, utilizado para persistir os dados da aplicação.
Biblioteca sqlite3: Uma biblioteca em Python que fornece uma interface para trabalhar com o SQLite.

FUNCIONALIDADES
O sistema de controle de equipamentos possui as seguintes funcionalidades:

Criar um novo equipamento: Permite adicionar informações de um novo equipamento, incluindo nome, descrição e quantidade.
Listar equipamentos: Exibe todos os equipamentos cadastrados, mostrando seu ID, nome, descrição e quantidade.
Atualizar um equipamento: Permite editar as informações de um equipamento existente, como nome, descrição e quantidade.
Excluir um equipamento: Remove um equipamento do banco de dados com base no seu ID.

COMO INSTALAR E EXECUTAR O PROJETO
Certifique-se de ter o Python instalado em seu sistema.
Instale a biblioteca sqlite3 usando o pip: pip install sqlite3.
Faça o download ou clone os arquivos do projeto em seu ambiente de desenvolvimento.
No terminal, navegue até o diretório do projeto.
Execute o comando python atividade_projeto.py para iniciar o sistema.

AVISO LEGAL
Este projeto foi desenvolvido com o objetivo de fornecer uma demonstração de implementação de um sistema de controle de equipamentos básico. É importante ressaltar que ele pode não ser adequado para casos de uso complexos ou em ambientes de produção. Recomenda-se a devida avaliação, testes e adaptação para atender às necessidades específicas do projeto.

OBJETIVO
Realizar um sistema para o Hospital Regional de Presidente Prudente no setor da Engenharia Clínica para que o setor tenha um controle maior de todos os equipamentos em uso no hospital e para ter uma facilidade e agilidade no serviço de empréstimo de equipamentos para as clínicas. Com isso, podemos também eliminar toda burocracia do uso de papéis e cadernos para uma maior automatização do serviço utilizando o sistema, garantindo assim a integridade e confiabilidade dos dados.

DESCRIÇÃO DO AMBIENTE
O sistema de controle de equipamentos foi todo desenvolvido no Visual Studio Code.

ESPECIFICAÇÃO
Linguagem de programação: Python 3.9.7
Biblioteca para acesso ao banco de dados: sqlite3

REQUISITOS
Python 3.9 ou superior instalado.
Biblioteca 'sqlite3' já inclusa na instalação padrão do Python.
Sistema Operacional: A aplicação pode ser executada em sistemas operacionais como Windows, Linux ou macOS, desde que o Python esteja corretamente configurado e instalado.

CONTRIBUIÇÕES
Fork do repositório: Comece fazendo um fork do repositório para sua conta do GitHub. Isso criará uma cópia do projeto em seu próprio repositório.

Clone o repositório: Faça um clone do seu fork do repositório em sua máquina local.

Crie um branch: Antes de começar a fazer alterações, crie um novo branch para trabalhar. É uma boa prática criar um branch separado para cada nova funcionalidade ou correção de bug que você deseja implementar.

Implemente as alterações: Escreva o código para a funcionalidade ou correção que deseja adicionar ao projeto. Certifique-se de seguir as diretrizes de estilo de código existentes e de testar suas alterações.

Faça commits das alterações: Faça commits incrementais com mensagens descritivas para cada conjunto de alterações lógicas que você implementar.

Push das alterações: Após concluir as alterações em seu branch local, faça push das alterações para o seu fork no GitHub.

Abra um pull request: Vá para a página do seu fork no GitHub e abra um pull request para o repositório original. Descreva suas alterações e explique o motivo pelo qual elas devem ser incorporadas ao projeto.

Revisão e discussão: Faça seu pull request e poderá também fazer comentários ou solicitar alterações adicionais. Esteja aberto a feedback e participe de discussões construtivas.

Atualize o pull request: Se forem solicitadas alterações adicionais, faça as modificações necessárias em seu branch local, faça commit e faça push novamente para o GitHub. O pull request será atualizado automaticamente.

Aceitação do pull request: Uma vez que o pull request tenha sido revisado e todas as alterações solicitadas tenham sido implementadas, você poderá mesclar suas alterações ao repositório principal.

PRÁTICAS DE CÓDIGO LIMPO
Nomes significativos, Funções e métodos concisos, evitar duplicação de código, Comentários e documentação, Estrutura e organização, Testes unitários, Manutenibilidade, Refatoração.
Essas são apenas algumas práticas de código limpo que são aplicadas na aplicação de Controle de Equipamentos. O código limpo é um objetivo contínuo e que a adoção dessas práticas pode variar de acordo com o contexto e as necessidades do projeto.

TESTES AUTOMATIZADOS
Neste exemplo, criamos uma classe de teste EquipmentManagerTest que herda da classe unittest.TestCase. O método setUp é executado antes de cada teste e cria uma instância do EquipmentManager.

Cada teste é uma função iniciada com o prefixo test_. No teste test_add_equipment, adicionamos um equipamento e verificamos se o ID do equipamento retornado não é nulo.

No teste test_get_equipment, adicionamos um equipamento, obtemos suas informações e verificamos se os valores estão corretos.

Nos testes test_update_equipment e test_delete_equipment, realizamos operações de atualização e exclusão de um equipamento e verificamos se as alterações foram aplicadas corretamente.

Por fim, o trecho if __name__ == '__main__': unittest.main() permite executar os testes quando o script é executado diretamente.

Esses são apenas exemplos básicos de testes automatizados. Podemos adicionar mais casos de teste, incluindo casos de borda e cenários de erro, para garantir uma cobertura adequada.



