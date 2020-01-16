import java.util.HashMap;

public class java {
  public static int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<>();
    int compliment;
    for (int i = 0; i < nums.length; i++) {
      compliment = target - nums[i];
      if (map.containsKey(compliment)) {
        return new int[] {map.get(compliment), i};
      }
      map.put(nums[i], i);
    }
    return null;
  }

  public static void main(String args[]) {
    int [] nums = {2,7,11,15};
    int target = 18;
    int[] answer = twoSum(nums, target);
    if (answer == null) {
      System.out.println("BAD");
    } else {
      System.out.print(answer[0]);
      System.out.print(" " + answer[1]);
    }
  }
}
