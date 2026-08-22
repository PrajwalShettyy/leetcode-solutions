bool checkDivisibility(int n) {
    int digit , sumDigit = 0 , productDigit = 1 , temp = n;
    while (temp > 0) {
        digit = temp % 10 ;
        sumDigit += digit ; 
        productDigit *= digit ;
        temp /= 10 ;
    }

    return n % (sumDigit + productDigit)  == 0 ;
}