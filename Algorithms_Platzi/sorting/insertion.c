#include <stdio.h>

#define lenght 10


void print_array(int *a, int len){
	printf("{");
	for (int i = 0; i < len; ++i)
	{
		printf("%d ",a[i]);
	}
	printf("}\n");
}

void iterate_and_compare(int *arr, int n){
	int n_queue = 0;

	for (int i = 0; i < n; ++i)
	{
		int focused_value = arr[i];
		int i_focused_v = i;
		for (int j = n_queue; j >= 0; --j)
		{
			if(focused_value < arr[j]){
				int value_to_replace = arr[j]; 
				arr[j] = focused_value;
				arr[i_focused_v] = value_to_replace;
				i_focused_v = j;
			}

		}
		n_queue++;			
	}


}

void insertion_sort(int *arr, int n){
	printf("Unsorted array: \n"); 
	print_array(arr, n); 

	iterate_and_compare(arr, n);

	printf("Sorted array: \n");
	print_array(arr, n); 
}

int main(){
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
	insertion_sort(A, n);
	return 0;
}