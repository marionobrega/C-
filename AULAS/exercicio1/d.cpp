#include<bits/stdc++.h> 
    using namespace std;
    int main() {
       long long int D;
        while (cin >> D && D != -1) {
            long long int N;
            cin >> N;

            long long int sum = 0;
            while (N > 0) {
                sum += N % 10;
                N /= 10;
            }
            cout << sum << " ";
            cout << (sum % 3 == 0 ? "sim" : "nao") << "\n";
        }
        return 0;
    }
