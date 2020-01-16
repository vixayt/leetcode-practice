public class Solution{
  public static boolean isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x !=0)) {
      return false;
    }

    int reverted = 0;
    while(x > reverted) {
      reverted = reverted * 10 + x % 10;
      x /= 10;
    }
    return x == reverted || x == reverted/10;
  }
  public static void main(String args[]) {
    System.out.println(isPalindrome(12321));
    System.out.println(isPalindrome(123321));
    System.out.println(isPalindrome(123123321));
  }
}
