#include <stdio.h>
#include <string.h>

int main(void) {
    int tc;
    scanf("%d", &tc);
    
    char buf[1005];
    
    while (tc--) {
        scanf("%s", buf);
        
        int cntN = 0, cntS = 0, cntE = 0, cntW = 0;
        int len = strlen(buf);
        
        for (int i = 0; i < len; i++) {
            char c = buf[i];
            if (c == 'N') cntN++;
            else if (c == 'S') cntS++;
            else if (c == 'E') cntE++;
            else if (c == 'W') cntW++;
        }
        
        int okNS = (cntN > 0 && cntS > 0) || (cntN == 0 && cntS == 0);
        int okEW = (cntE > 0 && cntW > 0) || (cntE == 0 && cntW == 0);
        
        if (okNS && okEW)
            printf("Yes\n");
        else
            printf("No\n");
    }
    
    return 0;
}