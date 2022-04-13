#include <iostream>

int main() {
    int i = 0;
    // Captures i by reference; increments it by one
    auto addOne = [&] () {
        i++; 
    };

    while(i < 10) {
        addOne(); //Add 1 to i
        std::cout << i << "\n";
    }
}
