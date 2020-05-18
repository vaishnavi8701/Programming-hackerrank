#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
main()
{
    int tippercent,taxpercent,total;
    float totalcost;
    float tip,tax;
    double mealcost;
    scanf("%lf",&mealcost);
    scanf("%d",&tippercent);
    scanf("%d",&taxpercent);
    tip=(mealcost*tippercent)/100;
    tax=(mealcost*taxpercent)/100;
    totalcost=tip+tax+mealcost;
    total= roundf(totalcost);
    printf("%d",total);


}
