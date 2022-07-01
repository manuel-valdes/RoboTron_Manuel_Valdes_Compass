![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/logo_compass.png)

# 🐙 Introdução

<div align=justify>

Como parte do programa de bolsas da Compass.uol, eu e meus colegas fomos desafiados a resolver, individualmente, uma bateria de exercícios em Python. A ideia é de colocar em prática nossos conhecimentos em Git, GitHub e Python para criar um repositório remoto em que todos os exercícios deverão ser "commitados". Para isso, precisei seguir uma série de passos que passaram pela instalação do Git na minha máquina, pelo estudo e compreensão dos principais comandos relacionados às práticas de versionamento e pela instalação e aplicação de bibliotecas diretamente no ambiente de desenvolvimento. Este documento tem o objetivo de descrever cada um desses passos para que outras pessoas interessadas possam reproduzir essas práticas e desenvolver esses mesmos exercícios ou desafios similares em suas próprias máquinas.
  
Os exercícios, presentes na Sprint 4 do programa de bolsas, foram divididos em duas categorias principais: exercícios de lógica e sintaxe (encontrados no dia 5 da Sprint) e exercícios de manipulação de arquivos com Python (vistos no dia 7). Decidi separá-los em pastas chamadas [exercicios_logica_sintaxe](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/tree/develop/exercicios_logica_sintaxe) e [exercicios_manipulacao_arquivos](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/tree/develop/exercicios_manipulacao_arquivos). Para os do dia 5, criei um arquivo .py separado para cada exercício. Já em relação ao dia 7, pelo fato de existirem vários exercícios direcionados à manipulação de um único arquivo, agrupei todos aqueles que diziam respeito ao mesmo .json ou .csv num lugar só. 
  
A seguir, explicarei em tópicos diferentes como é possível navegar entre essas pastas e arquivos, além de guiar o processo de instalação das diferentes tecnologias e bibliotecas envolvidas no desenvolvimento e na execução dos programas citados. Para navegar entre tópicos, acesse o índice abaixo:
  
