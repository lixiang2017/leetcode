/*
g++ -std=c++11 test_to_string.cpp

std::cout: 23.43
to_string: 23.430000

std::cout: 1e-09
to_string: 0.000000

std::cout: 1e+40
to_string: 10000000000000000303786028427003666890752.000000

std::cout: 1e-40
to_string: 0.000000

std::cout: 1.23457e+08
to_string: 123456789.000000
*/

#include <iostream>
#include <string>
 
int main()
{
    for (const double f : {23.43, 1e-9, 1e40, 1e-40, 123456789.})
        std::cout << "std::cout: " << f << '\n'
                  << "to_string: " << std::to_string(f) << "\n\n";
}

