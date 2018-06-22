public class isValidBST{
	public static void main(String args[]){

	}

	public static boolean is_validbst(TreeNode root) {
        return is_validbst(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
	public static boolean is_validbst(TreeNode root, long minVal, long maxVal) {
        if (root == null) return true;
        if (root.val >= maxVal || root.val <= minVal) return false;
       return is_validbst(root.left, minVal, root.val) && is_validbst(root.right, root.val, maxVal);
	}
}

