#include <stdio.h>
#include <stdlib.h>
#include "../sorting/quick_lib.c"

int linear_search(int arr[], int n, int search){
	int to_return = -1;
	for (int i = 0; i < n; ++i)
	{
		if(arr[i] == search && to_return == -1){
			to_return = i;
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
	for (int i = 0; i < n; ++i)
	{
		printf("A[%d]: ", i+1);
		scanf("%d", &A[i]);
	}

	quicksort(A, 0, n);

	printf("Array: ");
	print_array(A, n);

	int what_to_search;
	printf("\nWhat to search: ");
	scanf("%i", &what_to_search);

	int index = linear_search(A, n, what_to_search);
	if(index >= 0){
		printf("What you are looking for is in ARRAY[%i]: %i\n", index, A[index]);
	}else{
		printf("Couldn't find %i\n",what_to_search );
	}

	return 0;
}
