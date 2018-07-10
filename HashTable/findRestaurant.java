import java.util.*;

public class findRestaurant{
	public static void main(String args[]){
		String list1[]={"Shogun", "Tapioca Express", "Burger King", "KFC"};
		String list2[]={"KFC", "Shogun", "Burger King"};
		String result[]=find_restaurant(list1,list2);
		System.out.println(Arrays.toString(result));
	}

	public static String[] find_restaurant(String[] list1, String[] list2) {
        HashMap < Integer, List < String >> map = new HashMap < > ();
        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j])) {
                    if (!map.containsKey(i + j))
                        map.put(i + j, new ArrayList < String > ());
                    map.get(i + j).add(list1[i]);
                }
            }
        }
        int min_index_sum = Integer.MAX_VALUE;
        for (int key: map.keySet())
            min_index_sum = Math.min(min_index_sum, key);
        String[] res = new String[map.get(min_index_sum).size()];
        return map.get(min_index_sum).toArray(res);
    }
}