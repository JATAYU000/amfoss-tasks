#include<iostream>
#include<list>
int main()
{

    int x;
    std::list<int> prime = {2};

    std::cout<<"\nEnter the range: ";
    std::cin>>x;
    if(x==1 || x==0){
            std::cout<<"no prime";
        }
    else if (x==2)
        {
            std::cout<<"2";
        }
    else{
        for(int i=2;i<=x;i++)
        {
            int c = prime.size();
            int y = 0;
            for(int j : prime)
            {
                if(i%j==0)
                {
                    continue;
                }
                else
                {
                    y++;
                }
            }

            if(y==c)
            {
                prime.push_back(i);
            }
        }

        for(int i :prime)
        {
            std::cout<<i<<"\n";
        }
    }

return 0;

}