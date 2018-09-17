#include <stdio.h>
#include "../sorting/quick_lib.c"
#include "linear_lib.c"
#include <math.h>

int jump_search(int arr[], int n, int search){
	int jumps = sqrt(n);
	int index_at_which_to_look_at = 0;
	int to_return = -1;

	for (int i = 0; i <= n;i+=jumps)
	{
		printf("Interval: %i/%i\n", i, n);
		if (search <= arr[i])
		{
			int from = i-jumps;
			printf("Interval to look at : %i to %i\n", from, i);
			to_return = linear_search(arr, from, i, search);
		}
	}

	return to_return;
}


int main(int argc, char const *argv[])
{
	int n;

	printf("Lenght of the array: ");
	scanf("%d", &n);
	int A[n];
	printf("Give me values of the array separated by a line break: \n");
	for (int i = 0; i < n; i++)
	{
		printf("A[%d]: ", i+1);
		scanf("%d", &A[i]);
	}
	printf("Array: ");
	print_array(A, n);

	quicksort(A, 0, n-1);

	printf("Array: ");
	print_array(A, n);

	int what_to_search;
	printf("\nWhat to search: ");
	scanf("%i", &what_to_search);

	int index = jump_search(A, n-1, what_to_search);
	if (index == -1)
	{
		printf("%i couldn't be found.\n", what_to_search);
	}else{
		printf("%i is in index ARRAY[%i]\n",what_to_search, index );
	}

	return 0;
}