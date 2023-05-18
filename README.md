# Sudoku Solver with Genetics Algorithm
A Sudoku puzzle solver Python tool with genetics algorithm.

A command-line tool to solve sudoku puzzles with genetics algorithms. It's developed by students of LAIA (Liga Acadêmica de Inteligência Artificial - Artificial Intelligence Academic League).

## Content
- ### [Install and run the project](https://github.com/laiauft/sudoku_genetic_algorithm#install-and-run-the-project-1)
- ### [Documentation](https://github.com/laiauft/sudoku_genetic_algorithm#documentation-1)
- ### [Screenshots](https://github.com/laiauft/sudoku_genetic_algorithm#screenshots-1)
- ### [References](https://github.com/laiauft/sudoku_genetic_algorithm#references-1)
- ### [License](https://github.com/laiauft/sudoku_genetic_algorithm#license-1)
- ### [Genetic Algorithm's Flow](https://github.com/laiauft/sudoku_genetic_algorithm#genetic-algorithms-flow-1)

## Install and run the project

Requeriments: [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/).

Clone the project:

    git clone https://github.com/laiauft/sudoku_genetic_algorithm.git

Enter the project's directory:

    cd sudoku_genetic_algorithm

Update pip:

    pip install --upgrade pip

Install all python packages:

    pip install -r requeriments.txt

Go to file folder location:

    cd src

Run the app:

    python main.py test.txt

## Documentation

### Cromossomo Enconde
Cromossomo = lista de LINHA DO SUDOKU ``[[]]``
Gene = linha de VALORES DO SUDOKU     ``[]``

### Genetic Operators
#### **SELECTION**

O operador de seleção tem como objetivo selecionar individuos da população atual que deverão gerar descendentes, dando preferencia ao melhores individuos da geração atual.

1. #### **Seleção por Roleta**

    Nesse processo é simulado uma roleta no qual cada individuo possui a sua probabilidade de seleção de acordo com o seu nível de aptidão. Assim individuos mais adpatados são mais fáceis de serem selecionados.

3. CROSSING
cruzamento com um ponto de cruzamento
    
     c = crossing_point (PONTO DE CRUZAMENTO)
     
1. MUTATION
A mutação irá envolver alterar o genes para que seja gerado um novo cromossomo para um novo individuo da população

## Screenshots

## References:

* [95 Sudoku Puzzles](http://magictour.free.fr/top95)

## License

MIT License

Copyright (c) 2023 LAIA - Liga Acadêmica de Inteligência Artificial

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Genetic Algorithm's Flow

![Genetic Algorithm's Flow](/GeneticAlgorithm'sFlow.jpg)