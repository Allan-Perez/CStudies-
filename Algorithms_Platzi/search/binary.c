#include <stdio.h>
#include "../sorting/quick_lib.c"

int binary_search(int arr[], int start, int end, int search){
	if( end >= 1){
		int middle = start + (end-start)/2;
		printf("Middle: %i\n", arr[middle]);
		if(arr[middle] == search){
			return middle;
		}if(arr[middle] > search){
			return binary_search(arr, start, middle-1, search);
		}
		return binary_search(arr, middle+1, end, search);
	}
	return -1;

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

	int index = binary_search(A, 0, n-1, what_to_search);
	if(index >= 0){
		printf("What you are looking for is in ARRAY[%i]: %i\n", index, A[index]);
	}else{
		printf("Couldn't find %i\n",what_to_search );
	}

	return 0;
}