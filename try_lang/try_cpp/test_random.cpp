#include <iostream>
#include <vector>
#include <cstdlib>

template<typename T>
T random(std::vector<T> const &v)
{
	auto it = v.cbegin();
	int random = rand() % v.size();
    std::cout << "in random: " << random << std::endl;
	std::advance(it, random);

	return *it;
}

int main()
{
	std::vector<int> v = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

	for (int i = 0; i < 5; i++) {
		std::cout << random(v) << std::endl;
	}

	return 0;
}

