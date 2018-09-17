#include <stdio.h>

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