- [Instalações](#instalacao)
    - [Git](#git)
    - [Python](#python)
    - [VSCode](#vscode)
    - [Pandas](#pandas)
- [Baixando o repositório](#baixar-repositorio)
    - [Git Clone](#git-clone)
- [Interagindo com os arquivos no VSCode](#arquivos-vscode)
- [Rodando os exercícios no CMD](#cmd)
- [Ferramentas e extensões utilizadas](#ferramentas)
- [Referências](#referencias)
- [Agradecimentos](#agradecimentos)

</div>

<div align=justify>

# 👨‍💻 Instalações<a name="instalacao"></a>

Algumas ferramentas são fundamentais para o desenvolvimento de software. Uma boa parte delas não vem junto com a sua máquina, portanto é essencial esclarecer o processo de instalação desses utilitários e destacar alguns possíveis problemas que podem aparecer ao longo do caminho. Para todas as ferramentas descritas na sequência, parto do pressuposto que a pessoa seguindo estes passos está usando o sistema operacional Windows 10.

## Git<a name="git"></a>
  
O Git é a principal tecnologia de versionamento do mercado. Através dele, equipes de dezenas de pessoas podem trabalhar no mesmo projeto de desenvolvimento sem gerar conflitos destrutivos ou perder informações e funcionalidades cruciais do sistema. O GitHub, site no qual nos encontramos neste momento, é basicamente uma plataforma de hospedagem de código que permite que, através de comandos Git, repositórios locais (aqueles que estão no seu computador) sejam armazenados de maneira remota, ou seja, na internet. 
  
Para que isso seja possível, é necessário que o Git esteja instalado na sua máquina. Os primeiros passos são simples: 

  1. Acesse o [site oficial do Git](https://git-scm.com/)
  2. Clique em "Download for Windows"
  3. Execute o arquivo 
  4. Siga todos os passos indicados no instalador 
  
OBS: O instalador passa por diversas páginas, mas as principais opções são padronizadas e já estão marcadas. Clique "Next" em tudo.
  
Uma das <i>features</i> que virá como resultado do processo de instalação é o "Git Bash", uma espécie de terminal do Git através do qual executaremos nossas ações. Abra o Git Bash e digite os seguintes comandos (aperte Enter depois de escrever o primeiro, só depois escreva o segundo):
  
<div align=center>
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/configurando_git.png)

</div>  
  
Isso permitirá que você insira seus dados, assim todas as suas ações (como commits) serão identificadas. A partir deste momento, seu Git está configurado. Caso você queira criar um repositório local (na sua máquina) e vinculá-lo a um repositório remoto, siga os seguintes passos:
  
1. Crie ou abra a pasta em que você deseja armazenar seu repositório
2. Clique na área vazia da pasta com o botão direito
3. Selecione "Git Bash Here"
4. Execute o comando "git init" (escreva no terminal e aperte Enter)
5. Execute o comando "git remote add origin [url do repositório]" para linkar o repositório local ao GitHub
  
Por enquanto, é isso que você precisa saber sobre Git. Um pouco mais para a frente retomaremos este tópico e explicarei como usar o Git para clonar este repositório e interagir com os exercícios listados. 

## Python<a name="python"></a>
  
Para baixar o Python, entre no site [python.org](https://www.python.org/), vá para a aba de "Downloads" e baixe a última versão do Python para Windows. Execute o instalador e siga todos os passos.
  
IMPORTANTE: tenha certeza de que a seguinte opção está marcada no momento da instalação:
  
<div align=center>    
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/python_path.png)
  
</div> 
  
Note que, na imagem, o Python estava na versão 3.7. Agora já nos encontramos na versão 3.10. Não estranhe essa diferença, é simplesmente pelo fato de que a imagem foi feita há um certo tempo e, na época, o Python estava nessa outra versão.
  
## VSCode<a name="vscode"></a>
  
O Visual Studio Code será nosso ambiente de desenvolvimento (IDE) de preferência. Sua instalação, assim como a do Python, é extremamente simples. Acesse o site do [VSCode](https://code.visualstudio.com/) e clique no botão "Download for Windows (Stable Build)". Siga os passos indicados no instalador, crie um atalho na Área de Trabalho (se achar necessário, eu particularmente acredito que facilita o acesso) e conclua o processo de instalação.
  
## Pandas<a name="pandas"></a>
  
Por se tratar de uma biblioteca, o Pandas não tem um instalador guiado como as outras ferramentas que discutimos até agora. Sua instalação é feita diretamente no terminal por meio do pip - o gerenciador de pacotes nativo do Python. Ainda assim, o processo também é simples. Digite "cmd" na barra de pesquisas do Windows (aquela que fica do lado do botão iniciar) e aperte enter. Com o prompt de comando aberto, digite o primeiro comando da imagem a seguir. É possível que seu pip esteja desatualizado, se essa informação aparecer na mensagem de erro, execute o segundo comando da imagem e rode o primeiro novamente depois de concluído. 
  
<div align=center>  
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/pandas_pip.png)
  
</div>  
  
OBS: Ao abrir o VSCode, o programa indicará que é necessário instalar a extensão do Python para o VSCode para que ele funcione corretamente. NÃO instale essa extensão. Ela acaba conflitando com a sua versão do Python e pode vir a gerar problemas de funcionamento do pip.
  
# 🏋🏽‍♂️ Baixando o repositório<a name="baixar-repositorio"></a>
  
Com todas as nossas ferramentas instaladas, podemos passar para a interação com o repositório remoto. Para puxar o repositório para a sua máquina local, um simples comando Git é o suficiente. Antes de tudo, porém, crie ou acesse uma pasta no seu computador em que você deseja armazenar este repositório. Com isso feito, passamos para o próximo tópico. 
  
## Git Clone<a name="git-clone"></a>
  
O comando "git clone" permite que você puxe um repositório completo para sua máquina através do terminal. Na pasta que você escolheu para armazenar o repositório, clique no espaço vazio com o botão direito e selecione "Git Bash Here". No Bash, digite o seguinte comando (para clonar este repositório, no caso de outros repositórios a URL, naturalmente, seria diferente):
  
<div align=center>  
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/git-clone.png)
  
</div>  
  
Caso você ainda não tenha validado seu login no GitHub dentro desse repositório local, é possível que apareça uma janela pedindo que você autentique seu login. Se você estiver logado no GitHub dentro do seu browser, basta clicar em "Sign in with your browser", como aparece na imagem a seguir:

<div align=center>
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/connect_github.png)
  
</div>
  
Outra forma de trazer um repositório remoto para sua máquina é de, literalmente, baixá-lo. Para isso, entre no link do repositório no GitHub que você deseja baixar, aperta no botão "Code" e selecione a opção "Download ZIP".
  
# 📚 Interagindo com os arquivos no VSCode<a name="arquivos-vscode"></a>
  
Agora que todos os arquivos e pastas do repositório estão na sua máquina, vamos abri-los através do VSCode para que seja possível visualizar o código de maneira mais estruturada. 
  
1. Abra o VSCode
2. No canto superior esquerdo, clique em "File" e em seguida selecione a opção "Open Folder"
3. Localize a pasta em que você clonou ou baixou o repositório
4. Clique em "Selecionar Pasta"
  
Agora, todos os arquivos foram importados para o seu VSCode dentro de suas respectivas pastas. Seu ambiente de exploração de arquivos (à esquerda) deve estar parecido com o da seguinte imagem: 
  
<div align=center>
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/explorer_vscode.png)  
  
</div>
  
Clicando nas setinhas do lado esquerdo das pastas, é possível abri-las e enxergar todos os arquivos que aparecem dentro. A partir deste momento, você é capaz de abrir, executar e editar todos esses arquivos na sua máquina! Porém, existe uma vírgula. No tópico de instalação do Pandas eu comentei que a extensão do Python para o VSCode não era uma boa escolha para os nossos objetivos porque ela pode gerar conflito com o pip, o gerenciador de pacotes. Por isso, para executar nossos arquivos precisaremos usar o Prompt de Comando.
  
# 🖥️ Rodando os exercícios no CMD (Prompt de Comando)<a name="cmd"></a>  
  
O ponto mais importante do CMD é saber navegar entre diretórios (pastas). É preciso estar na pasta em que o arquivo está localizado para poder colocá-lo em ação. Assim, neste momento, apenas três comandos nos interessam. O primeiro deles é o comando "cd" (change directory). Como seu nome indica, a função dele é de mudar de diretório. Por padrão, o ponto de partida é o caminho C:\Users\Usuário (em que "Usuário" seria seu nome ou o nome que colocaram quando o computador estava sendo configurado). Para rodar os arquivos do repositório que clonamos, precisamos chegar até a pasta em que eles estão localizados. Digamos que você deseja rodar algum dos exercícios do dia 5, ou seja, aqueles que estão na pasta [exercicios_logica_sintaxe](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/tree/develop/exercicios_logica_sintaxe). Partindo do caminho inicial, execute o seguinte comando: 
  
<div align=center>
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/cmd_cd_pastas.png)
  
</div>
  
Pronto. Agora estamos na pasta em que os arquivos estão localizados. Mas como faço para rodá-los? Simples: execute o comando "python + nome_do_arquivo.py" e veja o resultado do código no terminal.
  
<div align=center>  
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/exercicio_exemplo.png)
  
</div>
  
O último comando que vamos ver é o "cd..". Ele simplesmente volta para a pasta anterior àquela em que estamos no momento. Por exemplo, se quisessemos explorar os arquivos que estão na pasta [exercicios_manipulacao_arquivos](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/tree/develop/exercicios_manipulacao_arquivos), como poderíamos chegar até lá sabendo que estamos na pasta [exercicios_logica_sintaxe](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/tree/develop/exercicios_logica_sintaxe)? Em dois comandos, estamos lá: 
  
<div align=center>   
  
![](https://github.com/manuel-valdes/RoboTron_Manuel_Valdes_Compass/blob/develop/images/cd_para_tr%C3%A1s.png)
  
</div>
  
Novamente, dentro desta pasta podemos rodar qualquer arquivo que esteja ali através do comando "python + nome_do_arquivo.py".

# 🖥️ Ferramentas e extensões utilizadas<a name="ferramentas"></a>  
  
<div align=center>

<table>
  <tr>
    <td nowrap><strong>Ferramenta</strong></td>
    <td>Função</td>
  </tr>  
  <tr>
    <td>VSCode</td>
    <td>IDE utilizada para desenvolvimento do código e realização de comentários explicando as soluções</td>
  </tr>
  <tr>
    <td>Python</td>
    <td>Linguagem de programação</td>
  </tr>
  <tr>
    <td>Pandas</td>
    <td>Biblioteca do Python para manipulação de arquivos</td>
  </tr>
  <tr>
    <td>PPrint</td>
    <td>Biblioteca do Python para impressão (print()) formatada</td>
  </tr>
  <tr>
    <td>Git</td>
    <td>Versionamento do código</td>
  </tr>
  <tr>
    <td>GitHub</td>
    <td>Repositório remoto usado para compartilhar e armazenar código e dados</td>
  </tr>
  <tr>
    <td>CSV Rainbow</td>
    <td>Extensão do VSCode que facilita a leitura de arquivos .csv</td>
  </tr>
  <tr>
    <td>JSON</td>
    <td>Biblioteca do Python que permite a manipulação de arquivos .json</td>
  </tr>
  <tr>
    <td>Prompt de comando</td>
    <td>Usado para rodar o código</td>
  </tr>
</table>

</div> 
  
# 🤯 Referências<a name="referencias"></a> 

Todos estes exercícios foram desenvolvidos com base no conhecimento gerado por:

- [Documentação do Python](https://www.python.org/doc/) para consultas relacionadas às funcionalidades da linguagem
- [Documentação do Pandas](https://pandas.pydata.org/docs/) para entender o funcionamento e a estrutura de comandos da biblioteca
- [Documentação do Git](https://git-scm.com/doc) para ter em mãos os principais comandos Git
- [Documentação do VSCode](https://code.visualstudio.com/docs) para entender o funcionamento da IDE
- [StackOverflow](https://stackoverflow.com/) para eventuais dúvidas e consulta a erros
- Masterclasses e conteúdo disponibilizado pelo PB da Compass.uol
- [100 days of Python](https://www.udemy.com/course/100-days-of-code/): curso da Udemy que fiz há algum tempo (não cheguei a completar)
- [The modern Python 3 bootcamp](https://www.udemy.com/course/the-modern-python3-bootcamp/): outro curso de Python que rendeu uma série de anotações e aprendizados
- [Canal de Youtube da Rafaella Ballerini](https://www.youtube.com/c/rafaellaballerini) para videoaulas sobre Git e GitHub

# 👏 Agradecimentos<a name="agradecimentos"></a> 

Deixo aqui meus sinceros agradecimentos às pessoas que colaboraram com este projeto:

- [Silvioney Backes](https://github.com/neybackes) pela troca de ideias e ajuda em dúvidas
- [Amanda Bressam](https://github.com/abressam) pela troca de ideias e ajuda em dúvidas
- [Matheus Locatelli](https://github.com/matheuslocatelli) pelo acompanhamento e apoio diário

</div>
