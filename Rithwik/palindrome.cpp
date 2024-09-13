// C++ Program to check whether the
// Array is palindrome or not

#include <iostream>
using namespace std;

void palindrome(int arr[], int n)
{
	// Initialise flag to zero.
	int flag = 0;

	// Loop till array size n/2.
	for (int i = 0; i <= n / 2 && n != 0; i++) {

		// Check if first and last element are different
		// Then set flag to 1.
		if (arr[i] != arr[n - i - 1]) {
			flag = 1;
			break;
		}
	}

	// If flag is set then print Not Palindrome
	// else print Palindrome.
	if (flag == 1)
		cout << "Not Palindrome";
	else
		cout << "Palindrome";
}

// Driver code.
int main()
{
	int arr[] = { 1, 2, 3, 2, 1 };
	int n = sizeof(arr) / sizeof(arr[0]);

	palindrome(arr, n);
	return 0;
}
