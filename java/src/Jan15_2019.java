/*Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.*/
//JANURARY 15th, 2019
//Anthony Lai

import java.util.Arrays;
public class Jan15_2019{
    public static void main(String[] args) {
        int[] list = {10,15,3,7};
        System.out.println(twoOfListSum(list,17));

    }

    public static boolean twoOfListSum (int[]list, int k){
        Arrays.sort(list);
        int lowIndex = 0;
        int highIndex = list.length - 1;

        while(lowIndex != highIndex){
            int sum = list[lowIndex] + list[highIndex];
            if (sum > k){
                highIndex--;
            }else if (sum < k){
                lowIndex++;
            }else if (sum == k){
                return true;
            }
        }
        return false;
    }

}
