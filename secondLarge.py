A = [12, 34, 45, 32, 54]
def secLarge(A):
    n = len(A)
    if n < 2 :
        return -1
        
    first = second = float('-inf')
    for num in A :
        if num > first :
            second = first
            first = num
        elif num > second & num != first :
            second = num
    
    if second != float('-inf'):
        return second
    return -1

print(secLarge(A))

#include <stdio.h>

#int secondLargest(int nums[] , int size){
#    int large, secLarge;
#    large = nums[0];
#    secLarge = -1;
#    for(int i = 0 ; i < size ; i++){
#        if(nums[i] > large){
#            large = nums[i];
#        }
#    }
#    for(int j = 0 ; j < size ; j++){
#        if(nums[j] > secLarge && nums[j] != large){
#            secLarge = nums[j];
#        }
#    }
#    return secLarge;
#}
#int main() {
#    int arr[] = {12, 35, 1, 10, 34, 1};
#    int n = sizeof(arr)/ sizeof(arr[0]);
#
#    printf("The second largest element in given array = %d ", secondLargest(arr, n));
#    return 0;
#}


###############      OUTPUT     #################
#The second largest element in given array = 34 
#################################################
