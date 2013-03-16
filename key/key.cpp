#include<iostream>
#include<stdio.h>
#include<cstring>
#include<malloc.h>
#include<stdlib.h>


using namespace std;
//存储表的大小
const unsigned long nTableSize = 387039;

unsigned long cryptTable[0x500];

typedef struct  
{  
    int nHashA;  
    int nHashB;  
    char bExists;  
} MPQHASHTABLE;

//函数prepareCryptTable以下的函数生成一个长度为0x501（合10进制数：1280）\
	的cryptTable[0x500]  
void prepareCryptTable()
{
    unsigned long seed = 0x00100001, index1 = 0, index2 = 0, i;

    for( index1 = 0; index1 <0x100; index1++ )
    {
        for( index2 = index1, i = 0; i < 5; i++, index2 += 0x100)  
        {  
            unsigned long temp1, temp2;  
            seed = (seed * 125 + 3) % 0x2AAAAB;  
            temp1 = (seed & 0xFFFF)<<0x10;  
            seed = (seed * 125 + 3) % 0x2AAAAB;  
            temp2 = (seed & 0xFFFF);  
            cryptTable[index2] = ( temp1 | temp2 );  
        }  
    }  
}  
  
//函数HashString以下函数计算lpszFileName 字符串的hash值，其中dwHashType 为hash的类型，  
unsigned long HashString(const char *lpszkeyName, unsigned long dwHashType )  
{  
    unsigned char *key  = (unsigned char *)lpszkeyName;  
    unsigned long seed1 = 0x7FED7FED;  
    unsigned long seed2 = 0xEEEEEEEE;  
    int ch;  
  
    while( *key != 0 )  
    {  
        ch = *key++;  
        seed1 = cryptTable[(dwHashType<<8) + ch] ^ (seed1 + seed2);  
        seed2 = ch + seed1 + seed2 + (seed2<<5) + 3;  
    }  
    return seed1;  
}  
  
/////////////////////////////////////////////////////////////////////  
//function: 哈希词典 编码  
//parameter:  
//author: lei.zhou  
//time: 2011-12-14  
/////////////////////////////////////////////////////////////////////  

//存放关键词的哈希值，顺序存储
MPQHASHTABLE TestHashTable[nTableSize];  
//int for what? C D are what
int TestHashCTable[nTableSize];  
int TestHashDTable[nTableSize];  

typedef struct KEYNODE {
	unsigned long weight;
	char* pkey;//
} *key_list;
//
key_list test_data[nTableSize];  

unsigned long nMaxStrLen = 2048;

//直接调用上面的hashstring，nHashPos就是对应的HASH值
int insert_string(const char *string_in)
{
    const int HASH_OFFSET = 0, HASH_C = 1, HASH_D = 2;  
    unsigned int nHash = HashString(string_in, HASH_OFFSET);  
    unsigned int nHashC = HashString(string_in, HASH_C);//暴雪
    unsigned int nHashD = HashString(string_in, HASH_D);  //暴雪
    unsigned int nHashStart = nHash % nTableSize; //查找的起始位置
    unsigned int nHashPos = nHashStart;
    int ln, ires = 0;  
  
    while (TestHashTable[nHashPos].bExists)  
    {  
		//      if (TestHashCTable[nHashPos]  == (int) nHashC && \
						TestHashDTable[nHashPos] == (int) nHashD)  
		//          break;  
		//      //...  
		//      else  
        //如之前所提示读者的那般，暴雪的Hash算法对于查询那样处理可以，\
			但对插入就不能那么解决  
            nHashPos = (nHashPos + 1) % nTableSize;  
  
        if (nHashPos == nHashStart)  
            break;  
    }  
  
    ln = strlen(string_in);

    if (!TestHashTable[nHashPos].bExists && (ln < nMaxStrLen))
    {   
        TestHashCTable[nHashPos] = nHashC;  
        TestHashDTable[nHashPos] = nHashD;  
  
        test_data[nHashPos] = (KEYNODE *) malloc (sizeof(KEYNODE) * 1);  
        if(test_data[nHashPos] == NULL)  
        {  
            printf("10000 EMS ERROR !!!!\n");  
            return 0;  
        }  
  
        test_data[nHashPos]->pkey = (char *)malloc(ln+1);  
        if(test_data[nHashPos]->pkey == NULL)  
        {
            printf("10000 EMS ERROR !!!!\n");  
            return 0;  
        }
  
        memset(test_data[nHashPos]->pkey, 0, ln+1);  
        strncpy(test_data[nHashPos]->pkey, string_in, ln);  
        *((test_data[nHashPos]->pkey)+ln) = 0;  
        test_data[nHashPos]->weight = nHashPos;  
  
        TestHashTable[nHashPos].bExists = 1;  
    }  
    else  
    {  
        if(TestHashTable[nHashPos].bExists)  
            printf("30000 in the hash table %s !!!\n", string_in);  
        else  
            printf("90000 strkey error !!!\n");  
    }  
    return nHashPos;  
}  
unsigned long TERM_MAX_LENG = 2048;
unsigned long WORD_MAX_LENG = 2048;
unsigned long BUFF_MAX_LENG = 2048;

