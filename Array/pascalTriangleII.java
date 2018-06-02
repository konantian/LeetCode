import java.util.*;

public class pascalTriangleII{
	public static void main(String [] args){
		int rowIndex=5;
		List<Integer> LL = getRow(5);
		System.out.println(Arrays.toString(LL.toArray()));
	}

	public static List<Integer> getRow(int rowIndex) {
	List<Integer> list = new ArrayList<Integer>();
	if (rowIndex < 0)
		return list;

	for (int i = 0; i < rowIndex + 1; i++) {
		list.add(0, 1);
		for (int j = 1; j < list.size() - 1; j++) {
			list.set(j, list.get(j) + list.get(j + 1));
		}
	}
	return list;
	}
}