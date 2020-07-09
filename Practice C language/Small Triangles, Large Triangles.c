#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
float area(triangle *tr)
{
    int a=tr->a,b=tr->b,c=tr->c;
    float p=(a+b+c)/2.0;
    return sqrt(p*(p-a)*(p-b)*(p-c));

}
void swap(triangle* tr1, triangle* tr2)
{
    triangle temp=*tr1;
    *tr1 = *tr2;
    *tr2 = temp;
}
void sort_by_area(triangle* tr, int n) {
    int i,j;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(area(&tr[j]) > area(&tr[j+1]))
            {
                swap(&tr[j],&tr[j+1]);
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}