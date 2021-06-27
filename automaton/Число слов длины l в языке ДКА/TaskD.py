//
// Created by Anna on 29.05.2021.
//
 
#include <iostream>
#include <vector>
 
using namespace std;
 
int main() {
    freopen("problem4.in", "r", stdin);
    freopen("problem4.out", "w", stdout);
    int n;
    int m;
    int k;
    int l;
    cin >> n >> m >> k >> l;
    vector<int> transition[101][26];
    int a, b;
    char c;
    long long admit[k];
    int z;
    for (int i = 0; i < k; i++) {
        cin >> z;
        admit[i] = z;
    }
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        transition[b][c - 'a'].push_back(a);
    }
    long long way[l + 1][n + 1];
    for (int i = 0; i < l + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            way[i][j] = 0;
        }
    }
    way[0][1] = 1;
 
    for (int i = 1; i < l + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            for (int b = 0; b < 26; b++) {
                for (int k = 0; k < transition[j][b].size(); k++) {
                    way[i][j] += way[i -1][transition[j][b][k]];
                    way[i][j] %= (1000000000 + 7);
                }
            }
        }
    }
    long long cnt = 0;
    for (int i = 0; i < k; i++) {
        cnt += way[l][admit[i]];
        cnt %= (1000000000 + 7);
    }
 
    /*     for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 26; j++) {
            for (int k = 0; k < perehody[i][j].size(); j++) {
                cout << '\n';
                cout << "i " << i << " j " << j << " k " << k << " ";
                cout << perehody[i][j][k];
            }
        }
 
    }
cout << '\n';
    cout << '\n';
    for (int i = 0; i <= l; ++i) {
        for (int j = 1; j <= n; ++j) {
            cout << "i " << i << " j " << j << ' ';
            cout << way[i][j];
            cout << '\n';
        }
    } */
    cout << cnt;
    return 0;
