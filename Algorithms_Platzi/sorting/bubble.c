#include <stdio.h>
#include <stdbool.h>

void print_array(int *a, int n){
	int len = n;

	printf("{");
	for (int i = 0; i < len; ++i)
	{
		printf("%d ",a[i]);
	}
	printf("}\n");
}

void bubble_sort(int *arr, int n){
	bool swapped = true;
	while(swapped){
		swapped = false;
		for (int i = 0; i < n; ++i)
		{
			if(arr[i] > arr[i+1]){ //swap
				int v_t_r = arr[i+1];
				arr[i+1] = arr[i];
				arr[i] = v_t_r;
				swapped = true;
			}
		}
	}

	printf("Sorted list: ");
	print_array(arr, n);
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

	printf("Array: ");
	print_array(A, n);

	bubble_sort(A,n);

	return 0;
}