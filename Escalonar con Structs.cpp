#include <bits/stdc++.h>
using namespace std;
int k;
struct vec{
	int dim;
	double *arr;
}*base=new vec[k+1];
int particion(vec *bro,int x,int ini,int fin){
	double pivote=*(bro[fin].arr+x);
	int key=ini;
	for(int i=ini;i<fin;i++){
		if(*(bro[i].arr+x)>pivote){
			swap(bro[i],bro[key]);
			key++;
		}
	}
	swap(bro[key],bro[fin]);
	return key;
}
void quicksort(vec *bro,int x,int ini,int fin){
	if(ini<fin){
		int pivote=particion(bro,x,ini,fin);
		quicksort(bro,x,ini,pivote-1);
		quicksort(bro,x,pivote+1,fin);
	}
}
//n representa la cantidad de filas (vectores)
//length comienza desde 1
void escalonar(vec *bro,int length,int n){
	if(length==n){
		return;
	}
	int abrev=bro[0].dim;
	quicksort(bro,length-1,length,n-1);
	double pivote=*(bro[length].arr+length-1);
	if(pivote==0){
		return escalonar(bro,length+1,n);	
	}
	for(int i=0;i<abrev;i++){
		*(bro[length].arr+i)=*(bro[length].arr+i)/pivote;
	}
	for(int i=1;i<n;i++){
		if(i!=length){
			double pivote2=*(bro[i].arr+length-1);
			for(int j=length-1;j<abrev;j++){
				*(bro[i].arr+j)-= *(bro[length].arr+j)*pivote2;
				}
			}
		}
	escalonar(bro,length+1,n);
}
void rellenar(double *arr,int a){
	for(int i=0;i<a;i++){
		cin>>*(arr+i);
	}
}
void print(vec *example,int n){
	for(int i=1;i<n;i++){
		for(int j=0;j<example[i].dim;j++){
			cout<<setw(8)<<setprecision(2)<<*(example[i].arr+j);
		}
		cout<<endl;
		cout<<endl;
	}
}
int main(){
	srand(time(NULL));
	int dim;
	cout<<"Ingrese la cantidad de vectores:"<<endl;
	cin>>k;
	cout<<"Ingrese la dimension del espacio:"<<endl;
	cin>>dim;
	for(int i=0;i<=k;i++){
		if(i==0){
			base[i].dim=dim;
			base[i].arr=new double[dim];
			for(int j=0;j<dim;j++){
				*(base[i].arr+j)=0;
			}
			continue;
		}
		base[i].dim=dim;
		base[i].arr=new double[dim];
		rellenar(base[i].arr,dim);
	}
	print(base,k+1);
	int f;
	cout<<"Su resultado:"<<endl;
	escalonar(base,1,k+1);
	print(base,k+1);
	return 0;
}