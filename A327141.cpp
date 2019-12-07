#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
int main() {
int n;
cin>>n;
vector <int> v;
for (int i=1; i<=n; i++)
{int count=0;
for (int j=1; j<=i; j++)
for (int k=j; k<=i; k++)
{count++; }
//Diagonally placed ii-length, jj-width of diagonal rectangle
for (int ii=i+1; ii<=int(sqrt(2)*i); ii++)
     for (int jj=1; jj<=i; jj++)
          if ((double(i)-double(ii)/sqrt(2))-double(jj)/sqrt(2)>0)
                    {count++; }
v.push_back(count);
}

for (int i=0; i<v.size(); i++) cout << v[i] << ", ";
return 0;
}
