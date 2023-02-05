#include <iostream>
#include <cstdio>
using namespace std;
int main(void)
{
    unsigned int enc[6] = {3746099070, 550153460, 3774025685, 1548802262, 2652626477, 2230518816};
    int a2[4] = {2, 2, 3, 4};
    int val = 0x40 * 1166789954;
    for(int i=0; i< 6; i+=2)
    {
        int v5 = val;
        unsigned int v3 = enc[i], v4 = enc[i + 1];
        for(int j=0; j< 0x40; j++)
        {
            v4 -= (v3 + v5 + 20) ^ ((v3 << 6) + a2[2]) ^ ((v3 >> 9) + a2[3]) ^ 0x10;
            v3 -= (v4 + v5 + 11) ^ ((v4 << 6) + *a2) ^ ((v4 >> 9) + a2[1]) ^ 0x20;
            v5 -= 1166789954;
        }
        enc[i] = v3;
        enc[i + 1] = v4;
    }
    for(int i=0; i < 6; i++)
        printf("\'0x%x\', ", enc[i]);
}