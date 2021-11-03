#include <iostream>
#include <vector>

using namespace std;

template<typename T>
void merge(vector<T> & a, int leftPos, int rightPos, int rightEnd)
{
    int numElements = rightEnd - leftPos + 1;
    vector<T>  tempArray(numElements);

    //main loop
    int iter_a = leftPos;
    int iter_b = rightPos;
    int iter_c = 0;
    while(iter_a <= rightPos - 1 && iter_b <= rightEnd)
        if(a[iter_a] <= a[iter_b])
            tempArray[iter_c++] = move(a[iter_a++]);
        else    
            tempArray[iter_c++] = move(a[iter_b++]);
    
    while(iter_a <= rightPos - 1) //copy rest of first half
        tempArray[iter_c++] = move(a[iter_a++]);

    while(iter_b <= rightEnd) //copy the rest of right half
        tempArray[iter_c++] = move(a[iter_b++]);

    //copy tempArray
    for(iter_c = 0, iter_a = leftPos; iter_c < numElements; iter_c++, iter_a++)
        a[iter_a] = move(tempArray[iter_c]);
}

template<typename T>
void mergeSort(vector<T> & a, int left, int right)
{
    if(left < right){
        int center = (left + right) / 2;
        mergeSort(a, left, center);
        mergeSort(a, center+1, right);
        merge(a, left, center+1, right);
    }
}

template<typename T>
void mergeSort(vector<T> & a)
{
    mergeSort(a, 0, a.size()-1);
}

int main()
{
    vector<int> v;
    int temp;

    while(cin >> temp)
        v.push_back(temp);
    
  
    mergeSort(v);

    for(int i = 0; i < v.size(); i++)
        cout << v[i] << ' ';
    cout << endl;
    return 0;
}