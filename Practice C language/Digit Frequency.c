#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *s;
    int i, *hashTable = (int *)calloc(10, sizeof(int)), v;
    s = (char *)malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    for (i = 0; s[i] != NULL; i++)
    {
        v = (int)s[i];
        if (v >= 48 && v <= 57)
        {
            hashTable[v - 48]++;
        }
    }
    i = 0;
    while (i < 10)
    {
        printf("%d ", hashTable[i]);
        i++;
    }
    free(s);
    free(hashTable);
    return 0;
}