//a get real length of string
int GetRealString(const char* string_in){
	char * p = (char*)string_in;
	if(p==NULL || *p=='\0' ){
		return -1;
	}
	int len = 0;
	len = strlen(string_in);
	return len;
}

/////////////////////////////////////////////////////////////////////
//
/////////////////////////////////////////////////////////////////////
void bigIndex_hashcode(const char *in_file_path, const char *out_file_path)  
{  
    FILE *fr, *fw;  
    int len, value;  
    char *pbuf, *pleft, *p;  
    char keyvalue[TERM_MAX_LENG], str[WORD_MAX_LENG];  
  
    if(in_file_path == NULL || *in_file_path == '\0') {  
        printf("input file path error!\n");  
        return;  
    }  
  
    if(out_file_path == NULL || *out_file_path == '\0') {  
        printf("output file path error!\n");  
        return;  
    }  
  
    fr = fopen(in_file_path, "r");  //读取in_file_path路径文件  
    fw = fopen(out_file_path, "w");  
  
    if(fr == NULL || fw == NULL)  
    {  
        printf("open read or write file error!\n");  
        return;  
    }  
  
    pbuf = (char*)malloc(BUFF_MAX_LENG);  
    pleft = (char*)malloc(BUFF_MAX_LENG);  
    if(pbuf == NULL || pleft == NULL)  
    {  
        printf("allocate memory error!");  
        fclose(fr);  
        return ;  
    }  
  
    memset(pbuf, 0, BUFF_MAX_LENG);  
  
    int offset = 1;  
    while(fgets(pbuf, BUFF_MAX_LENG, fr))  
    {  
        if (--offset > 0)  
            continue;  
  
        if(GetRealString(pbuf) <= 1)  
            continue;  
  
  
        p = strstr(pbuf, " ");  
        if (p == NULL)  
        {  
            printf("file contents error!");  
        }  
		while( p!=NULL && *p!='\0' && (*p<='9' && *p>='0' )){
			p++;
		}
		p++;
		
		char* pend = strstr(pbuf, "\n");
	
        len = p - pbuf;//get length of key
  		len--;
        // 确定跳过行数
        strncpy(pleft, pbuf, len);
  
        strncpy(keyvalue, p, pend-p);
        keyvalue[pend-p] = '\0';  
        value = insert_string(keyvalue);//insert and get pos in hashtable
  
        if (value != -1) {  
            // 将key value写入文件  
            //fprintf (fw, "%s\n", keyvalue);  
			fprintf(fw, "%d %s %s\n", value, pleft, keyvalue);
        }  
    }  
    free(pbuf);  
    fclose(fr);  
    fclose(fw);  
}  


int main()  
{  
    prepareCryptTable();  //Hash表起初要初始化  
  
    //现在要把整个big_index文件插入hash表，以取得编码结果  
    bigIndex_hashcode("words.txt", "hashmap.txt");  
    system("pause");  
  
    return 0;  
}  
