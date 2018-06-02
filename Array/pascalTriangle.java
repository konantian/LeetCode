import java.util.*;

public class pascalTriangle{
	public static void main(String[] args){
		int numRows=5;
		List<List<Integer>> array = generate(numRows);
		System.out.println(Arrays.toString(array.toArray()));
	}

	public static List<List<Integer>> generate(int numRows){
	List<List<Integer>> allrows = new ArrayList<List<Integer>>();
	ArrayList<Integer> row = new ArrayList<Integer>();
	for(int i=0;i<numRows;i++)
	{
		row.add(0, 1);
		for(int j=1;j<row.size()-1;j++)
			row.set(j, row.get(j)+row.get(j+1));
		allrows.add(new ArrayList<Integer>(row));
	}
	return allrows;
	
	}
}