#include<iostream>

int main() {
    // This declares a lambda, which can be called just like a function
    auto print_message = [](std::string message) 
    { 
        std::cout << message << "\n"; 
    };

    // Prints "Hello!" 10 times
    for(int i = 0; i < 10; i++) {
        print_message("Hello!"); 
    }
}
