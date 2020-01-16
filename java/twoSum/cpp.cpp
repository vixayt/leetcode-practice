#include <iostream>
/*
	INCOMPLETE!
	Create a struct to finish this, save values there.
*/

int * twoSum(int * nums, int target);

int * twoSum(int * nums, int target) {
	std::vector<int> res;
	for (int i = 0; i < 4; ++i) {
		for (int j = 1; j < 4; ++j) {
			if (nums[i] == target - nums[j])
				res[0] = i;
				res[1] = j;
				std::cout << "Found!\n";
				return *res;
		}
	}
	int error[1] = {69};
	return error;
}

int main() {
	int nums[4] = {2, 7, 11, 15 };
	int target = 26;
	int * pNums = twoSum(nums, target);
	std::cout << "Numbers: ";
	std::cout << *pNums +2 << std::endl;
	// std::cout << pNums[0] << ", " << pNums[1] << std::endl;
	return 0;
}

