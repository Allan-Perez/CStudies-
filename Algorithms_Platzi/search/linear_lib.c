#include <stdio.h>


int linear_search(int arr[], int start, int end, int search){
	int to_return = -1;
	for (int i = start; i <= end; ++i)
	{
		if(arr[i] == search && to_return == -1){
			to_return = i;
		}
	}
	return to_return;
}
