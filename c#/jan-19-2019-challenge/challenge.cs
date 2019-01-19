/* Given an array of integers, find the first missing positive integer in linear time and constant space. 
 * In other words, find the lowest positive integer that does not exist in the array. 
 * The array can contain duplicates and negative numbers as well.
 * 
 * For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
 * 
 * You can modify the input array in-place.*/

 //
 //Anthony Lai
 //Jan 19th, 2019
 //Find the lowest missing postive integer in the sequence of a given list
 //

using System;

namespace jan_19_2019_challenge
{
    class jan_19_2019_challenge
    {
        public static void Main()
        {
            int[] array = { 3, 4, -1, 1 };
            Console.WriteLine(lowestMissing(array));
        }

        public static int lowestMissing(int[] arr)
        {
            int missing = 0;
            Array.Sort(arr);
            int prev = arr[0];

            for (int i = 1; i < arr.Length; i++)
            {
                if (prev > 0)
                {
                    if ((arr[i] - prev) > 1)
                    {
                        missing = prev+1;
                        break;
                    }
                }
                prev = arr[i];
            }

            return missing;

        }
    }
}
