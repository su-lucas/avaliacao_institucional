# Avaliação Institucional

Projeto desenvolvido na disciplina de Laboratório de Programação Back End utilizando Django.

## Objetivo

Criar uma API para um sistema de avaliação institucional, onde alunos avaliam disciplinas.

O projeto foi dividido em três apps:

- alunos
- disciplinas
- avaliacoes

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/su-lucas/avaliacao_institucional.git
cd avaliacao-institucional/backend



## Perguntas

### 1. Por que usamos um ambiente virtual em cada projeto?

Eu uso um ambiente virtual para deixar as bibliotecas de cada projeto separadas. Assim, um projeto pode usar uma versão do Django e outro usar uma versão diferente sem dar conflito. Também facilita para instalar somente o que aquele projeto realmente precisa.

### 2. Por que dividimos o sistema em 3 apps em vez de um só?

Porque cada app tem uma responsabilidade diferente. O app de alunos cuida dos alunos, o de disciplinas cuida das disciplinas e o de avaliações cuida das avaliações. Dessa forma, o projeto fica mais organizado e mais fácil de entender e dar manutenção.

### 3. Para que servem `makemigrations` e `migrate`, e por que nessa ordem?

O `makemigrations` cria os arquivos de alteração com base nas mudanças feitas nos models. Já o `migrate` aplica essas alterações no banco de dados. Por isso, primeiro eu gero as mudanças com `makemigrations` e depois aplico no banco com `migrate`.
