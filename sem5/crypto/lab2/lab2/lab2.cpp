#include "pch.h"
#include <iostream>
using namespace std;

//---------------------FIRST TRY ----------------------
// Function to return gcd of a and b 
int gcd(int a, int b)
{
	if (a == 0)
		return b;
	return gcd(b % a, a);
}

// A simple method to evaluate Euler Totient Function 
int phi(unsigned int n)
{
	unsigned int result = 1;
	for (int i = 2; i < n; i++)
		if (gcd(i, n) == 1)
			result++;
	return result;
}

//--------------------------SECOND TRY-----------------------

//To solve this problem we should count all prime factors and their multiples 
//and subtract this count from n to get the totient function value 
//(Prime factors and multiples of prime factors won’t have gcd as 1)

/*
1) Initialize result as nr
2) Consider every number 'p' (where 'p' varies from 2 to nr).
If p divides nr, then do following
a) Subtract all multiples of p from 1 to nr[all multiples of p
will have gcd more than 1 (at least p) with nr]
b) Update nr by repeatedly dividing it by p.
3) If the reduced nr is more than 1, then remove all multiples
of nr from result.

*/
int phi2(int nr)
{
	int result = nr; // Initialize result as nr 

	// Consider all prime factors of nr and substract their 
	// multiples from result 
	for (int p = 2; p * p <= nr; ++p) {

		// Check if p is a prime factor. 
		if (nr % p == 0) {

			// If yes, then update nr and result 
			while (nr % p == 0)
				nr /= p;
			result -= result / p;
		}
	}

	// If n has a prime factor greater than sqrt(nr) 
	// (There can be at-most one such prime factor) 
	if (nr > 1)
		result -= result / nr;
	return result;
}

// Driver program to test above function 
int main()
{	 
	// Read the bound and the value from keyboard
	int value=-1, bound = -1;
	while (bound <= 0) {
		cout << "Give the bound b = ";
		cin >> bound;
	}
	while (value <= 0) {
		cout << "Give the value v = ";
		cin >> value;
	}

	
	cout << "These are the numbers less than " << bound
		<< " for which the Euler function is equal with " << value << ":\n";

	// Call the function for every number less than 'bound'
	// Verify if the value of the Euler functions(phi) is equal with 'value'
	// If it is, print the result

	for (int i = 1; i <= bound; i++) 
		if (phi2(i) == value)
		{
			cout << "phi(" << i << ")= " << phi2(i) << "\n";
		}
	
	return 0;
}