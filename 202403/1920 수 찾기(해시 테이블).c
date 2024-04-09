#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>


#define MAX_LOAD_FACTOR 0.5
#define INITIAL_CAPACITY 7

typedef enum { false, true} bool;

/* 구현 */
typedef struct pair {
	char* key;				// key는 문자열
	int value;
}pair;

/* 구조체 */
typedef enum state {
	EMPTY,
	USED,
	DELETED
}state;

/* 해시 노드 */
typedef struct node {
	state state;
	pair* data;
	unsigned int hash_value;
}node;


typedef struct hash {
	node* bucket;
	int size;
	int capacity;
}hash;

pair* make_pair(char* key, int value);
void initialize(hash* hash);
static unsigned hashing(unsigned char* str);
void insert(hash* hash, pair* data);
static int find_idx(hash* hash, char* key);
void erase(hash* hash, char* key);
pair* find(hash* hash, char* key);
static int get_next_prime(int num);
static void re_allocate(hash* hash, int size);
void clear(hash* hash);
void print_hash(hash* hash);
void print_hash_find(pair* result);


pair* make_pair(char* key, int value) {
	pair* new_pair = (pair*)malloc(sizeof(pair));
	if (new_pair == NULL) free (new_pair);

	new_pair->key = strdup(key);					// malloc을 호출하여 string의 사본에 대한 기억장치 공간을 예약한다.
	new_pair->value = value;

	return new_pair;
}

/* initialize */
void initialize (hash* hash) {
	hash->bucket = NULL;
	hash->capacity = 0;
	hash->size = 0;
}

/* hash function */
static unsigned hashing (unsigned char* str) {
	unsigned int hash = 5381;

	while (*str != '\0') {
		hash = hash * 33 + *str;
		++str;
	}

	return hash;
}

/* insert data */
void insert (hash* hash, pair* data) {
	unsigned int hash_value = hashing((unsigned char*)data->key);
	unsigned int idx = hash_value;
	
	if (hash->capacity == 0 || (double) hash->size / hash->capacity > MAX_LOAD_FACTOR)
		re_allocate (hash, hash->capacity * 2);

	while (hash->bucket [idx % hash->capacity].state == USED) {
		if (strcmp (hash->bucket [idx % hash->capacity].data->key, data->key) == 0)
			return;
		++idx;
	}
}

/* serching data by index */
static int find_idx (hash* hash, char* key) {
	unsigned int hash_value = hasing((unsigned char*)key);
	unsigned int idx = hash_value;

	for (int i = 0; i < hash->capacity; ++i, ++idx) {
		if (hash->bucket[idx % hash->capacity].state == EMPTY) break;
		if (hash->bucket[idx % hash->capacity].state == DELETED) continue;
		if (strcmp(hash->bucket[idx % hash->capacity].data->key, key) == 0) return idx % hash->capacity;
	}
	
	return -1;
}

/* erase data */
void erase (hash* hash, char* key) {
	int idx = find_idx(hash, key);
	if (idx == -1) return;

	free(hash->bucket[idx].data->key);
	free(hash->bucket[idx].data);

	hash->bucket[idx].state = DELETED;
	--hash->size;
}

/* search data */
pair* find (hash* hash, char* key) {
	int idx = find_idx(hash, key);

	if (idx == -1) return NULL;

	return hash->bucket[idx].data;
}

/* searching next prime number */
static int get_next_prime (int num) {
	while (true) {
		bool is_prime = true;

		for (long long i = 2; i * i <= num; ++i) {
			if (num % i == 0) {
				is_prime = false;
				break;
			}
		}

		if (is_prime) return (num);
		++num;
	}
}

