#include <set>
using namespace std;
#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>

using namespace boost::multiprecision;

int main(){
    long long s = 1, cnt = 0;
    set<int> uniques;
    for (long i =0; i<300000000; i++){
        uniques.insert(s%2019);
        s = s*10+1;
        cnt++;
    }
    int len = uniques.size();
    cout<<cnt<<" "<<len<<endl;
}