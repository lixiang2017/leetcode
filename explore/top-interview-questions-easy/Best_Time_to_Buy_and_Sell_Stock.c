/**
You are here!
Your runtime beats 94.99 % of c submissions.
*/

#include <stdio.h>
#include <assert.h>

int maxProfit(int* prices, int pricesSize){
    if (pricesSize <= 1)
    {
        return 0;
    }
    
    int cursor = 0, low = prices[0], max_profit = 0;
    
    for (cursor = 1; cursor < pricesSize; cursor++)
    {
        if (prices[cursor] < low)
        {
            low = prices[cursor];
        }
        if (prices[cursor] - low > max_profit)
        {
            max_profit = prices[cursor] - low;
        }
    }
    
    return max_profit;
}


int main(int argc, char const *argv[])
{
	/* code */
	int prices[] =  {7,1,5,3,6,4};
	int pricesSize = 5;
	int max_profit = maxProfit(prices, pricesSize);
	printf("%d\n", max_profit);
	assert (max_profit == 5);

	return 0;
}



/** run
$ gcc Best_Time_to_Buy_and_Sell_Stock.c
$ ./a.out
*/