#include <stdio.h>
#include <math.h>

// Funções Auxiliares
int num_de_digitos(long long n) {
    if (n == 0) return 1;
    int count = 0;
    while (n > 0) {
        count++;
        n /= 10;
    }
    return count;
}

long long potencia_10(int exp) {
    long long resultado = 1;
    for (int i = 0; i < exp; i++) {
        resultado *= 10;
    }
    return resultado;
}

long long maximo(long long a, long long b) {
    return (a > b) ? a : b;
}

// Algoritmo 
long long M_trad(long long x, long long y) {
    if (x < 10 || y < 10) {
        return x * y;
    }
    
    int n = num_de_digitos(maximo(x, y));
    int m = n / 2;  
   
    long long divisor = potencia_10(m);
  
    long long xL = x / divisor;
    long long xR = x % divisor;
    long long yL = y / divisor;        
    long long yR = y % divisor;
    
    long long p1 = M_trad(xL, yL);
    long long p2 = M_trad(xL, yR);
    long long p3 = M_trad(xR, yL);
    long long p4 = M_trad(xR, yR);
    
    long long potencia_2m = potencia_10(2 * m);
    long long potencia_m = potencia_10(m);
    
    long long resultado = potencia_2m * p1 + potencia_m * (p2 + p3) + p4;
    
    return resultado;
}

int main() {
    long long x, y;
    
    printf("=== Algoritmo de Multiplicação por Divisão e Conquista ===\n\n");
    
    // Teste 1
    x = 12;
    y = 34;
    printf("M_trad(%lld, %lld) = %lld\n", x, y, M_trad(x, y));
    printf("Verificação: %lld × %lld = %lld\n\n", x, y, x * y);
    
    // Teste 2
    x = 1234;
    y = 5678;
    printf("M_trad(%lld, %lld) = %lld\n", x, y, M_trad(x, y));
    printf("Verificação: %lld × %lld = %lld\n\n", x, y, x * y);
    
    // Teste 3
    x = 99;
    y = 99;
    printf("M_trad(%lld, %lld) = %lld\n", x, y, M_trad(x, y));
    printf("Verificação: %lld × %lld = %lld\n\n", x, y, x * y);
    
    // Teste interativo
    printf("Digite dois números para multiplicar: ");
    scanf("%lld %lld", &x, &y);
    printf("M_trad(%lld, %lld) = %lld\n", x, y, M_trad(x, y));
    
    return 0;
}