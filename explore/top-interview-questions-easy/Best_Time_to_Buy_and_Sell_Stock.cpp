/**
You are here!
Your runtime beats 12.42 % of cpp submissions.
*/

#include <climits>
#include <vector>
#include <iostream>
#include <cassert>

//using namespace std;

class Solution {
	public:
	    int maxProfit(std::vector<int>& prices) {
	        int low = INT_MAX;
	        int max_profit = 0;
	        
	        for(int i = 0; i < prices.size(); i++)
	        {
	            low = std::min(low, prices[i]);
	            max_profit = std::max(max_profit, prices[i] - low);
	        }
	        return max_profit;
	    }
};


int main(int argc, char const *argv[])
{
	/* code */
	Solution s;
	std::vector<int> prices {7,1,5,3,6,4};
	int ans = s.maxProfit(prices);
	std::cout << ans << std::endl;
	assert (ans == 5);

	return 0;
}


/** run
$ g++ Best_Time_to_Buy_and_Sell_Stock.cpp
$ ./a.out
*/