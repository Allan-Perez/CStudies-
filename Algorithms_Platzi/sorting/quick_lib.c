#include <stdio.h>


void print_array(int *a, int len){
	printf("{");
	for (int i = 0; i < len; ++i)
	{
		printf("%d ",a[i]);
	}
	printf("}\n");
}
void swap(int* a, int* b ){
	int aux = *b;
	*b = *a;
	*a = aux;
}

int partition(int *arr, int low, int high){
	int pivot = arr[high];
	int index = low-1;
	for (int i = low; i < high; i++)
	{
		if(arr[i] < pivot ){
			index++;
			swap(&arr[index], &arr[i]);
		}
	}
	swap(&arr[index+1], &arr[high]);
	return index+1;
}

void quicksort(int *arr, int low, int high){
	if (low < high)
	{
		int part_index = partition(arr, low, high);

		quicksort(arr, low, part_index-1);
		quicksort(arr, part_index+1, high);
	}
}