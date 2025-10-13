#include <stdio.h>
#include <time.h>

int buscaBinariaIterativa(int vetor[], int tamanho, int chave, int *comparacoes) {
    int inicio = 0;
    int fim = tamanho - 1;
    int meio;

    *comparacoes = 0;

    while (inicio <= fim) {
        (*comparacoes)++;

        meio = inicio + (fim - inicio) / 2;

        if (vetor[meio] == chave) {
            return meio;
        }

        if (chave < vetor[meio]) {
            fim = meio - 1;
        } else {
            inicio = meio + 1;
        }
    }

    return -1;
}

int main() {
    int meuVetor[] = {1, 2, 3, 5, 7, 8, 10, 12, 13, 15, 16, 17, 18, 20, 23, 24, 26, 30, 32, 38, 42, 43, 48, 49, 50, 56, 61, 62, 66, 69, 72, 74, 75, 80, 89, 91, 96, 99};
    int n = sizeof(meuVetor) / sizeof(meuVetor[0]);
    int numeroProcurado;

    int contagemComparacoes = 0;
    clock_t tempo_inicio, tempo_fim;
    double tempo_execucao;

    printf("Vetor com valores de 1 a 99. \n");
    printf("Digite o numero que deseja encontrar: ");
    scanf("%d", &numeroProcurado);

    tempo_inicio = clock();
    int resultado = buscaBinariaIterativa(meuVetor, n, numeroProcurado, &contagemComparacoes);
    tempo_fim = clock();

    tempo_execucao = ((double)(tempo_fim - tempo_inicio)) / CLOCKS_PER_SEC;

    if (resultado != -1) {
        printf("\n--- Resultados ---\n");
        printf("O numero %d foi encontrado no indice %d do vetor.\n", numeroProcurado, resultado);
    } else {
        printf("\n--- Resultados ---\n");
        printf("O numero %d nao foi encontrado no vetor.\n", numeroProcurado);
    }

    printf("Numero de comparacoes realizadas: %d\n", contagemComparacoes);
    printf("Tempo de execucao da busca: %f segundos.\n", tempo_execucao);

    return 0;
}