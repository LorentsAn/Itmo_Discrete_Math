//
// Created by Anna on 29.05.2021.
//
 
using namespace std;
 
#include <iostream>
#include <vector>
#include <algorithm>
 
 
 
 
vector<bool> first_state;
vector<bool> second_state;
vector<bool> have;
vector<vector<int>> fisrt_pereh;
vector<vector<int>> second_pereh;
vector<int> pohoj;
int ns;
int ms;
int ks;
int nf;
int mf;
int kf;
 
 
bool dfs(int i1, int i2) {
    have[i1] = true;
    pohoj[i1] = i2;
    bool ans = true;
 
    if (first_state[i1] != second_state[i2])
        return false;
 
    for (int c = 0; c < 26; c++) {
        bool f = fisrt_pereh[i1][c] == nf && second_pereh[i2][c] != ns;
        bool s = fisrt_pereh[i1][c] != nf && second_pereh[i2][c] == ns;
        if (f ||s)
            return false;
        if (have[fisrt_pereh[i1][c]])
            ans = ans & (second_pereh[i2][c] == pohoj[fisrt_pereh[i1][c]]);
        else
            ans = ans & dfs(fisrt_pereh[i1][c], second_pereh[i2][c]);
    }
    return ans;
}
 
int main() {
    freopen ("isomorphism.in", "r", stdin);
    freopen ("isomorphism.out", "w", stdout);
    int first;
    int second;
    char sym;
    int z;
 
    cin >> nf;
    cin >> mf;
    cin >> kf;
 
 
 
 
 
    first_state.resize(nf + 1);
    for (int i = 0; i < nf + 1; i++) {
        first_state[i] = false;
    }
    for (int i = 0; i < kf; i++) {
        cin >> z;
        z--;
        first_state[z] = true;
    }
 
    fisrt_pereh.resize(nf + 1);
    for (int i = 0; i < nf + 1; i++) {
        fisrt_pereh[i].assign(26, nf);
    }
    for (int i = 0; i < mf; i++) {
        cin >> first;
        cin >> second;
        cin >> sym;
        first--;
        second--;
        fisrt_pereh[first][sym - 'a'] = second;
    }
 
    cin >> ns;
    cin >> ms;
    cin >> ks;
 
    second_state.resize(ns + 1);
    for (int i = 0; i < ns + 1; i++) {
        second_state[i] = false;
    }
 
    for (int i = 0; i < ks; i++) {
        cin >> z;
        z--;
        second_state[z] = true;
    }
 
    second_pereh.resize(ns + 1);
    for (int i = 0; i <= ns; i++) {
 
        second_pereh[i].assign(26, ns);
    }
    for (int i = 0; i < ms; i++) {
        cin >> first;
        cin >> second;
        cin >> sym;
        first--;
 
        second--;
        second_pereh[first][sym - 'a'] = second;
    }
 
    have.assign(nf + 1, false);
    pohoj.assign(nf + 1, nf);
 
    if (dfs(0, 0)) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    return 0;
}
