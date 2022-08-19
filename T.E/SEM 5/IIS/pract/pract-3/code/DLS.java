class Tree{
    int val;
    Tree left;
    Tree right;
    Tree(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }

}

public class DLS{
    public static void main(String[] args) {
        Tree binaryTree = new Tree(1);
        binaryTree.left = new Tree(2);
        binaryTree.right = new Tree(3);

        binaryTree.left.left = new Tree(4);
        binaryTree.left.right = new Tree(5);

        binaryTree.right.left = new Tree(6);
        binaryTree.right.right = new Tree(7);

        int h = 2;
        int tar = 2;

        int x = searchDLS(binaryTree, h, tar) == 0? -1:searchDLS(binaryTree, h, tar);
        
        
        System.out.println(x);
    }

    private static int searchDLS(Tree bt, int h, int t){
        h--;
        if (h == -1) return 0;
        if(bt == null) return 0;

        System.out.println(bt.val);
        if(t == bt.val) return bt.val;
        int l = searchDLS(bt.left, h, t);
        if (l != 0) return l;
        int r = searchDLS(bt.right, h, t);
        if (r != 0) return r;
        return l==0?r:l;
    }
}