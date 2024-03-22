#include <stdio.h>


#define MAX_LOAD_FACTOR 0.5

/* 구현 */
typedef struct pair {
	char* key;				// key는 문자열
	int value;
}pair;

pair* make_pair(char* key, int value) {
	pair* new_pair = (pair*)malloc(sizeof(pair));

	new_pair->key = strdup(key);
	new_pair->value = value;

	return new_pair;
}

/* 구조체 */
typedef enum state {
	EMPTY,
	USED,
	DELETED
}state;

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

/* initialize */
void initialize(hash* hash) {
	hash->bucket = NULL;
	hash->capacity = 0;
	hash->size = 0;
}

static unsigned hashing(unsigned char* str) {
	unsigned int hash = 5381;

	while (*str != '\0') {
		hash = hash * 33 + *str;
		++str;
	}

	return hash;
}

void insert(hash* hash, pair* data) {
	if (hash->capacity == 0 || (double)hash->size / hash->capacity > MAX_LOAD_FACTOR)
		re_allocate(hash, hash->capacity * 2);

	unsigned int hash_value = hashing((unsigned char*)data->key);
	unsigned int idx = hash_value;

	while (hash->bucket[idx % hash->capacity].state == USED) {
		if (strcmp(hash->bucket[idx % hash->capacity].data->key, data->key) == 0)
			return;
		++idx;
	}
}