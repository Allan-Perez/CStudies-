#include <stdio.h>

//The first element of an array will always be the size of that array (including the last one)

void print_array(int *a, int n){
	int len = n;

	printf("{");
	for (int i = 0; i < len; ++i)
	{
		printf("%d ",a[i]);
	}
	printf("}\n");
}

void merge(int *arr, int *carr, int start, int middle, int end){
	int s = start;
	int m = middle;
	int e = end; 


	for(int i=start; i<end; i++){
		if(s < middle && (m >= end || arr[s] <= arr[m])) {
            carr[i] = arr[s];
            s = s + 1;
        } else {
            carr[i] = arr[m];
            m = m + 1;
        }
	}
}

void split_merge(int *carr, int *arr, int start, int end){
	if(end - start == 1){
		return;
	}

	int middle = (start+end)/2;

	split_merge(arr, carr, start, middle);
	split_merge(arr, carr, middle, end );

	merge(carr, arr, start, middle, end);
}

void merge_sort(int *arr, int n){

	// Create auxiliar array
	int carr[n];
	memcpy(carr, arr, sizeof(int)*n);
	

	printf("Unsorted array: \n"); 
	print_array(arr, n);   

	split_merge(carr, arr, 0, n);
	
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

	printf("Array: ");
	print_array(A, n);


	merge_sort(A, n);
	return 0;
}