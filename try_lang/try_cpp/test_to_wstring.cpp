/*
g++ -std=c++11 test_to_wstring.cpp

std::wcout: 23.43
to_wstring: 23.430000

std::wcout: 1e-09
to_wstring: 0.000000

std::wcout: 1e+40
to_wstring: 10000000000000000303786028427003666890752.000000

std::wcout: 1e-40
to_wstring: 0.000000

std::wcout: 1.23457e+08
to_wstring: 123456789.000000
*/

#include <iostream>
#include <string>
 
int main()
{
    for (const double f : { 23.43, 1e-9, 1e40, 1e-40, 123456789. }) {
        std::wcout << "std::wcout: " << f << '\n'
                   << "to_wstring: " << std::to_wstring(f) << "\n\n";
    }
}
