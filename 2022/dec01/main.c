#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int n, int m)
{
    if (n > m)
        return n;
    return m;
}

int part_one(void)
{
    FILE *file = fopen("input.txt", "r");
    if (!file)
        return -1;

    char line[10];
    int curr, high = 0;
    while (fgets(line, sizeof(line), file))
    {
        if (strcmp(line, "\n"))
        {
            curr += atoi(line);
        }
        else
        {
            high = max(curr, high);
            curr = 0;
        }
    }
    fclose(file);
    return max(curr, high);
}

int main(void)
{
    int p1 = part_one();
    printf("%d\n", p1);
    return 0;
}
