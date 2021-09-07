#include<iostream>
#include<string.h>
using namespace std;

string keyexpand(string str,string key){
    string ori_key=key;
    if(str.length()>key.length()){
        int quo=str.length()/key.length();
        int rem=str.length()%key.length();
        for(int i =0;i<quo-1;i++){
            key+=ori_key;
        } 
        for(int i =0;i<rem;i++){
            key+=ori_key[i];
        }
    }
    cout<<"After key expand :"<<key<<endl;
    return key;
}

string encrypt(string str,string key){
    for(int i=0;i<str.length();i++){
        int keys=key[i];
        int plain_text=str[i];
        str[i]=(char)(((keys+plain_text)%26)+65);
    }
    cout<<"After encryption :"<<str<<endl;
    return str;
}


string decrypt(string str,string key){
    for(int i=0;i<str.length();i++){
        int keys=key[i];
        int plain_text=str[i];
        str[i]=(char)(((plain_text-keys+26)%26)+65);
    }
    cout<<"After decryption :"<<str<<endl;
    return str;
}

int main(){
    string key,str;
    cout<<"Enter key string in caps :";
    cin>>key;
    cout<<"Enter plain string in caps :";
    cin>>str;
    key=keyexpand(str,key);
    str=encrypt(str,key);
    decrypt(str,key);
}
