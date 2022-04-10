package com.zixiong.search;

/**
 * Created by zixiong on 2018/06/12.
 */
public class BinarySearch {
    public Integer search(int[] array, int target, int start, int end) {
        int mid = (end + start) / 2;
        if (array[mid] == target) {
            return mid;
        }
        if (start == mid) {
            return null;
        }
        if (array[mid] > target) {
            end = mid;
        } else {
            start = mid + 1;
        }
        return search(array, target, start, end);
    }

    public Integer search2(int[] array, int target) {
        int start = 0;
        int end = array.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (array[mid] == target) {
                return mid;
            }
            if (array[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return null;
    }

    public Integer search3(int[] array, int target) {
        int start = 0;
        int end = array.length - 1;
        Integer result = null;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (array[mid] < target) {
                result = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return result;
    }



    public static void main(String[] args) {
        BinarySearch binarySearch = new BinarySearch();
        int[] array = new int[] {1, 2, 4, 4,4,  5, 6, 7};
        int target = 3;
//        System.out.println("---->" + binarySearch.search(array, target, 0, array.length - 1));
//        System.out.println("---->" + binarySearch.search2(array, target));
        System.out.println("---->" + binarySearch.search3(array, target));
    }
}
