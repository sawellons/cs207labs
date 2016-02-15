#include "bloom.h"

void set_bit(bloom_filter_t *B, index_t i) {
  index_t bigi = i >> 6;
  index_t littlei = i % 64;
  index_t mask = 1; // = 1 << (64-littlei-1);
  index_t *Btable = B->table;

  // This is ridiculous, but I'm having issues w/ 64 vs 32 bit
  for (index_t j=64; j>littlei; j--) {
    mask = mask*2;
    // printf("%llu\n", mask);
  }

  Btable[bigi] = Btable[bigi] | mask;
}

index_t get_bit(bloom_filter_t *B, index_t i) {
  index_t bigi = i >> 6;
  index_t littlei = i % 64;
  index_t mask = 1; // << (64-littlei-1);
  index_t *Btable = B->table;

  // This is ridiculous, but I'm having issues w/ 64 vs 32 bit
  for (index_t j=64; j>littlei; j--) {
    mask = mask*2;
  }

  if ((Btable[bigi] & mask) == 0) {return 0;}
  else {return 1;}
}

// Simplest possible hash
index_t hash1(bloom_filter_t *B, key_t k) {
  index_t m = B->size;
  return k % m;
}

index_t hash2(bloom_filter_t *B, key_t k) {
  index_t m = B->size;
  return (k+1)*(k+7) % m;
}

void bloom_init(bloom_filter_t *B, index_t size_in_bits) {
  B->size = size_in_bits;
  B->count = 0;
  B->table = (index_t *) malloc(sizeof(index_t)*(size_in_bits/64 + 1));
  for (int i=0; i < size_in_bits/64 + 1; i++) {B->table[i] = 0;}
}

void bloom_destroy(bloom_filter_t *B) {
  free(B->table);
}

int bloom_check(bloom_filter_t *B, key_t k) {
  index_t hashval;
  index_t m = B->size;
  for (int i=0; i<N_HASHES; i++) {
    hashval = (hash1(B,k) + i*hash2(B,k)) % m;
    if (get_bit(B, hashval) == 0) {return 0;}
  }
  return 1;
}

void bloom_add(bloom_filter_t *B, key_t k) {
  index_t hashval;
  index_t m = B->size;
  B->count += 1;
  for (int i=0; i<N_HASHES; i++) {
    hashval = (hash1(B,k) + i*hash2(B,k)) % m;
    set_bit(B, hashval);
  }
}
