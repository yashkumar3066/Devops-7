#include <iostream>
#include <string>
#include <algorithm>  // For std::reverse

int main() {
    // Input string
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);

    // Reverse the string using std::reverse
    std::reverse(str.begin(), str.end());

    // Output the reversed string
    std::cout << "Reversed string: " << str << std::endl;

    return 0;
}