static void re_allocate(hash* hash, int size) {
	int prev_capacity = hash->capacity;

	if (size == 0)
		hash->capacity = INITIAL_CAPACITY;
	else
		hash->capacity = get_next_prime(size);

	node* new_bucket = (node*)malloc(hash->capacity * sizeof(node));
	for (int i = 0; i < hash->capacity; ++i)
		new_bucket[i].state = EMPTY;

	for (int i = 0; i < prev_capacity; ++i)
	{
		if (hash->bucket[i].state != USED)
			continue;
		unsigned int idx = hash->bucket[i].hash_value;

		while (new_bucket[idx % hash->capacity].state == USED)
		{
			if (strcmp(new_bucket[idx % hash->capacity].data->key, hash->bucket[i].data->key) == 0)
				return;
			++idx;
		}

		new_bucket[idx % hash->capacity] = (node){ USED, hash->bucket[i].data, hash->bucket[i].hash_value };
	}
	free(hash->bucket);
	hash->bucket = new_bucket;
}

/* delete all data */
void clear(hash* hash) {

	for (int i = 0; i < hash->capacity; ++i) {

		if (hash->bucket[i].state == USED) {
			free(hash->bucket[i].data->key);
			free(hash->bucket[i].data);

		}
	}

	free (hash->bucket);
	initialize (hash);
}

void print_hash(hash* hash)
{
	printf("size: %d, cap: %d\n", hash->size, hash->capacity);
	for (int i = 0; i < hash->capacity; ++i)
	{
		switch (hash->bucket[i].state)
		{
		case 0:
			printf("[%d] EMPTY   , - : - [-]\n", i);
			break;
		case 1:
			printf("[%d] USED    , %s : %d [%u]\n", i, hash->bucket[i].data->key, hash->bucket[i].data->value, hash->bucket[i].hash_value % hash->capacity);
			break;
		case 2:
			printf("[%d] DELETED , - : - [-]\n", i);
			break;
		}
	}
	printf("\n");
}

void print_hash_find(pair* result)
{
	if (result == NULL)
		printf("key not found\n");
	else
		printf("%d\n", result->value);
}

int main()
{
	hash hash;
	int num1, num2;

	scanf_s("%d", &num1);

	/* 배열의 동적 할당 */
	int* arr1 = (int*)malloc(num1 * sizeof(int));
	if (arr1 == NULL) {
		printf("Memory allocation failed.\n");
		return -1;
	}

	/* 수 입력 */
	for (int i = 0; i < num1; i++) {
		scanf_s("%d", &arr1[i]);
	}

	/* 해시 테이블 초기화 */
	initialize(&hash);

	/* 입력받은 수 해시 테이블 삽입 */
	for (int i = 0; i < num1; i++) {
		struct pair *pair = make_pair("hello", arr1[i]);
		insert(&hash, pair);
	}

	/* 문제 입력 */
	scanf_s("%d", &num2);
	int* arr2 = (int*)malloc(num2 * sizeof(int));
	for (int i = 0; i < num2; i++) {
		scanf_s("%d", &arr2[i]);
	}

	/* 해시 테이블에서 인덱스로 찾고 bool 값 출력 */
	for (int i = 0; i < num2; i++) {
		if (find(&hash, arr2[i])) printf("1\n");
		else printf("0");
	}
}

//
//pair* make_pair(char* key, int value);
//void initialize(hash* hash);
//static unsigned hashing(unsigned char* str);
//void insert(hash* hash, pair* data);
//static int find_idx(hash* hash, char* key);
//void erase(hash* hash, char* key);
//pair* find(hash* hash, char* key);
//static int get_next_prime(int num);
//static void re_allocate(hash* hash, int size);
//void clear(hash* hash);
//void print_hash(hash* hash);
//void print_hash_find(pair* result);

///* 배열의 포인터 연산 연습 */
//#include <stdio.h>
//
//int main() {
//	int arr[3] = { 10, 20, 30 };
//
//	printf("배열의 이름을 이용하여 배열 요소에 접근 : %d, %d, %d\n", arr[0], arr[1], arr[2]);
//	printf("배열의 이름으로 포인터 연산을 한 뒤 배열 요소에 접근 : %d %d %d\n", *(arr + 0), *(arr + 1), *(arr + 2));
//
//	/* arr이 배열의 이름이거나 포인터이고 n이 정수일 때, arr[n] == **(arr + n) */
//}
