import java.util.*;

public class java_prime{
    public static void main(String arg[]){

        int i,n,c,j;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the n value : ");
        n=scanner.nextInt();
        System.out.println("Prime numbers:");

        for(j=2;j<=n;j++){
            c=0;

            for(i=1;i<=j;i++){
                if(j%i==0){
                c++;
                }
            }

            if(c==2){
                System.out.println(j);
            }
            
        }
    }
}