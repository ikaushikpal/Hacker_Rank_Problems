#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *s;
    int i, len = 0;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    len = strlen(s) + 1;
    s = realloc(s, len);
    for (i = 0; s[i] != NULL; i++)
    {
        if (s[i] == ' ')
            printf("\n");
        else
            printf("%c", s[i]);
    }
    free(s);
    return 0;
}